#!/usr/bin/python3

import sys

genre = []
genres = dict()

try:
    with open(sys.argv[1], "rt") as df:
        data = df.read()
        rows = data.split("\n")
        for row in rows:
            info = row.split("::")
            genre = info[2].split("|")

            for i in genre:
                if i not in genres:
                    genres[i] = 1
                else:
                    genres[i] += 1

except FileNotFoundError as e:
    print("File Not Found")

with open(sys.argv[2], "wt") as wf:
    for g, c in zip(genres.keys(), genres.values()):
        wf.write("%s %d\n" % (g, c))
