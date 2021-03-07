#!/usr/bin/env python3
#simplicity and runtime are valued- find missing number in range of 1 to n
#think of halves/halving (binary search)
#given integer n, return least number of perfect squares that sum to n (can repeat squares)
import math 
def missingnumberfinder(endnum):
	print("a run")
	middle = math.floor(len(endnum)/2)
	print(middle)
	print(endnum[middle])
	if len(endnum) == 2:
		return (endnum[0]+endnum[1])/2
	if middle+1 == endnum[middle]:
		return missingnumberfinder(endnum[middle:])
	if middle+2 == endnum[middle]:
		return missingnumberfinder(endnum[0:middle])
	
if __name__ == "__main__":
	print(missingnumberfinder([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17]))
	
