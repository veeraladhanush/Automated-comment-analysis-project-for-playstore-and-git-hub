#!/usr/bin/env python
# coding: utf-8

# # Module 1 : Pre-processing, Analyzing data using Python and SQL

# ## Task 1 : Pre-processing the data

# In[1]:


# Firstly, we would have to import all the necessary libraries to be utilized

import pandas as pd
import numpy as np
from numpy import nan
from datetime import datetime, timedelta


# In[2]:


#There are two datasets which we would then import using pandas
apps = pd.read_csv("playstore_apps.csv", index_col = 'App')
reviews = pd.read_csv("playstore_reviews.csv")


# In[3]:


#Lets see the column attributes for apps dataset
apps.info()


# In[4]:


# Let's find the no of rows and columns in apps dataset
apps.shape


# In[5]:


# Let's view the first 5 rows of the apps dataset
apps.head()


# In[6]:


apps.duplicated().value_counts()


# ### Subtask 1 : Removing Duplicate Rows
# 
# We have established that 483 columns in the apps dataset contains duplicate rows, while the App column contains 9660 unique columns. we will then attempt to remove those duplicate rows from our apps dataset.

# In[7]:


# Drop duplicate rows in 'App' column
apps = apps.drop_duplicates()


# In[8]:


#Check to make sure duplicates rows were dropped
apps.info()


# ### SubTask 2: Remove Irrelevant values from each column if any
# 
# We would check each column to ascertain attributes that are irrelevant and must be removed from the dataset.
# 
# We would start by checking the unique attributes for each column so as to source for irregularities.

# In[9]:


apps['Category'].unique()


# The `category` column loos okay except the 1.9 attribute as seen above which is not a google playstore category and thus we would attempt to remove the row entry containing the category of '1.9'

# In[10]:


#Check the row that contains the category of 1.9
apps[apps['Category'] == '1.9']


# In[11]:


# only one row (row 10472) contain the category of 1.9 and that row should be removed form our dataset since its not needed.

apps.drop('Life Made WI-Fi Touchscreen Photo Frame', inplace=True)


# In[12]:


# Check to make sure the category of 1.9 was removed.

apps['Category'].unique()


# In[13]:


# Check the distinct attributes of `Rating` column
apps['Rating'].unique()


# The `Rating` column contains missing values. Since the Ratings for each app is a numerical value, these missing values will be replaced with '0' much later in our analysis using Microsoft Excel after our dataset has been exported to csv.

# In[14]:


# Check the distinct attributes of `Content Rating` column
apps['Content Rating'].unique()


# In[15]:


# Check for unique column attributes
apps['Type'].unique()


# #### There is an unwanted `nan` row on the `Type` column which should be removed as it's not needed

# In[16]:


# Let's remove the nan rows in the `Type` column
apps = apps.dropna(subset=['Type'])


# #### Let's confirm that the nan row has been removed from the `Type` column

# In[17]:


apps['Type'].unique()


# ### Next is to check for incorrect datatype in column attributes. The `Last Updated` column has a datatype of object and must be changed to a datatype of datetime to reflect the date attributes in it

# In[18]:


# Change datatype of `Last Updated` column to datetime

apps['Last Updated'] = pd.to_datetime(apps['Last Updated'])


# In[19]:


# Let's check that all changes made are reflected in every column.
apps.info()


# From the above assessment, it can be seen that the `app` dataset still contains missing values in the `Rating` , `Current Ver` and `Andriod Ver` columns which will be addressed in the next stage of our analysis using Microsoft Excel.

# ### Now we can export our `apps` dataset to csv file for further accessment on microsoft Excel

# In[20]:


apps.to_csv('cleaned_apps_v2.csv')


# ## Pre-processing on the `review` dataset

# Lets programmatically view the reviews dataset to get familiar with its properties.

# In[21]:


# Lets see the column attributes for reviews dataset
reviews.info()


# In[22]:


reviews.head(10)


# In[26]:


reviews['Translated_Review'].isna().value_counts()


# We can observed that the `reviews` dataset has 26868 null values in its `Translated_Review` column. Therefore all rows with null values in the `Translated_Review` column will be deleted as there is no translated reviews present and as such that kind of data is of no use for our analysis
#     
# The reviews dataset will be further cleaned on Microsoft Excel for both null values and duplicate values before exporting for analysis.

#     All pre-processing on the reviews dataset would be carried out in Microsoft Excel.
