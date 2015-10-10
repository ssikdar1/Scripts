#ogr2ogr -f "KML" output_name.kml input_name.shp

cd C:/Users/Shan/Downloads/NY/wgs/Erie
mkdir kml_test/

#ogr2ogr -f "KML" output_name.kml input_name.shp
for f in *.shp
do
output="kml_test/${f%.*}"'.kml'
ogr2ogr -f "KML" $output $f
done


