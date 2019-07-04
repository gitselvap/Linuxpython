#!/usr/bin/env python

import re

output="/root/python/inter.txt"

b="down"


p = re.compile("down")

for line in open(output,'r'):

	m=p.search(line)

	if m:
           m=m.group()
           print "Interface is DOWN"
        
q = re.compile("UP")

for line in open(output,'r'):

        n=q.search(line)

        if n:
           n=n.group()
           print "Interface is UP"
