from flask import Flask
from flask import request
from flask_restful import Api, Resource
import visualization as viz
from flask import jsonify
import preprocessing

app = Flask(__name__)
api = Api(app)


#Just ya typical Hi there
class HelloWorld(Resource):
    def get(self):
        return {"Greeting":"Hello World"} #put a stub here that calls headings from csv file on server

api.add_resource(HelloWorld, "/hew")

#PS DEVS: You can change the function args once you achieve functionality described in the docstring.

#Denelle
class Dropdown(Resource):
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
        
        return {datatype:ret}, 200

#Shankar
class Image(Resource):
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
                return viz.makeLineplot(req), 200
            else:
                return "JSON received!, but not for a lineplot", 200
            

        else:

            # The request body wasn't JSON so return a 400 HTTP status code
            return "Request was not JSON", 400

api.add_resource(Dropdown, '/options/<string:datatype>')
api.add_resource(Image, '/charts/<string:visualization>')

if __name__ == '__main__':
    app.run(debug=True)

