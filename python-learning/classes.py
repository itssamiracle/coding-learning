#!/usr/bin/env python3

class Person:
	def __init__(self, name, age, birthmonth):
		self.name = name
		self.age = age
		self.birthmonth = birthmonth
	def happybirthday(self):
		self.age += 1
class Food:
	def __init__(self,price,name,numoforders):
		self.price = price
		self.name = name
		self.numoforders = numoforders
		self.totalprice = price*numoforders
	def onemoreorder(self):
		self.numoforders += 1
if __name__ == "__main__":
	Samir1 = Person("samir",16,"october")
	print(Samir1.age)
	Samir1.happybirthday()
	print(Samir1.age)
	Amanda1 = Person("amanda",22,"February")
	print(Amanda1.name)
	hamburgers = Food(3,"hamburger",4)
	print(hamburgers.totalprice)
	
	'''
	make a class called food, make it helpful, maybe price calculator?



take a string and find most efficient way:
if there are more than one space between two characters, make it one space

"   i    lo   ve   coding    "
"i lo ve coding"
	'''
	
	
	
	