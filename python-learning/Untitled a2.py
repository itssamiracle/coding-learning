#!/usr/bin/env python3
#1,10,25 cent coins
def coinproblem(amount,coin_count=0):
	if amount == 0:
		return coin_count
	return min(
		
			coinproblem(amount-1, coin_count+1),
			coinproblem(amount-5, coin_count+1),
			coinproblem(amount-25, coin_count+1)
			
	)
	
	
if __name__ == "__main__":
	print(coinproblem(6))