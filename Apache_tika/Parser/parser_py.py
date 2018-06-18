#!/usr/bin/env python
import tika
#tika.initVM()
from tika import parser
from tika import detector
tika.TikaClientOnly = True
#parsed = parser.from_file('parser.java')
print(detector.from_file('parser.java'))

"""
parsed  = parser.from_buffer('Good evening, Dave', 'http://tika:9998/tika')
print(parsed["metadata"])
print(parsed["content"])
"""
