#!/usr/bin/env python
from py2neo import Graph, Node, Relationship, Path
import sys

host=(sys.argv[1])
#host="135.250.193.220"
port="7473"

#URL='bolt://135.250.193.220:7687'
URL='https://%s:%s/browser/' % (host, port)
User = "neo4j"
Pass = "admin@123"

graph=Graph(URL, user=User, password=Pass, secure=True)

sy ='MATCH (n:Equipment) RETURN n.SureName limit 5'
#sy='MATCH (n:Path) RETURN n.SureName="GEO51-for-P2P Test" limit 1'

res=graph.run(sy).data()

#print res

def out_fun():
    return res
res = out_fun()
file = open("sample.txt","w")
file.write(str(res))
file.close()





