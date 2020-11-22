from flask import Flask
from flask import request
from flask import make_response
from flask_restful import Api, Resource
from flask_cors import CORS
import visualization as viz
import preprocessing

#See API documentation and SDD for more details. 
#Flask docs: https://flask.palletsprojects.com/en/1.1.x/
#Flask-RESTful docs: https://flask-restful.readthedocs.io/en/latest/
#Visualization docs: See SDD and visualizaton module for more support.
#Preprocessing docs: See SDD and preprocessing module for more support.

#Postman was very helpful in testing and validation. Although the desktop version was the 
#only way to use the software. The website was unresponsive and buggy so I would 
#strongly recommend the Desktop version. 
# ~Shankar 

#Postman website: https://www.postman.com/

version = "0.2.6"

# Todo: Implement CORS support
# Look at : 
# https://stackoverflow.com/questions/19962699/flask-restful-cross-domain-issue-with-angular-put-options-methods
# for a possible fix

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


#PS DEVS: You can change the function args once you achieve functionality described in the docstring.

#Denelle
@api.resource('/api/options/<string:datatype>')
class Headings(Resource):
    def get(self,datatype):
        '''
        Return a JSON file containg the requested headings
        Read the csv from firebase and collect all string columns into categorical
        '''
        ret = []
        if(datatype == "numerical"):
            ret = preprocessing.getHeadings(datatype)

        elif(datatype == "categorical"):
            ret = preprocessing.getHeadings(datatype)
        else:
            return "Invalid heading type", 400
        
        return ret, 200

@api.resource('/api/options/countries')
class Countries(Resource):
    def get(self): #Change to fetch countries directly from firebase
        df = preprocessing.pd.read_csv('test.csv')
        return list(df['location'].unique()), 200

@api.resource('/api/options/charts')
class ChartOptions(Resource):
    def get(self):
        return ["lineplot","piechart","barchart"],200

#Shankar
@api.resource('/api/charts/<string:visualization>')
#@cross_origin()
class Image(Resource):
    #def options():
    #    return {'Allow' : 'PUT' }, 200, { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods' : 'PUT,GET' }
    def put(self,visualization):
        '''
        Returns html string containing the visualization
        '''
        
        if request.is_json:

            # Parse the JSON into a Python dictionary
            req = request.get_json()

            # Print the dictionary
            #print(req)

            # Return a string along with an HTTP status code
            # return "JSON received!", 200
            
            if(visualization == "lineplot"):
                #html_text =  viz.makeLineplot(req) #how do i get the passed json file?
                #Html_file= open("resp.html","w")
                #Html_file.write(html_text)
                #Html_file.close()
                #return "Lineplot generated in index.html", 200
                #return viz.makeLineplot(req), 200, {'content-type': 'text/html'}
                #text = viz.makeLineplot(req)



                resp = make_response(viz.makeLineplot(req))
                resp.status_code = 201
                #resp.headers['Access-Control-Allow-Origin'] = '*'
                resp.mimetype = 'application/json'
                return resp
                

                # file = open("sample.html","w")
                # file.write(text)
                # file.close()
                # #print(text)
                # return {'raw_html':'Viz html'}, 200
            else:
                return "JSON received!, but not for a lineplot", 200
        else:
            # The request body wasn't JSON so return a 400 HTTP status code
            return "Request was not JSON", 400



if __name__ == '__main__':
    app.run()
