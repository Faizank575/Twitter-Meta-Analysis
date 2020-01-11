import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium

from Project_4 import aggregate_data,subset_data,plot_data,map_data


#Part 1
sen = pd.read_csv('senators_parsed.csv') #Read in data from file
sen['year'] = sen['created_at'].apply(lambda x: '20' + x.split('/')[2].split(' ')[0]) #Create year column
months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September',
          10:'October', 11:'November', 12:'December'}
sen['month'] = sen['created_at'].apply(lambda x: months.get(int(x.split('/')[0]))) #Create month column
sen.drop(['url', 'bioguide_id', 'created_at'],axis = 1) #Drop 3 columns
sen['user'] = sen['user'].str.upper() #Put usernames in to uppercase
sen_2016 = sen[(sen['year'] == '2016') & (sen['month']=='November')] #New data frame just November 2016


#Part 3 Question 1
UserData=aggregate_data(sen_2016,'user')

#Part 3 Question 2
subset_data(UserData,column = 'retweets', cutoff = 10000)

#Part 3 Question 3
aggregate_data(sen_2016,'party','mean')

#Part 3 Question 4
plot_data(sen_2016,'favorites','party')

#Part 3 Question 5
TotalRepliesByState=aggregate_data(sen_2016[['state','replies']],'state')
map_data(TotalRepliesByState,'replies','us-states.json','feature.id')