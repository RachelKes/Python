#! /usr/bin/python3

def number_set_create():
    s = set()
    for number in range(1, 11):
        s.add(number)
    return s

def odd_even_sets_create(number_set):
    odd = set()
    even = set()
    for number in number_set:
        if number % 2 == 0:
            even.add(number)
        else:
            odd.add(number)
    return odd, even

def set_from_file(file):
    s = set()
    for string in file:
        s.add(string.strip())
    return s

numbers = number_set_create()
print(numbers)
odd, even = odd_even_sets_create(numbers)
print(odd)
print(even)
animal_file = open("animals.txt")
animals = set_from_file(animal_file)
print(animals)