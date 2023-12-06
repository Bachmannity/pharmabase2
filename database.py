import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem",
    }
  }
)

def load_table_from_db(query):
  with engine.connect() as conn:
    df = pd.read_sql(query, conn)
    table = df.to_dict('records')
  print(table)
  return table