#!/usr/bin/env python

import re
import sys



def checkMAC(x):
      if re.match("[0-9a-fA-F]{2}([-:])[0-9a-fA-F]{2}(\\1[0-9a-fA-F]{2}){4}$",x.upper()):
           return 'Valid ip address =', x
      else:    
           return 'Invalid ip address=',x



print checkMAC("AA:BB:CC:DD:EE:FF")
print checkMAC("00-11-22-33-44-66")
print checkMAC("1 2 3 4 5 6 7 8 9 a b c")
print checkMAC("This is not a mac")


