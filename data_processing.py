
import pandas as pd
import numpy as np
import pyodbc

def collect_and_process_data():
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=server_name;DATABASE=database_name;UID=user;PWD=12345')

    query = "SELECT * PTF_CLIENT"
    data = pd.read_sql(query, conn)

    data_cleaned = data.dropna()  

    data_transformed = data_cleaned.apply(lambda x: x * 1.1)  
  
    data_transformed.to_csv('data/NEW_data.csv', index=False)

    print("Données collectées et transformées avec succès.")
