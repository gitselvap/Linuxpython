#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
import sys
from termcolor import colored, cprint

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
 


#sql_select_Query = "SELECT * FROM SPECIFICATIONS"
sql_select_Query = "SELECT * FROM SPECIFICATIONS WHERE SUB_TYPE ='ACL'"
cursor = cnx.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
'''for row in records:
    print row[0], " ", row[3]
'''
cursor.execute("SELECT COUNT(*) FROM SPECIFICATIONS WHERE SUB_TYPE ='ACL'")
#print(list(cursor))
res=cursor.fetchone()
#print  "Total count of ACL =", res[0]
cursor.close()
cnx.close()
count=102

if res[0] == count:
	text = colored('Total count of ACL= ', 'green', attrs=['reverse', 'blink'])
        print "\n"
	print(text + str(res[0]))
        print "\n"
        inform1 = colored('Current ACL are placed in your database', 'green', attrs=['reverse', 'blink'])
        print(inform1)
elif res[0] > count:
	text = colored('Total count of ACL= ', 'cyan', attrs=['reverse', 'blink'])
        print "\n"
        print(text + str(res[0]))
        print "\n"
        inform2 = colored('Some more ACL are added in the database... kindly contact developer for more info', 'cyan', attrs=['reverse', 'blink'])
        print(inform2)
elif res[0] < count and  res[0] != 0:
        text = colored('Total count of ACL= ', 'yellow', attrs=['reverse', 'blink'])
        print "\n"
        print(text + str(res[0]))
        print "\n"
        inform3 = colored('Some ACL catalog attributes are missing in the database... kindly re-run the acl script', 'yellow', attrs=['reverse', 'blink'])
        print(inform3)
else:
        text = colored('ACL are  missing in your database', 'red', attrs=['reverse', 'blink'])
        print "\n"
	print(text)
        print "\n"

