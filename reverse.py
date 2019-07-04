#! /usr/bin/env python


import sys


name=raw_input("Enter the string :")

rev=name[::-1]

#print rev

fcap=rev[:0]+rev[0].swapcase()+rev[1:]

#print fcap

scap=fcap[:5]+fcap[5].swapcase()

print scap

def swap(scap, i, j):
    return ''.join((scap[:i], scap[j], scap[i+1:j], scap[i], scap[j+1:]))

print swap(scap,1,4)




