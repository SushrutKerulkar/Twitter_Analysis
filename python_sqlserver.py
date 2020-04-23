import pyodbc
import sqlalchemy
import urllib

cxn_str = "DRIVER={ODBC Driver 13 for SQL Server};SERVER=SUSHRUT;DATABASE=airflowdb;Trusted_Connection=yes"
params = urllib.parse.quote_plus(cxn_str)
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
conn = engine.connect().connection
print(conn)
