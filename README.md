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
* /api/charts/<string:visualization>

Example:<br /><br />
`curl https://td-coviz.herokuapp.com/api/hew`<br /><br />
Above will produce a hello world output <br /><br />
`{"Greeting": "Hello World"}`



## Dependancies

This API utilizes httplib2 version 0.15.0 and google-api-python-client version 1.7.11 to work around an internal error in firebases's implementation.
See shorturl.at/hiF89 for more info on this issue and the fix.

 
