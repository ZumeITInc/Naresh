# script to create a table
# importing sqlite3 database 
import sqlite3 as sql
conn = sql.connect( "database1.db" )
#read and write the content
curs = conn.cursor()
try:
    curs.execute( "create table employee(idno number,name text,salary real )" )
    print( "table is created" )
#exception if table is available
except sql.OperationalError as oe:
    print(oe)

finally:
    conn.close()
print( "thanks" )
