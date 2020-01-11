import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium


#Part 2 Question 1
def subset_data(df, column = 'replies', cutoff = 100, above = True):
    #Checking for whether the column exists in the dataframe
    if column in df.columns:
        #conditional expression to minimize the code and write if-else code in one line
        return df[df[column]>cutoff] if above else df[df[column]<=cutoff]

#Part 2 Question 2   
def aggregate_data(df, column, how = 'sum'):
    #Checking for whether the column exists in the dataframe
    if column in df.columns:
        # if else conditions to determine which operation to perfome        
        if how=='sum':
            return df.groupby(column).sum()
        elif how =='mean':
            return df.groupby(column).mean()
        elif how == 'count':
            return df.groupby(column).count()
        else:
            return df.groupby(column).median()

#Part 2 Question 3     
def plot_data(df, col1, col2, rotate_labels = False):
    #Checking whether both columns is subset of all column set 
    if {col1, col2}.issubset(df.columns):
        new_df=aggregate_data(df[[col1,col2]],col2)
        plt.xlabel(col2)
        plt.ylabel(col1)
        if(rotate_labels):
            #Setting rotation to 90 degree based on the value of the rotate_labels            
            plt.xticks(rotation=90)
            return plt.bar(new_df.index,new_df[col1])
        else:
            return plt.bar(new_df.index,new_df[col1])

#Part 2 Question 4
def map_data(df, data_col, json_file, key, cmap='BuPu', filename = 'map.html'):
    #Setting the default map location     
    map = folium.Map(location=[37, -102], zoom_start=5)
    map.choropleth(geo_data=json_file,
                 name='choropleth',
                 data=df,
                 columns=[df.index, data_col],
                 key_on=key,
                fill_color=cmap,
                fill_opacity=0.7,
                line_opacity=0.2)
    folium.LayerControl().add_to(map)
    # Save to html
    map.save(filename)
    return map