#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import csv 

l_time = []

with open('trig.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        #l_time.append(row[2])
        l_time.append(row[3])
l_time_sort = l_time[::-1]

for i in range(len(l_time_sort) - 1):
    #result = (int(l_time[i]) - int(l_time[i + 1]) + 60) % 10
    result = int(l_time_sort[i]) - int(l_time_sort[i + 1])
    #if result != 1:
    if result > 10:
        print(l_time_sort[i + 1], l_time_sort[i])
