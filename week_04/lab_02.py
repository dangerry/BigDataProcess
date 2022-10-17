#!/usr/bin/python3

for i in range(2):
	domain = input("웹 주소를 입력하세요 : ")
	if domain.endswith(".kr"):
		print("한국 도메인입니다")
	else:
		print("한국 도메인이 아닙니다")
