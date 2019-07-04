#!/usr/bin/env python

import re
p = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
test_str = u"TEXT WITH SOME MAC ADDRESSES 00:24:17:b1:cc:cc TEXT CONTINUES WITH SOME MORE TEXT 20:89:86:9a:86:24"

fd=re.findall(p, test_str)

print fd


