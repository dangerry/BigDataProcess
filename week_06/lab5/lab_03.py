#!/usr/bin/python3

price = [10000, 8000, 7500, 12000, 25000]

for sales in map(lambda x: x * 0.8, price):
	print(sales, end=', ')
print()
