#!/usr/bin/env python3
'''
memoizationht = {0:1,1:1}
def fibinacci(term):
	for a in range(2,term):
	'''	
	
	
'''
do knapsack problem with memoization



'''
'''
memoization_ht = {0:1,1:1}
def fibonnaci(n):
	print(n-1,n-2)
	if n in memoization_ht:
		return memoization_ht[n]
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		n_1 = fibonnaci(n-1)
		n_2 = fibonnaci(n-2)
		memoization_ht[n-1] = n_1
		memoization_ht[n-2] = n_2
	return fibonnaci(n-1)+fibonnaci(n-2)

if __name__ == "__main__":
	print(fibonnaci(192))
'''
memoizationht = {0:1,1:1}
def fibinacci(term):
	for a in range(2,term):
		
	
