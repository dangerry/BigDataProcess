#!/usr/bin/python3

import sys
from datetime import date

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
info = []; values = []
uber = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")

        for row in rows:
            element = row.split(",")
            d = list(map(int, element[1].split("/")))
            day = weekday[date(d[2], d[0], d[1]).weekday()]
            info.append(element[0] + "," + day)
            values.append(element[2] + "," + element[3])

except FileNotFoundError as e:
    print("File Not Found")

for i, v in zip(info, values):
    vehicles = 0; trips = 0
    if i not in uber:
        uber[i] = v
    elif i in uber:
        vt_values = list(map(int, v.split(",")))
        vt_uber = list(map(int, uber.get(i).split(",")))
        vehicles = vt_uber[0] + vt_values[0]
        trips = vt_uber[1] + vt_values[1]
        uber[i] = str(vehicles) + "," + str(trips)

with open(sys.argv[2], "wt") as wf:
    for i, j in zip(uber.keys(), uber.values()):
        wf.write("%s %s\n" % (i, j))
