#
# A script in python to combine the body of all geojson's together
# into one large geojson. From there either open in Qgis or use ogr2ogr.
#
#
# TODO: have it not keep everything in memory all at once.
# TODO: ADD THE ogr2ogr part here.
#

import json
import collections 

dict = collections.OrderedDict()

# from pprint import pprint

for i in range(1,55):
	json_data=open(str(i) + '.txt')

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
f = open("outfile.txt",'w')
json.dump(dict,f)
f.close()