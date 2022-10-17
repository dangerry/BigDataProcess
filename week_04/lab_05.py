#!/usr/bin/python3

id_num = "901231-1914983"
year = id_num[:2]
gender = id_num[7]
if gender == "1" or gender == "3":
	print("%s년생 남자" % year)
else:
	print("%s년생 여자" % year)
