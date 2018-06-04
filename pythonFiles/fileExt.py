#!/usr/bin/python
import magic
import os
import yaml

def getFileExt(fileName):
    paths = [os.path.abspath('magic_files/regex.mgc'), ]
    flags = magic.MAGIC_MIME_TYPE | magic.MAGIC_MIME_ENCODING | magic.MAGIC_CONTINUE
    flags=0
    with magic.Magic(paths=paths, flags=flags) as m:
        res = m.id_filename(fileName)#
        #print(fileName)

    return res


#print(getFileExt("examples/eml-200/00_eml-200.xml"))
