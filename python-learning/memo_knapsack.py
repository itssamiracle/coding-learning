#!/usr/bin/env python3
memo_ht = {}
def knapsack(maxweight,listofweights,listofvalues,valuesum=0):
	print(listofvalues)
	if maxweight == 0:
		thetuple = (tuple(listofvalues),"a",maxweight)
		memo_ht[thetuple] = valuesum
		return valuesum
	if len(listofweights) == 0:
		thetuple = (tuple(listofvalues),"a",maxweight)
		memo_ht[thetuple] = valuesum
		return valuesum
	if listofweights[0] > maxweight:
		return(knapsack(maxweight, listofweights[1:], listofvalues[1:], valuesum))

	tuplea = (tuple(listofvalues[1:0]) , "a", maxweight-listofweights[0])
	print(isinstance(tuplea, tuple))
	if tuplea in memo_ht:
		a = memo_ht[tuplea]
	else:
		a = knapsack(maxweight-listofweights[0], listofweights[1:], listofvalues[1:],valuesum+listofvalues[0])
	tupleb = (tuple(listofvalues[1:]),"a",maxweight)
	if tupleb in memo_ht:
		b = memo_ht[tupleb]
	else:
		b = knapsack(maxweight, listofweights[1:], listofvalues[1:], valuesum)
	return max(
	a,b)
	

if __name__ == "__main__":
	listofweights = [19,4,6,7,3]
	listofvalues = [x+1 for x in listofweights]
	print(knapsack(20, listofweights ,listofvalues))
