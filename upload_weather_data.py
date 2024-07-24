import pandas as pd
from sqlalchemy import create_engine,text
from pangres import upsert
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_env.settings')
django.setup()



# Assuming your Django settings are configured for database access
DATABASES = settings.DATABASES['default']
username = DATABASES['USER']
password = DATABASES['PASSWORD']
host = DATABASES['HOST']
port = DATABASES.get('PORT', '3306')  # Default MySQL port is 3306
database_name = DATABASES['NAME']

# Construct the correct SQLAlchemy URL
database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"
# Create SQLAlchemy engine
engine = create_engine(database_url)

# Load the CSV file into a DataFrame

df = pd.read_csv('location.csv')

# Convert timestamp column to datetime if not already in the correct format
# df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])
df.reset_index(drop=True, inplace=True)
df.index.rename('index_name', inplace=True)

# print(df.index.names)


# Use pangres to upsert the DataFrame into the database
# The table name is assumed to be the lowercase model name, which is Django's default behavior
# Insert DataFrame into SQL table
# df.to_sql(name='weather_app_weatherdata', con=engine, if_exists='append', index=False)
# upsert(con=engine, df=df, table_name='weather_app_weatherdata', if_row_exists='update')
# Connect to the database
engine.connect().execute(text("drop table IF EXISTS adaniq1.location"))

engine.connect().execute(text("CREATE table IF NOT EXISTS adaniq1.location (location VARCHAR(100))"))
    # for index, row in df.iterrows():
        # Construct the INSERT query with parameter placeholders
        # print(row['location'])
        # query = "INSERT INTO weather_data_location(id,location) VALUES ("+ str(id)+",'"+ row['location']+"')"
        # query = "INSERT INTO location VALUES ('"+row['location']+"')"

from sqlalchemy.sql import text

# Assuming 'engine' is already defined and connected to your database
with engine.connect() as connection:
    # Begin a transaction
    trans = connection.begin()
    try:
        for index, row in df.iterrows():
            # Construct the INSERT query with parameter placeholders
            query = "INSERT INTO adaniq1.location VALUES ('"+row['location']+"')"
            connection.execute(text(query))

        # Your existing INSERT operation
        # query = "INSERT INTO adaniq1.location VALUES ('a')"
        # connection.execute(text(query))
        
        # Check if the data was inserted
        check_query = "SELECT * FROM adaniq1.location"
        result = connection.execute(text(check_query))
        data = result.fetchone()
        
        if data:
            print('Data uploaded successfully')
            print(data)
            # Commit the transaction if data inserted
            trans.commit()
        else:
            print('Data insertion failed')
            # Rollback in case of failure (this is optional here since if no data is found, it means no insertion happened)
            trans.rollback()
    except Exception as e:
        # Rollback the transaction in case of an error
        trans.rollback()
        print(f"An error occurred: {e}")




# Use pangres to upsert the DataFrame into the database
# The table name is assumed to be the lowercase model name, which is Django's default behavior
# Insert DataFrame into SQL table
# df.to_sql(name='weather_app_weatherdata', con=engine, if_exists='append', index=False)
# upsert(con=engine, df=df, table_name='weather_app_weatherdata', if_row_exists='update')