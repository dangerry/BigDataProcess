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
            element = row.split(",")
            d = list(map(int, element[1].split("/")))
            day = weekday[date(d[2], d[0], d[1]).weekday()]
            info = (element[0], day)
            values = (int(element[2]), int(element[3]))

            if info not in uber:
                uber[info] = values
            else:
                uber[info] += values

    with open(sys.argv[2], "wt") as wf:
        for k, v in uber.items():
            vehicles = 0; trips = 0
            for i in range(len(v)):
                if i % 2 == 0:
                    vehicles += v[i]
                else:
                    trips += v[i]
            wf.write("%s,%s %d,%d\n" % (k[0], k[1], vehicles, trips))
            #print("%s,%s %d,%d\n" % (k[0], k[1], vehicles, trips))

except FileNotFoundError as e:
    print("File Not Found")
#print(uber)
