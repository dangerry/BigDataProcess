#!/usr/bin/python3

from openpyxl import load_workbook
from collections import Counter

wb = load_workbook(filename='student.xlsx')
ws = wb['Sheet1']

student = 0
sum_v = 0.0
row_id = 1
for row in ws:
    if row_id != 1:
        sum_v = ws.cell(row=row_id, column=3).value * 0.3
        sum_v += ws.cell(row=row_id, column=4).value * 0.35
        sum_v += ws.cell(row=row_id, column=5).value * 0.34
        sum_v += ws.cell(row=row_id, column=6).value
        ws.cell(row=row_id, column=7).value = sum_v
        student += 1
    row_id += 1

total = []
for row in ws['G']:
    total.append(row.value)
del total[0]

total_sort = sorted(total, reverse=True)

dict_count = dict(Counter(total))
print(dict_count)

rank = []
for i in total:
    if dict_count[i] > 1:
        rank.append(total_sort.index(i) + dict_count[i])
    else:
        rank.append(total_sort.index(i) + 1)
print(rank)

A = int(student * 0.3)
A_plus = int(A * 0.5); A0 = A - A_plus;
B = int(student * 0.7)
B_plus = int((B - A) * 0.5); B0 = B - A - B_plus;
C = student
C_plus = int((C - B) * 0.5); C0 = C - B - C_plus
print(A, A_plus, A0)
print(B, B_plus, B0)
print(C, C_plus, C0)

row_id = 2
for ranking in rank:
    if ranking <= A_plus:
        ws.cell(row=row_id, column=8).value = 'A+'
    elif ranking <= A:
        ws.cell(row=row_id, column=8).value = 'A0'
    elif ranking <= B - B0:
        ws.cell(row=row_id, column=8).value = 'B+'
    elif ranking <= B:
        ws.cell(row=row_id, column=8).value = 'B0'
    elif ranking <= C - C0:
        ws.cell(row=row_id, column=8).value = 'C+'
    else:
        ws.cell(row=row_id, column=8).value = 'C0'
    row_id += 1

wb.save("student.xlsx")
