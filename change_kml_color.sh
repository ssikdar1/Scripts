#!/bin/bash



function shp2kml(){
	#
	# shp files to kml
	#
echo 'shp files to kml'
cd C:/Users/Shan/Downloads/NY/wgs/Monroe
mkdir kml/
#ogr2ogr -f "KML" output_name.kml input_name.shp
for f in *.shp
do
echo $f
output="kml/${f%.*}"'.kml'
ogr2ogr -f "KML" $output $f
done            
}



kmz files to kml

cd C:/Users/Shan/Downloads/WA_Wetlands_KMLs
mkdir kml/
for f in *.kmz
do
# echo $f
output="${f%.*}"'.kml'
input=$f
7z e $input $output
done

#
# Change the color of kml to default of yellow and line width of 1.5
#
echo 'changing color'
# cd C:/Users/Shan/Downloads/HI_KMLrar
mkdir out

# # # #purple ffff55aa  white ffffffff

original="<Style><LineStyle><color>ff0000ff<\/color><\/LineStyle><PolyStyle><fill>0<\/fill><\/PolyStyle><\/Style>"
# new="<Style><LineStyle><color>ffff55aa<\/color><width>1.5<\/width><\/LineStyle><PolyStyle><fill>0<\/fill><\/PolyStyle><\/Style>"

newWetlands="<Style><LineStyle><color>ff00ff00<\/color><\/LineStyle><PolyStyle><color>4dff8000<\/color><\/PolyStyle><\/Style>"
# cd out
for f in *.kml
do
echo $f
sed "s/$original/$newWetlands/g" < "$f" > "out/$f"
rm $f
done

#Convert kml to kmz using 7 zip
echo 'Converting to kmz'
cd out/
for f in *.kml
do
output="${f%.*}"'.kmz'
input=$f
7z a -tzip $output $input
rm $f
done

