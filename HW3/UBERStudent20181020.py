#!/usr/bin/python3

import sys
import calendar

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
uber = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")

        for row in rows:
            info = row.split(",")
            d = list(map(int, info[1].split("/")))
            day = weekday[calendar.weekday(d[2], d[0], d[1])]
            s = info[0] + "," + day

            if s not in uber:
                uber[s] = info[2] + "," + info[3]
            else:
                v_t = uber.get(s).split(",")
                vehicles = int(v_t[0]) + int(info[2])
                trips = int(v_t[1]) + int(info[3])
                uber[s] = str(vehicles) + "," + str(trips)

except FileNotFoundError as e:
    print("File Not Found")

with open(sys.argv[2], "wt") as wf:
    for i, j in zip(uber.keys(), uber.values()):
        wf.write("%s %s\n" % (i, j))
