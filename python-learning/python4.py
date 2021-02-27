#!/usr/bin/env python3
import math 
def leastsquares(num,array = {},counter=1):
	print(counter)
	biggestsquareofnum = math.floor(math.sqrt(num))
	biggestsquare = math.floor(math.sqrt(counter))
	print(math.sqrt(num))
	if biggestsquareofnum == math.sqrt(num):
		return 1
	if biggestsquare == math.sqrt(counter):
		array[counter] = 1
	else:
		a = array[counter - biggestsquare**2]+1
		tracker = biggestsquare
		while tracker > 0:
			a = min(a,array[counter-tracker**2]+1)
			tracker = tracker-1
			#o(sqrtn)
		array[counter] = a
	if counter == num:
		return array[counter]

	newarray = array
	newcounter = counter+1
	return leastsquares(num, newarray, newcounter)

#o(n)*o(sqrt(n))
	

if __name__ == "__main__":
	print(leastsquares(120))