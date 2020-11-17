# Deep-Dive-into-COVID-Backend/dev_backend
This branch serves as a playground for development and testing. All non-final files are to be placed here from
backend.

See docs for API description

For accessing firebase contact dev lead for service credentials.
<br />
## API 

The API can be found at : https://td-coviz.herokuapp.com/
<br />
The above URL may change due to operation constraints of the Heroku platform.
At the moment the available endpoints are:
*/api/hew
*/api/options/<string:datatype>
*/api/options/countries
*/api/options/charts
*/api/charts/<string:visualization>

Example:
<br />
code(curl https://td-coviz.herokuapp.com/hew)

The above will produce an JSON file with the following contents

code({"Greeting": "Hello World"})


