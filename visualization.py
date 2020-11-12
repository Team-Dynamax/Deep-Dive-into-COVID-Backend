#import pygal
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import firebaseInterface

#Pygal DOCS: http://www.pygal.org/en/stable/documentation/


version = '0.0.1'

def makeLineplot(usr_request):
    '''
        Generates a lineplot with one or more countries for the features specified. 
        If request contains a valid date interval
        the plot should be generated only for that interval. 
        
        Returns a json file containg the svg image as a base64 encoded string

    '''
    with open(usr_request) as json_file:
        data = json.load(json_file)

        locations = data['countries']
        feature = data['feature']

        #Get the data from firebase
        #generate the seaborn plot
        #upload back to firebase
        #return the image
        #print(data)
        firebaseInterface.fetch_file('test.csv','Cleaned Data/cleaned_data_test.csv')
        df = pd.read_csv('test.csv')
        #make dataframe subset of countries
        df = df[df['location'].isin(locations)]

        #make plot with subset of countries

        plt.figure(figsize=(15,8))
        sns.lineplot(data=df,x='date',y=feature,hue='location')
        plt.gcf().autofmt_xdate()
        plt.show()


        


def makeBarchart(usr_request):
    '''
        Generates a barplot with one or more countries for the features specified. 
        If request contains a valid date interval
        the plot should be generated only for that interval. 
        
        Returns a json file containg the svg image as a base64 encoded string

    '''
    pass

def makePiechart(usr_request):
    '''
        Generates a piechart with two or more countries for the features specified. 
        If request contains a valid date interval
        the plot should be generated only for that interval. 
        
        Returns a json file containg the svg image as a base64 encoded string

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
makeLineplot('test.json')