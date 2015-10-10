#
# Python Script:
#
import os, os.path
import re
import csv
import sys
import ogr
directory = "C:\Users\Shan\Downloads\DE_Parcels_Zipcode_NCCFIXED\Kent\\test"
destination = directory + '\csv\\'

if not os.path.exists(destination):
	print destination
	os.makedirs(destination)
	print '\csv created.'
else:
	print '\csv already exists and files being dumped there'

tmpfile = destination +  'tmp.csv'
def main():
	for root, _, files in os.walk(directory):
		for f in files:
			fullpath = os.path.join(root, f)
			path, file = os.path.split(fullpath)
			
			if(file[len(file)-3:len(file)] == "shp"):
				#ogr2ogr -f "KML" output_name.kml input_name.shp
				input =  fullpath
				outfile =  destination + file[:len(file)-4] + '.csv'
				os.system('ogr2ogr -f CSV ' + tmpfile  + ' ' + input +  ' -lco GEOMETRY=AS_WKT')
				try:
					writeCoordinatesCsv(tmpfile, outfile)
				finally:
					os.system('del ' + tmpfile)


def writeCoordinatesCsv(tmpfile, outfile):
	with open(tmpfile, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		with open(outfile, 'w') as csvfile:
		
			outwriter = csv.writer(csvfile, delimiter=',',
										quotechar='"', quoting=csv.QUOTE_MINIMAL)		
		
			for row in reader:
				outRow = []
				
				for i in range(1, len(row)):
					outRow.append(row[i].strip())

				if(row[0] == "" or row[0] == None or row[0] == 'WKT'):
					outRow.append(row[0])
					outRow.append(row[0])
					outRow.append(row[0])
				else:
					poly_Wkt = row[0]
					geom_poly = ogr.CreateGeometryFromWkt(poly_Wkt)
					centroid = geom_poly.Centroid()
					c = str(centroid)
					d = re.search("(\()(.+)(\))",c)
					try:
						coords = d.group(2).split(' ')
						outRow.append(row[0])
						outRow.append(float(coords[0]))
						outRow.append(float(coords[1]))
					except:
						print c
						outRow.append(0)
						outRow.append(0)
				outwriter.writerow(outRow)
			
			
main()