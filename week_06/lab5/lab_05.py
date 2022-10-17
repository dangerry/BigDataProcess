#!/usr/bin/python3

import json

with open('movie.json') as datafile:
	jsondata = json.load(datafile)

movie = list(jsondata['movie'])

total = 0
for salesAmt in movie:
	total += int(salesAmt['salesAmt'])

print("오늘 매출액은 총 %d 원" % total)
