#!/usr/bin/python3

import sys
from datetime import date

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
info = []; v = []; t = []
uber_v = dict(); uber_t = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")

        for row in rows:
            element = row.split(",")
            d = list(map(int, element[1].split("/")))
            day = weekday[date(d[2], d[0], d[1]).weekday()]
            info.append(element[0] + "," + day)
            v.append(int(element[2]))
            t.append(int(element[3]))

except FileNotFoundError as e:
    print("File Not Found")

for i, v_info, t_info in zip(info, v, t):
    if i not in uber_v:
        uber_v[i] = v_info
    else:
        uber_v[i] += v_info
    if i not in uber_t:
        uber_t[i] = t_info
    else:
        uber_t[i] += t_info


with open(sys.argv[2], "wt") as wf:
    for i, j, k in zip(uber_v.keys(), uber_v.values(), uber_t.values()):
        wf.write("%s %d,%d\n" % (i, j, k))
