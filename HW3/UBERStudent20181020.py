#!/usr/bin/python3

import sys
import calendar

weekday = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
uber_v = dict(); uber_t = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")

        for row in rows:
            element = row.split(",")
            date = list(map(int, element[1].split("/")))
            day = weekday[calendar.weekday(date[2], date[0], date[1])]
            info = (element[0], day)

            if info not in uber_v:
                uber_v[info] = int(element[2])
            elif info in uber_v:
                uber_v[info] += int(element[2])
            if info not in uber_t:
                uber_t[info] = int(element[3])
            elif info in uber_t:
                uber_t[info] += int(element[3])

except FileNotFoundError as e:
    print("File Not Found")

with open(sys.argv[2], "wt") as wf:
    for i, j in uber_v.items():
        wf.write("%s,%s %d,%d\n" % (i[0], i[1], j, uber_t.get(i)))
