#!/usr/bin/python
from os import walk
from os.path import isfile
import magic
import os


mypath = "/Users/pratikshrivastava/Desktop/OneDrive - University of Illinois - Urbana/Box/GitHub/DataONE/internship2018/file_identification/examples"

'''
for (dirpath) in walk(mypath):
    print(dirpath)

fileObj = os.listdir(mypath)
for obj in fileObj:
	print(obj, isfile(obj))
'''

filetype= {}
for root, dirs, files in os.walk(mypath):
	for filename in files:
		type = filename.split('_')
		if len(type) > 1:
			filetype[filename] = type[1].split('.')[0]


print(filetype)
def chk_fil_type(magic_file, filename):
	paths = [os.path.abspath('../magic_files/onedcx'), ]
	flags = magic.MAGIC_MIME_TYPE | magic.MAGIC_MIME_ENCODING | magic.MAGIC_CONTINUE
	flags=0
	with magic.Magic(paths=paths, flags=flags) as m:
	  res = m.id_filename("../magic_files/01_onedcx.xml")
	  print("01_onedcx.xml:", res)
