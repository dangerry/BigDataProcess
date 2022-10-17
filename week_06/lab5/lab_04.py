#!/usr/bin/python3

from_dict = dict()

file = input("Enter file name : ")
with open(file, "rt") as fp:
	for line in fp:
		if line.startswith("From: "):
			str_arr = line.split()
			if str_arr[1] not in from_dict:
				from_dict[str_arr[1]] = 1
			else:
				from_dict[str_arr[1]] += 1
print(from_dict)
