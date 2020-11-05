import pygal

#Pygal DOCS: http://www.pygal.org/en/stable/documentation/


version = '0.0.0'

def makeLineplot(usr_request):
    '''
        Generates a lineplot with one or more countries for the features specified. 
        If request contains a valid date interval
        the plot should be generated only for that interval. 
        
        Returns a json file containg the svg image as a base64 encoded string

    '''
    pass


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