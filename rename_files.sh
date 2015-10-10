#!/bin/bash

# C:/Users/Shan/Downloads/
cd C:/Users/Shan/Downloads/PA_Wetlands/out

for f in *.kmz
do
# echo $f
# remname foo_120.kml to 120.kml
# token=$(IFS=_; set -- $f; shift 3; echo "$*")
# token=${token//[_]/}
# echo "${f%.*}"'.kmz'
# mv  $f "${f%.*}"'.kmz'
mv  $f "PA_"$f

# echo "HI_"$f

# substring
# echo ${f:6}

done