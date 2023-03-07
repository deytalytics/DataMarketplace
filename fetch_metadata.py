from connect_to_db import create_connection
from sqlalchemy import text
import json, pandas as pd

def fetch_metadata(query):
    #Connect to the metadata database
    conn = create_connection('data_product_metadata')

    #Read the query result into a dataframe
    df = pd.read_sql(text(query), conn)

    # Close the database connection
    conn.close()

    # Convert dataframe to a dictionary
    metadata_dict = df.to_dict(orient='records')

    #return the metadata as a dictionary
    return metadata_dict

