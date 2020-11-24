from flask import Flask
from flask import request
from flask import make_response
from flask_restful import Api, Resource
from flask_cors import CORS
import visualization as viz
import preprocessing as prp
import firebaseInterface as fbase

# See API documentation and SDD for more details. 
# Flask docs: https://flask.palletsprojects.com/en/1.1.x/
# Flask-RESTful docs: https://flask-restful.readthedocs.io/en/latest/
# Postman website: https://www.postman.com/

version = "0.3.1"

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


#Just ya typical Hi there
@api.resource('/api/hello')
class HelloWorld(Resource):
    def get(self):
        return {"Greeting":"Hello World"} #put a stub here that calls headings from csv file on server


@api.resource('/api/options/<string:datatype>')
class Headings(Resource):
    def get(self,datatype):
        '''
        Return a JSON file containg the requested headings
        Read the csv from firebase and collect all string columns into categorical
        '''
        ret = []
        if(datatype == "numerical"):
            ret = prp.getHeadings(datatype)

        elif(datatype == "categorical"):
            ret = prp.getHeadings(datatype)
        else:
            return "Invalid heading type", 400
        
        return ret, 200

@api.resource('/api/options/countries')
class Countries(Resource):
    def get(self): #Change to fetch countries directly from firebase
        fbase.fetch_file('tmp.csv',fbase.getCleanPath())
        df = prp.pd.read_csv('test.csv')
        return list(df['location'].unique()), 200

@api.resource('/api/options/charts')
class ChartOptions(Resource):
    def get(self):
        return ["lineplot","piechart","barchart"],200


@api.resource('/api/charts/<string:visualization>')
class Standalone(Resource):
    def put(self,visualization):
        '''
        Returns html string containing the visualization
        '''
        
        if request.is_json:

            # Parse the JSON into a Python dictionary
            req = request.get_json()

            
            if(visualization == "lineplot"):

                resp = make_response(viz.makeLineplot(req))
                resp.status_code = 201
                #resp.headers['Access-Control-Allow-Origin'] = '*'
                resp.mimetype = 'application/json'
                return resp
                
            elif(visualization == "piechart"):
                resp = make_response(viz.makePiechart(req))
                resp.status_code = 201
                resp.mimetype = 'application/json'
                return resp

            elif(visualization == "barchart"):
                resp = make_response(viz.makeBarchart(req))
                resp.status_code = 201
                #resp.headers['Access-Control-Allow-Origin'] = '*'
                resp.mimetype = 'application/json'
                return resp
            else:
                return "JSON received!, but not for a lineplot", 200
            
        else:
            # The request body wasn't JSON so return a 400 HTTP status code
            return "Request was not JSON", 400


if __name__ == '__main__':
    app.run(debug=True)
