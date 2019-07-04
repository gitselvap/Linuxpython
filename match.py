#!/usr/bin/env python

import re

output="Interface Gig is DOWN"

b="DOWN"

p = re.compile("DOWN")
m=p.search(output)

if m.group()==b:

         print "Inferface is DOWN"
else:
 
         print "Interface not found"

output2="Interface is UP"

a="UP"

q = re.compile("UP")
n=q.search(output2)

if n.group()==a:

         print "Inferface is UP"
else:

         print "Interface not found"
