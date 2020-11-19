#import pygal
#import seaborn as sns
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import json
import firebaseInterface as fi
import plotly
import plotly.express as px
#import mpld3

#Seaborn docs: http://seaborn.pydata.org/
#Mpld3 docs: https://mpld3.github.io/modules/API.html
#Matplotlib docs: https://matplotlib.org/3.3.2/index.html



version = '0.0.3'


def makeLineplot(data):
    return "<html> <head> <meta charset=\"utf-8\" /> </head> <body>Hello World</body></html>"


    #df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    # usr_req = {}
    # with open(data) as json_file:
    #   usr_req = json.load(json_file)

    #print(usr_req)

    #Grabbing locations and feature from user json request
    # locations = data['countries']
    # feature = data['feature']

    # #df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
    # fi.fetch_file('test.csv','Cleaned Data/cleaned_data_test.csv') #consider using a url instead of downloading data
    # df = pd.read_csv('test.csv')

    # #make dataframe subset of countries requested
    # df = df[df['location'].isin(locations)]
    # #converting the date column to a datetime type column to allow neater and cleaner visualization
    # df['date'] = pd.to_datetime(df['date'])

    # #make plot with subset of countries
    # #plt.figure(figsize=(15,8))
    # #sns.lineplot(data=df,x='date',y=feature,hue='location')

    # #return an html string of the visualization
    # #return mpld3.fig_to_html(plt.gcf())    


    # # gen plot
    # fig = px.line(df, x="date", y=feature, color="location",
    #           line_group="location") 

    # # Show plot 
    # #fig.show()
    # return plotly.io.to_html(fig, include_plotlyjs=True,full_html=True)
    #return plotly.io.to_html(fig, full_html=True)
    

#  def makeLineplot(data):
#     '''
#         Generates a lineplot with one or more countries for the features specified. 
        
#         Returns an html string containg the figure via the mpld3 library

#     '''
#     #Grabbing locations and feature from user json request
#     locations = data['countries']
#     feature = data['feature']


#     #fetching latest cleaned file from firebase database
#     firebaseInterface.fetch_file('test.csv','Cleaned Data/cleaned_data_test.csv')
#     df = pd.read_csv('test.csv')

#     #make dataframe subset of countries requested
#     df = df[df['location'].isin(locations)]
#     #converting the date column to a datetime type column to allow neater and cleaner visualization
#     df['date'] = pd.to_datetime(df['date'])

#     #make plot with subset of countries
#     plt.figure(figsize=(15,8))
#     sns.lineplot(data=df,x='date',y=feature,hue='location')

#     #return an html string of the visualization
#     return mpld3.fig_to_html(plt.gcf())     

        


def makeBarchart(usr_request):
    '''
        Generates a barplot with one or more countries for the features specified. 
        
        Returns an html string containg the figure via the mpld3 library

    '''
    pass

def makePiechart(usr_request):
    '''
        Generates a piechart with two or more countries for the features specified. 
        
         Returns an html string containg the figure via the mpld3 library

    '''
    pass


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
