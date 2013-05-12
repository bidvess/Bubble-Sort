#!/usr/bin/python
#############################################################
# Bubblesort for Python                                     #
# by: Dennis Linuz <dennismald@gmail.com>                   #
# Demonstration of a bubble 		                    #
#############################################################

import sys,time

input_array=[]
if (len(sys.argv) < 2):
    print ""
    print "Please input list items"
    print "here is change"
    print "\nExample: ./bubblesort.py <item1> [item2] [item3] [item4] ..."
    quit()
i=1
#loop for checking numbers
while (i < len(sys.argv)):
    input_array.append(int(sys.argv[i]))
    i+=1

def bubbleSort(array):
	length=len(array)
	result = True
	global count
	while result:
		result = False
		i=0
		while (i < length-1):
			if (array[i] > array[i+1]):
				tempVar = array[i]
				array[i] = array[i+1]
				array[i+1] = tempVar
				result = True
			i=i+1
			count+=1
			print "Sorting: " + str(array)
	return array
count = 0
time1 = time.time()
arrayResult = str(bubbleSort(input_array))
#sorted array after bubble sort
print ""
print "new change"
print "Sorted after " + str(count) + " tries."
print "Sorted:  " + arrayResult 
print "---"
a="sss"
b="bbb"
print a+b
print "Overall Time: " + str(time.time()-time1) + " seconds"
