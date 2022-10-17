#!/usr/bin/python3

try:
	input_nums = input("숫자 두 개를 입력하세요 : ")
	num_arr = [int(i) for i in input_nums.split()]
	result = num_arr[0] / num_arr[1]
	print(result)
except ZeroDivisionError as e:
	print("division by zero")
