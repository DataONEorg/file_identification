#!/usr/bin/python
import magic
with magic.Magic() as m:
	print("/etc/passwd", m.id_filename("/etc/passwd"))
