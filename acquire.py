#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import env
import os


# ## Telco Churn Data Acquire
# 
# #### Connection information from mySQL

# In[23]:


def get_connection(db, user=env.user, host=env.host, password=env.password):
    connection_info = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return connection_info


# In[ ]:





# In[24]:


def new_telco_data():
    '''
    This function reads the iris data from the Codeup db into a df.
    '''
    sql_query = """
                SELECT *
                FROM customers
                JOIN internet_service_types USING (internet_service_type_id)
                JOIN contract_types USING (contract_type_id)
                JOIN payment_types USING (payment_type_id)
                ;
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df


# In[25]:


def get_telco_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df


# In[26]:


import os
telco_data = get_telco_data()
telco_data


# In[ ]:




