from psycopg2 import connect

conn = connect(dbname="tbd1", user="avsco", password="123456")

def getConnection():
    return conn
