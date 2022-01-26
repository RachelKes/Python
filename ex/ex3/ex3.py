#! /usr/bin/python3

def average(filename):
    file = open(filename, "r")
    total = 0
    count = 0
    for line in file:
        date, temp = line.split()
        total += int(temp)
        count += 1
    file.close()
    return round(total/count)

def maximum(filename):
    file = open(filename, "r")
    max = -500
    for line in file:
        date, temp = line.split()
        temp = int(temp)
        if temp > max:
            max = temp
    file.close()
    return max

def minimum(filename):
    file = open(filename, "r")
    min = 500
    for line in file:
        data, temp = line.split()
        temp = int(temp)
        if temp < min:
            min = temp
    file.close()
    return min

print('Maximum: ', maximum('temps.txt'))
print('Minimum: ', minimum('temps.txt'))
print('Average: ', average('temps.txt'))
print()