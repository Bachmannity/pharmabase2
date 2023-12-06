import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import os

db_connection_string = "mysql+pymysql://9cweyz5agb1iua6z88uv:pscale_pw_KQYpIdeVoxwDnXyPvYQTL1usXK3P3SMVYB2p7d7sELZ@aws.connect.psdb.cloud/htainsights?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_gba_dict_list_from_db(query):
  with engine.connect() as conn:
    df = pd.read_sql(query, conn)
    dict_list = df.to_dict('records')
  return dict_list


def load_assessment_dict_from_db(id):
  with engine.connect() as conn:
    query = "SELECT * FROM gba WHERE id = " + str(id)
    df = pd.read_sql(query, conn)
    dict_list = df.to_dict('records')
    if len(dict_list) == 0:
      return None
    else:
      return dict_list[0]
