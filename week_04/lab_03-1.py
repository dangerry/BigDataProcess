#!/usr/bin/python3

str = "X-DSPAM-Confidence:0.8475"
num = str[str.rfind(':')+1:]
f_num = float(num)
print(f_num)
print(type(f_num))
