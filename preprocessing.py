version = "0.0.0" #version of module


import pandas as pd
import numpy as np

def getCountryData(country, data):
  """
  Return a pandas Dataframe that contains a subset of the data respect to the parameter country.
  Args: 
      country - A string contain the Name of the country. See Docs for list of country.   
      data - A pandas Dataframe form OWID.
  """
  return data.loc[data["location"] == country]
  


def preprocessData(data, heading):
  """
  Return a pandas Dataframe that containing preprocessed data
  Args: 
      data - A pandas Dataframe form OWID.
  """
  tmp_df = data[heading].fillna(0)
  tmp_df[heading].fillna( inplace = True, method = 'ffill')
  return tmp_df

def storeCountryInCsv(data, country):
  data.to_csv("{}_Data.csv".format(country))


def getVersion();
    """
        Returns the version of the python module
    """
    print("Version: {}".format(version))
