import os, os.path
import re
from subprocess import call
import zipfile

directory = "C:\Users\Shan\Downloads\HI_KMLrar\out"
# destination = directory + '\kmz\\'

# if not os.path.exists(destination):
	# print destination
	# os.makedirs(destination)
	# print '\kmz created.'
# else:
	# print '\kmz already exists and files being dumped there'


for root, _, files in os.walk(directory):
    for f in files:
		fullpath = os.path.join(root, f)
		path, file = os.path.split(fullpath)
		print file
		newname = file[6:]
		os.rename(file, newname)
		# input =  fullpath
		# output =  destination + file[:len(file)-4] + '.kmz'
		# command = '7z a -tzip ' + output + ' ' + input
		# os.system(command)
		
