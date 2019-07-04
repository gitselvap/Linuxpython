#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
import sys

local=(sys.argv[1])
#print local
try:
   cnx = mysql.connector.connect(user='METADATA', port=3306, password='METADATA',
                                host=local, database='METADATA')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("Database is connected!")
  print ("\n") 


#sql_select_Query = "SELECT * FROM SPECIFICATIONS"
sql_select_Query = "SELECT * FROM SPECIFICATIONS WHERE SUB_TYPE ='ACL'"
cursor = cnx.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for row in records:
    print row[0], " ", row[3]
cursor.execute("SELECT COUNT(*) FROM SPECIFICATIONS WHERE SUB_TYPE ='ACL'")
print(list(cursor))
cursor.close()
cnx.close()
