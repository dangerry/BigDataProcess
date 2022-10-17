#!/usr/bin/python3

score = input("5개의 성적을 입력하세요(각 값은 공백으로 분리) : ")
s_list = score.split()
int_list = [int(i) for i in s_list]
int_list.sort()
print(int_list)
