import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mpld3


df = pd.read_csv('test.csv')
#make dataframe subset of countries
df = df[df['location'].isin(['Brazil','China'])]
feature = 'new_cases'

df['date'] = pd.to_datetime(df['date'])

#make plot with subset of countries
plt.figure(figsize=(15,8))
viz = sns.lineplot(data=df,x='date',y=feature,hue='location')
html_text = mpld3.fig_to_html(plt.gcf())
Html_file= open("index.html","w")
Html_file.write(html_text)
Html_file.close()


