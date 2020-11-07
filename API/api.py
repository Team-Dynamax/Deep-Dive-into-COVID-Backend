from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

'''
API Documentation: https://app.swaggerhub.com/apis-docs/team-dynamax/COVIZ/1.0.0#/
'''


class HelloWorld(Resource):
    def get(self):
        return {"Greeting":"Hello World"} #put a stub here that calls headings from csv file on server

api.add_resource(HelloWorld, "/hew")

#PS DEVS: You can change the function args once you achieve functionality described in the docstring.

#Denelle
class Dropdown(Resource):
    def get(self):
        '''
        Return a JSON file containg the requested headings
        '''
        pass

#Sa'id
class Image(Resource):
    def put(self):
        '''
        Returns a JSON file containing a the SVG image as a string.
        '''
        pass

api.add_resource(Dropdown, '/options/<datatype>')
api.add_resource(Image, '/charts/<visualization>')

if __name__ == '__main__':
    app.run(debug=True)

