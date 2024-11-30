#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:





# In[ ]:





# In[ ]:


import os

# Get the current working directory
current_directory = os.getcwd()


# In[2]:


#Breakfast = 4:00 AM - 11:59 AM, Lunch = 12:00 PM to 16:30 PM, Dinner = 16:31 PM - 23:59 PM, Late-Night: 00:00 AM to 3:59 AM 
import pandas as pd

def count_meal_time(mt):
    breakfast = 0
    lunch = 0 
    dinner = 0 
    late_night = 0
    
    for i in mt: 
        meal_time_hr = (int(i[11:13]) - 4)
        meal_time_min = (int(i[14:16]))
        

        if meal_time_hr < 0:
            meal_time_hr = 24 + meal_time_hr
            
        meal_time = ((meal_time_hr)*60) + (meal_time_min)
        
        if meal_time >= 240 and meal_time <= 719:
            breakfast += 1
        elif meal_time >= 720 and meal_time <= 990:
            lunch += 1
        elif meal_time >= 991 and meal_time <= 1429:
            dinner += 1
        elif meal_time >= 0 and meal_time <= 239: 
            late_night += 1
        
    meal_count = pd.DataFrame({
        'meal': ['Breakfast', 'Lunch', 'Dinner', 'Late_Night'],
        'Number': [breakfast, lunch, dinner, late_night]
    })
    
    return meal_count
        


# In[3]:


import pandas as pd 
def meal_time_avg(time):
    array = []
    for i in time: 
        meal_time_hr = (int(i[11:13]) - 4)
        if meal_time_hr < 0:
            meal_time_hr = 24 + meal_time_hr
        array.append(meal_time_hr)
    count = pd.DataFrame({
        'Number': array
    })
    return count


# In[4]:


import pandas as pd
import pytz

df = pd.read_csv('C:/Users/My PC/GI_Tract/meals_data.csv')
df['meal_time (UTC)'] = pd.to_datetime(df['meal_time (UTC)'], utc =True)

# Define timezones
est = pytz.timezone('America/New_York')

# Convert UTC time to EST
df['meal_time_est'] = df['meal_time (UTC)'].dt.tz_convert(est)  # Convert to EST
# Assuming 'meal_time' is a column in your DataFrame with datetime strings
df['meal_time_est'] = pd.to_datetime(df['meal_time_est'])  # Convert the column to datetime


# If you want to have the name of the day instead of a number (e.g., Monday, Tuesday, etc.)
df['day_name'] = df['meal_time_est'].dt.day_name()

#homemade or not at a specific day of the week
def homemade(df):
    df['meal_time (UTC)'] = pd.to_datetime(df['meal_time (UTC)'], utc =True)

    # Define timezones
    est = pytz.timezone('America/New_York')

    # Convert UTC time to EST
    df['meal_time_est'] = df['meal_time (UTC)'].dt.tz_convert(est)  # Convert to EST
    # Assuming 'meal_time' is a column in your DataFrame with datetime strings
    df['meal_time_est'] = pd.to_datetime(df['meal_time_est'])  # Convert the column to datetime

    
    # If you want to have the name of the day instead of a number (e.g., Monday, Tuesday, etc.)
    df['day_name'] = df['meal_time_est'].dt.day_name()
    
    M_Y, TU_Y, W_Y, T_Y, F_Y, SAT_Y, S_Y = 0,0,0,0,0,0,0
    M_N,TU_N, W_N, T_N, F_N, SAT_N, S_N = 0,0,0,0,0,0,0
    
    for index, row in df.iterrows():
        if row['is_home_made'] == True:  # Access the actual value of 'is_home_made'
            if row['day_name'] == 'Monday':  # Access the actual value of 'day_name'
                M_Y += 1
            elif row['day_name'] == 'Tuesday':
                TU_Y += 1
            elif row['day_name'] == 'Wednesday':
                W_Y += 1
            elif row['day_name'] == 'Thursday':
                T_Y += 1
            elif row['day_name'] == 'Friday':
                F_Y += 1
            elif row['day_name'] == 'Saturday':
                SAT_Y += 1
            elif row['day_name'] == 'Sunday':
                S_Y += 1
        else:
            if row['day_name'] == 'Monday':
                M_N += 1
            elif row['day_name'] == 'Tuesday':
                TU_N += 1
            elif row['day_name'] == 'Wednesday':
                W_N += 1
            elif row['day_name'] == 'Thursday':
                T_N += 1
            elif row['day_name'] == 'Friday':
                F_N += 1
            elif row['day_name'] == 'Saturday':
                SAT_N += 1
            elif row['day_name'] == 'Sunday':
                S_N += 1
        
                
        
    days_count = pd.DataFrame({
        'Days': ['Monday', 'Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Home': [M_Y, TU_Y, W_Y, T_Y, F_Y, SAT_Y, S_Y],
        'NOT_HOME': [M_N,TU_N, W_N, T_N, F_N, SAT_N, S_N]
    })
    
    return days_count


#healthy or not at a specific day of the week
def healthy(df):
    df['meal_time (UTC)'] = pd.to_datetime(df['meal_time (UTC)'], utc =True)

    # Define timezones
    est = pytz.timezone('America/New_York')

    # Convert UTC time to EST
    df['meal_time_est'] = df['meal_time (UTC)'].dt.tz_convert(est)  # Convert to EST
    # Assuming 'meal_time' is a column in your DataFrame with datetime strings
    df['meal_time_est'] = pd.to_datetime(df['meal_time_est'])  # Convert the column to datetime

    
    # If you want to have the name of the day instead of a number (e.g., Monday, Tuesday, etc.)
    df['day_name'] = df['meal_time_est'].dt.day_name()
    
    M_Y, TU_Y, W_Y, T_Y, F_Y, SAT_Y, S_Y = 0,0,0,0,0,0,0
    M_N,TU_N, W_N, T_N, F_N, SAT_N, S_N = 0,0,0,0,0,0,0
    
    for index, row in df.iterrows():
        if row['predicted_category_2'] == 'Healthy Food':  # Access the actual value of 'is_home_made'
            if row['day_name'] == 'Monday':  # Access the actual value of 'day_name' 
                M_Y += 1
            elif row['day_name'] == 'Tuesday':
                TU_Y += 1
            elif row['day_name'] == 'Wednesday':
                W_Y += 1
            elif row['day_name'] == 'Thursday':
                T_Y += 1
            elif row['day_name'] == 'Friday':
                F_Y += 1
            elif row['day_name'] == 'Saturday':
                SAT_Y += 1
            elif row['day_name'] == 'Sunday':
                S_Y += 1
        elif row['predicted_category_2'] == 'Unhealthy food':
            if row['day_name'] == 'Monday':
                M_N += 1
            elif row['day_name'] == 'Tuesday':
                TU_N += 1
            elif row['day_name'] == 'Wednesday':
                W_N += 1
            elif row['day_name'] == 'Thursday':
                T_N += 1
            elif row['day_name'] == 'Friday':
                F_N += 1
            elif row['day_name'] == 'Saturday':
                SAT_N += 1
            elif row['day_name'] == 'Sunday':
                S_N += 1
        else: 
            continue
        
                
        
    days_count = pd.DataFrame({
        'Days': ['Monday', 'Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Healthy': [M_Y, TU_Y, W_Y, T_Y, F_Y, SAT_Y, S_Y],
        'Unhealthy': [M_N,TU_N, W_N, T_N, F_N, SAT_N, S_N]
    })
    
    return days_count


# In[5]:



import pandas as pd

import math

# Incorporate data

def md(tt):
    array = []
    for i in tt: 
        if i is None or (isinstance(i, float) and math.isnan(i)):
            continue
        index_start = 0 
        index_end = 0
        for j in i:
            index_end += 1
            if j == " " or j ==',' or j == " " and j == "  ": 
                k = i[index_start:index_end - 1]
                if k == 'on' or k == None or k == '1' or k == 'from' or k == '2' or k == 'small' or k == 'hot' or k == 'ground' or k =='of' or k == 'a' or k == '3' or k =='mixed' or k == 'half' or k == 'kale': 
                    continue
                elif k == 'egg' or k == 'eggs' or k == 'eggs,': 
                    k = 'egg'
                elif k == 'rice' or k == 'rice,':
                    k == 'rice'
                array.append(k)
                index_start = index_end 
                
    DF = pd.DataFrame({
        'Number': array
    })
    
    return DF


# In[6]:


from dash import Dash, dcc, html, dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Incorporate data
df = pd.read_csv('C:/Users/My PC/GI_Tract/meals_data.csv')

# Create a DataFrame to count meal logs for each author_uid
counting_df = df['author_uid'].value_counts().reset_index()
counting_df.columns = ['ID', 'Number']  # Rename columns for clarity

# Convert the counting DataFrame to a dictionary format for Dash
data_dict = counting_df.to_dict('records')

counting_df_2 = df['is_home_made'].value_counts().reset_index()
counting_df_2.columns = ['Type', 'Number of meals']  # Rename columns for clarity 

data_dict_2 = counting_df_2.to_dict('records')


df_3 = df['meal_time (UTC)']
meal_count = count_meal_time(df_3)

fig = px.pie(meal_count, names='meal', values='Number', title='Meal Logs per Time')


counting_df_4 = meal_time_avg(df_3)['Number'].value_counts().reset_index()
counting_df_4.columns = ['Time (hours)', 'Number of meals']

data_dict_4 = counting_df_4.to_dict('records')

df_5 = meal_time_avg(df_3)
fig_2 = px.box(df_5, x='Number', title='Meal Times Distribution by Meal Type')


# Convert 'meal_time' to datetime to work with dates
df['meal_time (UTC)'] = pd.to_datetime(df['meal_time (UTC)'], errors='coerce')

# Extract the date (ignore time) from 'meal_time' to count unique days
df['meal_date'] = df['meal_time (UTC)'].dt.date

# Calculate total meals and unique days for each user
meal_counts = df.groupby('author_uid').size().reset_index(name='total_meals')
unique_days = df.groupby('author_uid')['meal_date'].nunique().reset_index(name='unique_days')

# Merge the two DataFrames
df_user_stats = pd.merge(meal_counts, unique_days, on='author_uid')

# Calculate the average number of meals per day
df_user_stats['avg_meals_per_day'] = df_user_stats['total_meals'] / df_user_stats['unique_days']

fig_3 = px.scatter(df_user_stats, x='author_uid', y='avg_meals_per_day', title='Average Number of Meals per Day for each User',
                   labels={'author_uid': 'USER ID', 'avg_meals_per_day': 'Average Meals per Day'})


df_6 = homemade(df)
fig_4 = go.Figure()

# Add first line
fig_4.add_trace(go.Scatter(x=df_6['Days'], y=df_6['Home'], mode='lines+markers', name='Home'))

# Add second line
fig_4.add_trace(go.Scatter(x=df_6['Days'], y=df_6['NOT_HOME'], mode='lines+markers', name='NOT_HOME'))

fig_4.add_trace(go.Scatter(x=df_6['Days'], y=df_6['NOT_HOME']+df_6['Home'], mode='lines+markers', name='Total'))

# Update layout
fig_4.update_layout(title='Time Series Plot displaying how number of homemade meals vary over the week',
                  xaxis_title='Day',
                  yaxis_title='Number of meals')


df['meal_time (UTC)'] = pd.to_datetime(df['meal_time (UTC)'], utc=True)

# Sort data by user and log time
df = df.sort_values(by=['author_uid', 'meal_time (UTC)'])

# Calculate the first log date for each user
df['first_log_date'] = df.groupby('author_uid')['meal_time (UTC)'].transform('min')

# Calculate the number of days since the user's first log
df['days_since_first_log'] = (df['meal_time (UTC)'] - df['first_log_date']).dt.days 

# Group by 'author_uid' and 'days_since_first_log' to count the number of logs per user per day
logs_per_day = df.groupby(['author_uid', 'days_since_first_log']).size().reset_index(name='log_count')

# Now group by 'days_since_first_log' to calculate the average logs per user for each nth day
average_logs = logs_per_day.groupby('days_since_first_log').agg(
    total_logs=('log_count', 'sum'),
    user_count=('author_uid', 'nunique')  # Count unique users per nth day
).reset_index()



# Calculate the average number of logs per user
average_logs['avg_logs_per_user'] = average_logs['total_logs'] / average_logs['user_count']

filtered_logs = average_logs[average_logs['days_since_first_log'] <= 36]

fig_5 = px.line(filtered_logs, x='days_since_first_log', y='avg_logs_per_user',
              title='Average Number of Meal Logs for all Users Over Their Time with the App',
              labels={'days_since_first_log': 'Days Since First Log', 'avg_logs_per_user': 'Avg Logs Per User'})


df_7 = md(df['meal_description'])

counting_df_7 = df_7['Number'].value_counts().reset_index()
counting_df_7_sliced = counting_df_7.iloc[4:60]
counting_df_7_sliced.columns = ['Food', 'Number']  # Rename columns for clarity
data_dict_7 = counting_df_7_sliced.to_dict('records')


counting_df_8 = df['predicted_category'].value_counts().reset_index()
counting_df_8.columns = ['Cuisine', 'Number of meals']  # Rename columns for clarity 

data_dict_8 = counting_df_8.to_dict('records')

counting_df_9 = df['predicted_category_2'].value_counts().reset_index()
counting_df_9.columns = ['Type', 'Number of meals']  # Rename columns for clarity 
fig_9 = px.pie(counting_df_9, names='Type', values='Number of meals', title='Meals Healthy or not?')

data_dict_9 = counting_df_9.to_dict('records')

counting_df_10 = df['predicted_category_3'].value_counts().reset_index()
counting_df_10.columns = ['Type', 'Number of meals']  # Rename columns for clarity 
fig_10 = px.pie(counting_df_10, names='Type', values='Number of meals', title='Meals Organic or not?')

data_dict_10 = counting_df_10.to_dict('records') 

counting_df_11 = df['predicted_category_4'].value_counts().reset_index()
counting_df_11.columns = ['Taste', 'Number of meals']  # Rename columns for clarity 

data_dict_11 = counting_df_11.to_dict('records') 

counting_df_12 = df['predicted_category_5'].value_counts().reset_index()
counting_df_12.columns = ['Nutrients', 'Number of meals']  # Rename columns for clarity 

data_dict_12 = counting_df_12.to_dict('records') 

counting_df_13 = df['predicted_category_6'].value_counts().reset_index()
counting_df_13.columns = ['Nutrients', 'Number of meals']  # Rename columns for clarity 

data_dict_13 = counting_df_13.to_dict('records') 

counting_df_14 = df['predicted_category_7'].value_counts().reset_index()
counting_df_14.columns = ['Food Category', 'Number of meals']  # Rename columns for clarity 

data_dict_14 = counting_df_14.to_dict('records')

counting_df_15 = df['predicted_category_8'].value_counts().reset_index()
counting_df_15.columns = ['Cooking Style', 'Number of meals']  # Rename columns for clarity 
fig_15 = px.pie(counting_df_15, names='Cooking Style', values='Number of meals', title='How are the meals cooked?')

data_dict_15 = counting_df_15.to_dict('records')

df_16 = healthy(df) 
fig_16 = go.Figure()

# Add first line
fig_16.add_trace(go.Scatter(x=df_16['Days'], y=df_16['Healthy'], mode='lines+markers', name='Healthy Food'))

# Add second line
fig_16.add_trace(go.Scatter(x=df_16['Days'], y=df_16['Unhealthy'], mode='lines+markers', name='Unhealthy Food'))

df_17 = df.groupby(['author_uid', 'predicted_category_4']).size().reset_index(name='count')

df_17_most_com = df_17.loc[df_17.groupby('author_uid')['count'].idxmax()]
df_17_most_com.columns = ['ID', 'Taste', 'count']  # Rename columns for clarity
data_dict_17 = df_17_most_com.to_dict('records')

df_18 = df.groupby(['author_uid', 'predicted_category_5']).size().reset_index(name='count')

df_18_most_com = df_18.loc[df_18.groupby('author_uid')['count'].idxmax()]
df_18_most_com.columns = ['ID', 'Nutrient', 'count']  # Rename columns for clarity
data_dict_18 = df_18_most_com.to_dict('records') 

df_19 = df.groupby(['author_uid', 'predicted_category_6']).size().reset_index(name='count')

df_19_most_com = df_19.loc[df_19.groupby('author_uid')['count'].idxmax()]
df_19_most_com.columns = ['ID', 'Nutrient', 'count']  # Rename columns for clarity
data_dict_19 = df_19_most_com.to_dict('records') 

df_19 = df.groupby(['author_uid', 'predicted_category_6']).size().reset_index(name='count')

df_19_most_com = df_19.loc[df_19.groupby('author_uid')['count'].idxmax()]
df_19_most_com.columns = ['ID', 'Nutrient', 'count']  # Rename columns for clarity
data_dict_19 = df_19_most_com.to_dict('records') 


df_20 = df.groupby(['author_uid', 'predicted_category_7']).size().reset_index(name='count')

df_20_most_com = df_20.loc[df_20.groupby('author_uid')['count'].idxmax()]
df_20_most_com.columns = ['ID', 'Ingredient', 'count']  # Rename columns for clarity
data_dict_20 = df_20_most_com.to_dict('records') 

df_21 = df.groupby(['author_uid', 'predicted_category_8']).size().reset_index(name='count')

df_21_most_com = df_21.loc[df_21.groupby('author_uid')['count'].idxmax()]
df_21_most_com.columns = ['ID', 'Type', 'count']  # Rename columns for clarity
data_dict_21 = df_21_most_com.to_dict('records') 









# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Number Of Logs per user'),
    dash_table.DataTable(data=data_dict, page_size=10),
    html.Div(children='How many meals are homemade?'),
    dash_table.DataTable(data=data_dict_2, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_2, x='Type', y='Number of meals')),
    
    html.H1(children='Meal Logs Pie Chart'),
    
    # Display the table with counts
    dash_table.DataTable(data=meal_count.to_dict('records'), page_size=10),
    
    # Display the pie chart
    dcc.Graph(id='example-pie-chart', figure=fig),
    
    html.Div(children='Number of meals at a certain hour of the day'),
    dash_table.DataTable(data=data_dict_4, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_4, x='Time (hours)', nbins = 12, y='Number of meals')),
    
    html.Div([
    html.H1(children='Meal Times Box Plot'),
    dcc.Graph(figure=fig_2)
    ]),
    
    html.Div(children=[
    html.H1(children='How does homemade meals change over the week?'),
    dcc.Graph(
        id='time-series-plot',
        figure=fig_4
    )
    ]),
    
    html.Div([
    html.H1("Average Logs for all Users Over Time"),
    dcc.Graph(id='line-chart', figure=fig_5)
    ]),
    
    html.Div([
    html.H1(children='Average Meals/day scatter plot'),
    dcc.Graph(figure=fig_3)
    ]),
    
    html.Div(children='Most Repeated Words in Meal Descriptions'),
    dash_table.DataTable(data=data_dict_7, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_7_sliced, x='Food', y='Number')),
    
    html.Div(children='Which cuisines do meals belong to? (Used facebook/bart-large-mnli to categorize meal descriptions)'),
    dash_table.DataTable(data=data_dict_8, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_8, x='Cuisine', y='Number of meals')),
    
    html.H1(children='Healthy/Unhealthy Pie Chart'),
    dash_table.DataTable(data=data_dict_9, page_size=10),
    dcc.Graph(id='example-pie-chart', figure=fig_9),
    
    html.H1(children='Organic/Inorganic Pie Chart'),
    dash_table.DataTable(data=data_dict_10, page_size=10),
    dcc.Graph(id='example-pie-chart', figure=fig_10),
    
    html.Div(children='Which taste do most meals have?'),
    dash_table.DataTable(data=data_dict_11, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_11, x='Taste', y='Number of meals')),
    
    html.Div(children='Which nutrient are the meals high in?'),
    dash_table.DataTable(data=data_dict_12, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_12, x='Nutrients', y='Number of meals')),
    
    html.Div(children='Which nutrient are the meals low in?'),
    dash_table.DataTable(data=data_dict_13, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_13, x='Nutrients', y='Number of meals')),
    
    html.Div(children='What do most users eat?'),
    dash_table.DataTable(data=data_dict_14, page_size=4),
    dcc.Graph(figure=px.histogram(counting_df_14, x='Food Category', y='Number of meals')),
    
    html.H1(children='How do the users prefer the meals to be cooked?'),
    dash_table.DataTable(data=data_dict_15, page_size=10),
    dcc.Graph(id='example-pie-chart', figure=fig_15),
    
    html.Div(children=[
    html.H1(children='How does eating healthy/unhealthy change over the week?'),
    dcc.Graph(
        id='time-series-plot',
        figure=fig_16
    )
    ]),
    
    html.Div(children='Which taste does each user prefer?'),
    dash_table.DataTable(data=data_dict_17, page_size=10), 
    
    html.Div(children='Which Nutrient does each user take in high amounts?'),
    dash_table.DataTable(data=data_dict_18, page_size=10), 
    
    html.Div(children='Which Nutrient does each user take in low amounts?'),
    dash_table.DataTable(data=data_dict_19, page_size=10), 
    
    html.Div(children='Which ingredient does each user take in the most?'),
    dash_table.DataTable(data=data_dict_20, page_size=10), 
    
    html.Div(children='How does each user prefer to eat/cook their food?'),
    dash_table.DataTable(data=data_dict_21, page_size=10), 
    
    
    
    #fig_3.show()

]





# Run the app
if __name__ == '__main__':
    app.run_server()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




