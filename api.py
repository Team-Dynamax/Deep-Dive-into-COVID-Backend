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

version = "0.0.6"



app = Flask(__name__)
CORS(app, resources=r'/api/*', headers='Content-Type')
api = Api(app)



#Just ya typical Hi there
@api.resource('/api/hew')
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
        
        return {datatype:ret}, 200

@api.resource('/api/options/countries')
class Countries(Resource):
    def get(self):
        return {"countries":['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
       'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
       'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
       'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
       'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso',
       'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
       'Cayman Islands', 'Central African Republic', 'Chad', 'Chile',
       'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica',
       "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus',
       'Czech Republic', 'Democratic Republic of Congo', 'Denmark',
       'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Faeroe Islands', 'Falkland Islands', 'Fiji',
       'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia',
       'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
       'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
       'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong',
       'Hungary', 'Iceland', 'India', 'Indonesia', 'International',
       'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
       'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
       'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
       'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia',
       'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
       'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
       'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar',
       'Namibia', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'Northern Mariana Islands',
       'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama',
       'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
       'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'San Marino',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore',
       'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
       'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
       'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
       'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo',
       'Trinidad and Tobago', 'Tunisia', 'Turkey',
       'Turks and Caicos Islands', 'Uganda', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States',
       'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vatican',
       'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara',
       'World', 'Yemen', 'Zambia', 'Zimbabwe']}, 200

@api.resource('/api/options/charts')
class ChartOptions(Resource):
    def get(self):
        return {"charts":["lineplot","piechart","barchart"]},200

#Shankar
@api.resource('/api/charts/<string:visualization>')
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
                #return viz.makeLineplot(req), 200, {'content-type': 'text/html'}
                #text = viz.makeLineplot(req)



                resp = make_response(viz.makeLineplot(req))
                resp.status_code = 200
                resp.mimetype = 'text/html'
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

