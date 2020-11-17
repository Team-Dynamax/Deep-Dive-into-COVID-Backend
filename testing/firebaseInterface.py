import pandas as pd
import numpy as np
import pyrebase

version = "0.0.0"
    

firebaseConfig = {
        "apiKey": "AIzaSyBlLrs2zKP0C5nwG97aE4wpMoiQH5ulAlE",
        "authDomain": "team-dynamax-covid-analysis.firebaseapp.com",
        "databaseURL": "https://team-dynamax-covid-analysis.firebaseio.com",
        "projectId": "team-dynamax-covid-analysis",
        "storageBucket": "team-dynamax-covid-analysis.appspot.com",
        "messagingSenderId": "1008748926410",
        "appId": "1:1008748926410:web:502ae4316de66cb9b96b33",
        "measurementId": "G-7E0GF07TV9",
        "serviceAccount": "team-dynamax-covid-analysis-09c34cfe9f24.json"
    }



def upload_file(local_path,server_path):
    """
    This  function should upload the file specified in client_url onto firebase
    into server url
    Eg. 
    >>upload_file("images/cat.png","visualizations/cat.png")
    Firebase storage: 
    visualisations ---| ..
                      | <random files if any>
                      | ..
                      |->cat.png
    """
    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()
    storage.child(server_path).put(local_path)


def fetch_file(local_path,server_path):
    """
        This function should fetch the file in the url as specified and download it into the
        client working directory by the url specified as client_url.
        Eg.
        >>fetch_file("downloaded.svg","visualizations/sample.svg")
        local workspace -----| ..
                             | <random files if any>
                             | ..
                             |->downloaded.svg
        """
    firebase = pyrebase.initialize_app(firebaseConfig)
    storage = firebase.storage()
    storage.child(server_path).download(local_path)


def getVersion():
    """
        Returns the version of the python module
    """
    print("Version: {}".format(version))

#Testing :)
#upload_file("test_img.svg","visualizations/sample.svg")
#getVersion()
#fetch_file("x.svg","visualizations/sample.svg")