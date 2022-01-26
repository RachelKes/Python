#! /usr/bin/python3

class Student:
    def __init__(self, id, last_name, first_name):
        self.__id = id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__preffered_name = ''
        self.__phonetic_name = ''
        self.__email = ''
        self.__unix_username = ''
    
    def get_it(self):
        return self.__id

    def get_last_name(self):
        return self.__last_name

    def get_first_name(self):
        return self.__first_name

data_file = open('students.txt', 'r')
students = {}
for line in data_file:
    line = line.strip()
    id, last_name, first_name = line.split(',')
    if id not in students:
        student = Student(id, last_name, first_name)
        students[id] = student
data_file.close()

for id in students:
    student = students[id]
    name = student.get_first_name() + ' ' + student.get_last_name()
    print(name) 