import pyrebase
import pandas as pd
import httplib2
import preprocessing as prp
import firebaseInterface as fbase

version = '0.0.5'

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


#print(server_path)

def job():
    #print('This job is run every day at 10pm.')

    df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    df.to_csv('data.csv')
    local_path = 'data.csv'

    #Uploading unrefined data
    fbase.upload_file(local_path,fbase.getRawPath())

    #Cleaning and uploading refined data
    prp.refineData(df)
    df.to_csv('data.csv')
    fbase.upload_file(local_path,fbase.getCleanPath())
    
    print('Job Completed')
    

job()



 
 def getVersion():
    """
        Returns the version of the python module
    """
    print("Version: {}".format(version))



