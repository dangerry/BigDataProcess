#!/usr/bin/python3

import sys
from datetime import date

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
uber = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")

        for row in rows:
            info = row.split(",")
            d = list(map(int, info[1].split("/")))
            day = weekday[date(d[2], d[0], d[1]).weekday()]
            s = info[0] + "," + day

            vehicles = 0; trips = 0
            if s not in uber:
                uber[s] = info[2] + "," + info[3]
            else:
                v_t = list(map(int, uber.get(s).split(",")))
                vehicles = v_t[0] + int(info[2])
                trips = v_t[1] + int(info[3])
                uber[s] = str(vehicles) + "," + str(trips)

except FileNotFoundError as e:
    print("File Not Found")

with open("output2.txt", "wt") as wf:
    for i, j in zip(uber.keys(), uber.values()):
        wf.write("%s %s\n" % (i, j))
