#!/usr/bin/python3

list_a = [i for i in range(1, 11)]
list_b = [n * n for n in list_a]
dic = dict(zip(list_a, list_b))
print(dic)
print(dic.get(6))
