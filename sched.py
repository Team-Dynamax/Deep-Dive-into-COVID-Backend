import pyrebase
import firebase
import pandas as pd
from firebase_admin import credentials, initialize_app, storage
import httplib2
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import schedule 
import time

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

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
df.to_csv('data.csv')

local_path = 'data.csv'
server_path = 'team-dynamax-covid-analysis.appspot.com/Cleaned Data'
def upload_file(local_path,server_path):
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
    storage.child(server_path).put(local_path)




def job():
    print('This job is run every day at 10pm.')
    #today = date.today()
    now = datetime.now() # current date and time

    year = now.strftime("%Y")
    #print("year:", year)

    month = now.strftime("%m")
    #print("month:", month)

    day = now.strftime("%d")
    #print("day:", day)

    time = now.strftime("%H:%M:%S")
    #print("time:", time)

    date_time = now.strftime("%m-%d-%Y,%H:%M:%S")
    print("date and time:",date_time)
    #print(type(date_time))

    
    upload_file('data.csv','UnProcessed Data/'+date_time +'/data.csv')
    print('Job Completed')
    


schedule.every().day.at("22:00").do(job)

# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)

#print(os.system('dir'))
 
