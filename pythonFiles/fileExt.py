#!/usr/bin/python
import magic
import os
def getFileExt(fileName):
    paths = [os.path.abspath('magic_files/dataONE.mgc'), ]
    flags = magic.MAGIC_MIME_TYPE | magic.MAGIC_MIME_ENCODING | magic.MAGIC_CONTINUE
    flags=0
    with magic.Magic(paths=paths, flags=flags) as m:
        fileType = m.id_filename(fileName)#

    return fileType


#print(getFileExt("examples/eml-200/00_eml-200.xml"))
