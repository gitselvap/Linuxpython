#!/usr/bin/env python

import requests
import sys

host=(sys.argv[1])
#host="135.250.193.220"
port="28443"

URL="https://%s:%s/oss/sure/equipments" %(host, port)

#print URL

headers = {'content-type': 'application/xml', 'Accept': 'application/json', 'appId': 'SURE_APP', 'tenantId':'T0', 'ugId':'Admin_UserGroup', 'Authorization':'Basic YWRtaW46YWRtaW5AMTIz'}

payload='/root/python/payload/postequipment.xml'

res=requests.post(url=URL, headers=headers, data=open(payload), verify=False) 

#print (res.json)

output=(res.status_code)

#print output

if output  == 201:
   print ("\nData Successfully Created "+ u'\u2714'+ u'\u2714'+ u'\u2714'+ "\n");
elif output == 400:
   print "\n400 Bad Request\n"
elif output == 401:
   print "\n401 Unauthorized\n"
elif output == 404:
   print "\n404 Not Found\n"
elif output == 500:
   print ("\n500 Internal Server Error "+ u'\u2716'+ u'\u2716'+u'\u2716'+ "\n");
elif output == 502:
   print "\n502 Bad Gateway.........\n"
elif output == 503:
   print "\n503 Service Unavailable.......\n"
else:
     print "Status =".format(output)
     

