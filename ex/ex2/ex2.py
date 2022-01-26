#! /usr/bin/python3

file = open('temps.txt', 'r')
for line in file:
    fields = line.split()
    date = fields[0]
    temp = fields[1]
    print(date,temp)
