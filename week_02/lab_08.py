#!/usr/bin/python3

for i in range(3):
	n = int(input("정수 하나를 입력하세요 : "))
	if n > 0 and n % 5 == 0:
		print("5의 배수입니다.")
	else:
		print("5의 배수가 아닙니다.")
