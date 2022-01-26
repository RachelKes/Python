#! /usr/bin/python3

def print_dictionary_pairs(dict):
    for key in dict:
        print(key, dict[key])

def dictionary_from_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Cannot open file', filename)
    else:
        dict = {}
        for line in file:
            list = line.split()
            key = list[0]
            value = list[1]
            dict[key] = value
        file.close()
        return dict

def student_dictionary_create(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Cannot open', filename)
    else:
        data = {}
        for line in file:
            data_list = line.split()
            student_id = data_list[0]
            first_name = data_list[1]
            last_name = data_list[2]
            username = data_list[3]
            email = data_list[4]
            student_tuple = (first_name, last_name, username, email)
            data[student_id] = student_tuple
        return data

name_emails = dictionary_from_file('xxxx')
print()
name_emails = dictionary_from_file('names_emails.txt')
print_dictionary_pairs(name_emails)
print()
print()
student_data = student_dictionary_create('xxx')
print()
student_data = student_dictionary_create('student_data.txt')
for id in student_data:
    student_tuple = student_data[id]
    print(id, student_tuple[0], student_tuple[1],
          student_tuple[2], student_tuple[3])

