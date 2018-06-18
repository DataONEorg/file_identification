#!/usr/bin/env python
import os 
import tika
#tika.initVM()
from tika import parser
from tika import detector
#tika.TikaClientOnly = True
#parsed = parser.from_file('parser.java')
print(detector.from_file('../examples/eml-200/00_eml-200.xml'))


home = os.getenv('HOME')
tika.tika.TikaServerClasspath = home + '/git/geotopicparser-utils/mime:'+home+'/git/geotopicparser-utils/models/polar'
print(detector.from_file('https://github.com/chrismattmann/geotopicparser-utils/tree/master/geotopics/polar.geot'))
