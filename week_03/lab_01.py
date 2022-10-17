#!/usr/bin/python3

n = 1; total = 0
while n < 201:
	if n % 3 == 0:
		total += n
	n += 1
print(total)
