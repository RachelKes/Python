#! /usr/bin/python3

import sys
import pickle

pickle_filename = 'students.dat'

class Section:
    def __init__(self, course_id, semester, section_no):
        self.__course_id = course_id
        self.__semester = semester
        self.__section_no = str(section_no)
        self.__student_ids = set()
    
    def add_students(self, data_filename):
        try:
            data_file = open(data_filename, 'r')
        except:
            print("Could not open", data_filename)
            sys.exit()
        for line in data_file:
            line = line.strip()
            id, last_name, first_name = line.split(',')
            self.__student_ids.add(id)
        data_file.close()
    
    def get_enrolled_students(self):
        enrolled_students = {}
        try:
            pickle_file = open(pickle_filename, 'rb')
        except:
            print("Could not open", pickle_filename)
            sys.exit()
        all_students = pickle.load(pickle_file)
        pickle_file.close()
        for id in self.__student_ids:
            enrolled_students[id] = all_students[id]
        return enrolled_students
    
    def __str__(self):
        return self.__course_id + " " + self.__semester + " section " + str(self.__section_no)

if __name__ == "__main__":
    section = Section("it117", "s17", 1)
    print(section)
    section.add_students("students.txt")
    enrolled_students = section.get_enrolled_students()
    for id in enrolled_students:
        print(enrolled_students[id])