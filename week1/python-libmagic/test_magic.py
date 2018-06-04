#!/usr/bin/python
from os import walk
from os.path import isfile
import magic
import os
import yaml

mypath = "/Users/pratikshrivastava/Desktop/OneDrive - University of Illinois - Urbana/Box/GitHub/DataONE/internship2018/file_identification/examples"

'''
for (dirpath) in walk(mypath):
    print(dirpath)

fileObj = os.listdir(mypath)
for obj in fileObj:
	print(obj, isfile(obj))
'''
'''
filetype= {}
for root, dirs, files in os.walk(mypath):
	for filename in files:
		type = filename.split('_')
		if len(type) > 1:
			filetype[filename] = type[1].split('.')[0]


print(filetype)
'''

def getFileExt(folder, filename):
	paths = [os.path.abspath('../magic_files/regex.mgc'), ]
	flags = magic.MAGIC_MIME_TYPE | magic.MAGIC_MIME_ENCODING | magic.MAGIC_CONTINUE
	flags=0
	with magic.Magic(paths=paths, flags=flags) as m:
	  res = m.id_filename(mypath +'/'+folder +'/'+filename)

	return res
	  #print(filename, res)

def chkFileType(formatId, folder,list_obj):
	for obj in list_obj:
		fileName, fileExt = obj['filename'] , getFileExt(folder,obj['filename'])
		#print("{0}\t{1}\t{2}".format(formatId, fileName, fileExt))
		if formatId != fileExt:
			print("{0}\t{1}\t{2}".format( fileName, formatId,fileExt))

catalog_name = "../../examples/catalog.yaml"
yaml_text = open(catalog_name, "r").read()
catalog = yaml.load(yaml_text)
filetype = {}

print("*"*100)
print("FileName\tFormatId\t\t\t\tFileExt")
print("*"*100)
print()
for obj in catalog['examples']:
	formatId = obj['formatId']
	folder = obj["folder"]
	chkFileType(formatId,folder, obj['identifiers'])
	#print(formatId)
