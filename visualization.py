import pandas as pd
import numpy as np
import json
import firebaseInterface as fi
import plotly
import plotly.express as px




version = '0.0.6'


def makeLineplot(data):
    #return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>Hello World</body></html>"

    #Grabbing locations and feature from user json request
    locations = data['countries']
    feature = data['feature']

    #fi.fetch_file('temp.csv','Cleaned Data/cleaned_data_test.csv') #consider using a url instead of downloading data
    df = pd.read_csv('test.csv')



    if(len(feature) == 0):
        return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>No feature passed</body></html>"

    #make dataframe subset of countries requested
    if (len(locations) == 0):
        return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>No countries passed</body></html>"
    elif (len(locations) == 1):
        df = df[df['location'] == locations[0]]
    else:
        df = df[df['location'].isin(locations)]

    #converting the date column to a datetime type column to allow neater and cleaner visualization
    df['date'] = pd.to_datetime(df['date'])


    # gen plot
    fig = px.line(df, x="date", y=feature, color="location",
              line_group="location") 

    return plotly.io.to_json(fig)
    

        


def makeBarchart(usr_request):
    '''
        Generates a barplot with one or more countries for the features specified. 
        
        Returns an html string containg the figure via the mpld3 library

    '''
    return {"Status":"Under Construction"}

def makePiechart(data):
    '''
        Generates a piechart with two or more countries for the features specified. 
        
         Returns an html string containg the figure via the mpld3 library

    '''
        #return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>Hello World</body></html>"

    #fi.fetch_file('temp.csv','Cleaned Data/cleaned_data_test.csv') #consider using a url instead of downloading data
    df = pd.read_csv('test.csv')

    #data = {'feature':"new_deaths"}
    #Grabbing locations and feature from user json request
    locations = data['countries']
    feature = data['feature']
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['location'].isin(locations)]
    



    if(len(feature) == 0):
        return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>No feature passed</body></html>"

    fig = px.pie(df, values=feature, names='location')
    #fig.show()
    
    return plotly.io.to_json(fig)

def getSummary():
    '''
        Displays a table showcasing general information about a country.
        Implement however you think make sense,
    '''

def getVersion():
    """
        Returns the version of the python module
    """
    print("Version: {}".format(version))

#Testing
#x = makeLineplot('test_req.json')
#x = makePiechart('test_req.json')
