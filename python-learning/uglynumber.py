#!/usr/bin/env python3
#ugly number- check whether given number is positive number who's prime factors are only 2,3,5
def uglynumberfinder(number):
	a = number
	while number%3 == 0:
		number = number/3
	a = number
	while number%5 == 0:
		number = number/5		
	a = number
	while number%2 == 0:
		number = number/2	
	if number == 1:
		return True
	return False

if __name__ == "__main__":
	print(uglynumberfinder(120))
