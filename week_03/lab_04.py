#!/usr/bin/python3

for i in range(1, 11):
	for j in range(10, i, -1):
		print(" ", end='')
	for j in range(0, 2*i-1):
		print("*", end='')
	print()
