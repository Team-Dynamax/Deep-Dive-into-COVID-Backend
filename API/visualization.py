#import pygal
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import firebaseInterface
import mpld3

#Seaborn docs: http://seaborn.pydata.org/
#Mpld3 docs: https://mpld3.github.io/modules/API.html
#Matplotlib docs: https://matplotlib.org/3.3.2/index.html



version = '0.0.2'

def makeLineplot(data):
    '''
        Generates a lineplot with one or more countries for the features specified. 
        
        Returns an html string containg the figure via the mpld3 library

    '''
    #Grabbing locations and feature from user json request
    locations = data['countries']
    feature = data['feature']


    #fetching latest cleaned file from firebase database
    firebaseInterface.fetch_file('test.csv','Cleaned Data/cleaned_data_test.csv')
    df = pd.read_csv('test.csv')

    #make dataframe subset of countries requested
    df = df[df['location'].isin(locations)]
    #converting the date column to a datetime type column to allow neater and cleaner visualization
    df['date'] = pd.to_datetime(df['date'])

    #make plot with subset of countries
    plt.figure(figsize=(15,8))
    sns.lineplot(data=df,x='date',y=feature,hue='location')

    #return an html string of the visualization
    return mpld3.fig_to_html(plt.gcf())     

        


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
#makeLineplot('test.json')