#!/usr/bin/python3

file = input()
with open(file, "rt") as f:
	text = f.read()
with open("output.txt", "wt") as fp:
	fp.write(text.upper())
