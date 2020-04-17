#script to insert data into employee table
#importing sqlite3
import sqlite3 as sql
conn = sql.connect("database1.db")
curs = conn.cursor()
try:
    curs.execute( "insert into employee values(501, 'John',154000.22 )" )
    conn.commit()
    print( "data is inserted" )
except sql.IntegrityError:
    print( "IDno is available" )
finally:
    conn.close()
print( "thanks" )