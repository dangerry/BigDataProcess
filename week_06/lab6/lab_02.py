#!/usr/bin/python3

import datetime

today = datetime.datetime.today()
birth = datetime.datetime(1994, 5, 5)
day = today - birth
print(day)
