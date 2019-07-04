#! /usr/bin/env python


import re


ip="192.168.1.100"


a=re.split('\.',ip)

print a

#Comment for develpment purpose
'''
print a[0][0],a[0][1],a[0][2]

print a[1][0],a[1][1],a[1][2]

print a[2][0]

print a[3][0],a[3][1],a[3][2]
'''

print a[0]
print a[1]
print a[2]
print a[3]
