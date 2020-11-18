# Deep-Dive-into-COVID-Backend/dev_backend
This branch serves as a playground for development and testing. All non-final files are to be placed here from
backend.<br /> <br />
See docs for API description. <br />
For accessing firebase contact dev lead for service credentials. <br />
## API 

The API can be found at : https://td-coviz.herokuapp.com/ <br />

The above URL may change due to operation constraints of the Heroku platform.<br />
At the moment the available endpoints are:
* /api/hew
* /api/options/<string:datatype>
* /api/options/countries
* /api/options/charts
<<<<<<< HEAD
* /api/charts/<string:visualization> <br /><br />
Example:<br />
=======
* /api/charts/<string:visualization>

<br />Example:<br />
>>>>>>> c69959a866eab7609c7f4caff5fad7b8d940826b

    curl https://td-coviz.herokuapp.com/hew


The above will produce an JSON file with the following contents

    {"Greeting": "Hello World"}



