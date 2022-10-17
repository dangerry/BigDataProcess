#!/usr/bin/python3

def find_max(*ints):
	max_num = ints[0]

	for num in ints:
		if num > max_num: 
			max_num = num
	return max_num

print(find_max(1, 4, 6))
print(find_max(10, 5, 87, 57, 38))
print(find_max(4, 3, 2, 1))
