#
# Python Script:
# Note: Assuming Windows operating system
# 1. go through all files
# 2. Create a new folder called kml
# 3. For any that have .shp ending convert to kml using ogr2ogr ( a tool accessible from the command line)
#
import os, os.path
import re
from subprocess import call

directory = "C:\Users\Shan\Downloads\PA"
destination = "C:\Users\Shan\Downloads\PA\kml\\"

if not os.path.exists(destination):
	os.makedirs(destination)
	print '\kml created.'
else:
	print '\kml already exists and files being dumped there'

for root, _, files in os.walk(directory):
    for f in files:
		fullpath = os.path.join(root, f)
		path, file = os.path.split(fullpath)
		
		if(file[len(file)-3:len(file)] == "shp"):
			#ogr2ogr -f "KML" output_name.kml input_name.shp
			input =  fullpath
			output =  destination + file[:len(file)-4] + '.kml'
			os.system('ogr2ogr -f "KML" ' + output + ' ' + input)
			# print path
			# print file
			# print(path[len(path)-1])
