def getCentroid(paths):
    f;
    x = 0;
    y = 0;
    numPoints = paths.length;
    j = numPoints-1;
    area = 0;

	# formula from wikipedia
		
	# Cx 1/6A * Sum(i = o, j = n-1){(x_i + x_i+1)(x_i y_{i+1} - x_{i-1} y_i)}
	
    for  i in range(0, j):  
		pt1 = paths[i];
		pt2 = paths[j];

		#This is the second term in all three summations
		f = pt1[0] * pt2[1] - pt2[0] *  pt1[1];

		#Cx
		x += (pt1[0]() + pt2[0]()) * f;

		Cy
		y += ( pt1[1] +  pt2[1]) * f;

		# Calculate A
		area += pt1[0]() *  pt2[1];
		area -=  pt1[1] * pt2[0]();        
		
	area = float(area)/2
	f = area * 6
	centroid = [float(x)/f, float(y)/f]
	return centroid

def main():

	print 'hello'

main()