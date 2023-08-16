#!/usr/bin/env python
# coding: utf-8

# ![example](images/director_shot.jpeg)

# # Project Title
# 
# **Authors:** Student 1, Student 2, Student 3
# ***

# ## Overview
# 
# A one-paragraph overview of the project, including the business problem, data, methods, results and recommendations.

# ## Business Problem
# 
# Summary of the business problem you are trying to solve, and the data questions that you plan to answer to solve them.
# 
# ***
# Questions to consider:
# * What are the business's pain points related to this project?
# * How did you pick the data analysis question(s) that you did?
# * Why are these questions important from a business perspective?
# ***

# ## Data Understanding
# 
# Describe the data being used for this project.
# ***
# Questions to consider:
# * Where did the data come from, and how do they relate to the data analysis questions?
# * What do the data represent? Who is in the sample and what variables are included?
# * What is the target variable?
# * What are the properties of the variables you intend to use?
# ***

# In[2]:


# Import standard packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# Here you run your code to explore the data
df_movieinfo = pd.read_csv('zippedData/bom.movie_gross.csv.gz')


# In[5]:


df_movieinfo


# In[6]:


df_movie = pd.read_csv('zippedData/tmdb.movies.csv.gz')


# In[7]:


df_movie


# ## Data Preparation
# 
# Describe and justify the process for preparing the data for analysis.
# 
# ***
# Questions to consider:
# * Were there variables you dropped or created?
# * How did you address missing values or outliers?
# * Why are these choices appropriate given the data and the business problem?
# ***

# In[6]:


# Here you run your code to clean the data
dfimdb_rating = pd.read_csv(r'zippedData\imdb.title.ratings.csv.gz')
dfbudget = pd.read_csv(r'zippedData\tn.movie_budgets.csv.gz')


# ## Data Modeling
# Describe and justify the process for analyzing or modeling the data.
# 
# ***
# Questions to consider:
# * How did you analyze or model the data?
# * How did you iterate on your initial approach to make it better?
# * Why are these choices appropriate given the data and the business problem?
# ***

# In[ ]:


# Here you run your code to model the data


# ## Evaluation
# Evaluate how well your work solves the stated business problem.
# 
# ***
# Questions to consider:
# * How do you interpret the results?
# * How well does your model fit your data? How much better is this than your baseline model?
# * How confident are you that your results would generalize beyond the data you have?
# * How confident are you that this model would benefit the business if put into use?
# ***

# ## Conclusions
# Provide your conclusions about the work you've done, including any limitations or next steps.
# 
# ***
# Questions to consider:
# * What would you recommend the business do as a result of this work?
# * What are some reasons why your analysis might not fully solve the business problem?
# * What else could you do in the future to improve this project?
# ***
