#
# A script in python to combine the body of all geojson's together
# into one large geojson. From there either open in Qgis or use ogr2ogr.
#
#
# TODO: have it not keep everything in memory all at once. ( I have already hit memory errors in PA)
# TODO: ADD THE ogr2ogr part here.
#

# ogr2ogr -F "ESRI Shapefile" filename.shp geojsonfile.json OGRGeoJSON


import json
import collections 
import os
import sys
import zipfile

print(sys.argv)


# directory = "C:\Users\Shan\Downloads\work\NY\Schenectady"
directory = sys.argv[1]

if len(sys.argv) > 2:
	# outputName = sys.argv[1]
	outputName = sys.argv[2]
else:
	outputName = 'output'
	
destination = directory + '\\' + outputName + '\\'
# destination = directory + '\out\\'
print directory 

if not os.path.exists(destination):
	os.makedirs(destination)
	print '\out created.'
else:
	print '\out already exists and files being dumped there'

	
dict = collections.OrderedDict()

# from pprint import pprint
#
# Assuming all the files in the folder are geojsons for the same town
for root, _, files in os.walk(directory):
	
	for f in files:
		fullpath = os.path.join(root, f)
		path, file = os.path.split(fullpath)
		print fullpath
		
		json_data=open(fullpath)


		data = json.load(json_data)

		if len(dict.keys()) == 0:
		#first time trying to merge files so need to grab the information
		
			# For some reason if "feature collection" field of json is not at the top, it will not open in Qgis.
			dict["type"] =  "FeatureCollection"	
			for key in data.keys():
				dict[key] = data[key]
			
		else:
			#just need to append the features attribute
			for d in data["features"]:
				dict["features"].append(d)

		json_data.close()

#Open file, dump json, close file.
f = open(destination + "outfile.txt",'w')
json.dump(dict,f)
f.close()
outfile = destination + outputName + ".shp"
os.system('ogr2ogr -F "ESRI Shapefile" ' + outfile + ' ' + destination + "outfile.txt" + " OGRGeoJSON")
print "rar a" + destination
# os.system("cd " + destination )
# os.system("rar a " + outputName + " " + destination )