
import pandas as pd
import numpy as np
import env
import os



#preliminary clean delco:
def prep_telco(df):

    df = df.drop_duplicates()  #Drop duplicates
    
    #11 values are blank strings for total charges representing 11 customers at 0 tenure
    df['total_charges'] = df['total_charges'].str.strip() #eliminate white space
    df['total_charges'] = df['total_charges'].replace('', 0) #replace empty values as 0
    df['total_charges'] = df['total_charges'].astype('float64')

    #15 columns encoded to '0' = No, '1'= Yes
    #contract type MtM = 0, 1year = 1, 2year =2
    #concated manual billing = 0 , automatic billing = 1
    df['gender'] = df.gender.replace({'Female': 0, 'Male': 1})
    df['partner'] = df.partner.replace({'Yes': 1, 'No': 0})
    df['dependents'] = df.dependents.replace({'Yes': 1, 'No': 0})
    df['phone_service'] = df.phone_service.replace({'Yes': 1, 'No': 0})
    df['churn'] = df.churn.replace({'Yes': 1, 'No': 0})
    df['multiple_lines'] = df.multiple_lines.replace({'No': 0, "Yes": 1, "No phone service": 0})
    df['online_secuirty'] = df.online_security.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['online_backup'] = df.online_backup.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['device_protection'] = df.device_protection.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['tech_support'] = df.tech_support.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['streaming_tv'] = df.streaming_tv.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['streaming_movies'] = df.streaming_movies.replace({'No': 0, "Yes": 1, "No internet service": 0})
    df['paperless_billing'] = df.paperless_billing.replace({'Yes': 1, 'No': 0})
    #df['contract_type'] = df.contract_type.replace({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    df['payment_type'] = df.payment_type.replace({'Mailed check': 0, 'Credit card (automatic)': 1, 
                                               'Bank transfer (automatic)': 1,  'Electronic check': 0})


    # creating dummy values for payment, internet, & contract (*important values*)
    dummy_df = pd.get_dummies(df[['payment_type',"internet_service_type","contract_type"]])
    df = pd.concat([df, dummy_df], axis=1)


    columns_to_rename = {'contract_type': 'contract',
                   'internet_service_type': 'internet'} # Renaming columns
    df = df.rename(columns=columns_to_rename) 
    
    return df