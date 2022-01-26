#! /usr/bin/python3

def rnd(num):
    try:
        return round(num)
    except TypeError as err:
        print('TypeError on round(' + num + '):', err)

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('You cannot divide a number by zero')

def convert_to_integer(string):
    try:
        return int(string)
    except ValueError:
        print(string, 'cannot be converted into an integer')

def print_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Could not open', filename)
    else:
        print(file.read())

def list_from_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Could not open', filename)
    else:
        list = []
        for line in file:
            list.append(int(line))
        return list

def read_integers_into_list(filename):
    file = open(filename, "r")
    new_list = []
    for line in file:
        number = int(line)
        new_list.append(number)
    file.close()
    return new_list

def character_count(string, char):
    count = 0
    for ch in string:
        if ch == char:
            count += 1
    return count

value = rnd(5.7)
print('value:', value)
value = rnd('five')
print('value:', value)
print()

value = divide(3, 5)
print('value:', value)
value = divide(5, 0)
print('value:', value)
print()

value = convert_to_integer('50')
print('value:', value)
value = convert_to_integer('fifty')
print('value:', value)
print()

print_file('xxxx')
print()
print_file('numbers.txt')
print()

number_list = list_from_file('numbers.txt')
print("List:", number_list)
print()

number_list = read_integers_into_list("numbers.txt")
print("List:", number_list)
print()

count = character_count("Mississippi", "i")
print('The letter i appears ', count, 'times in Mississippi')