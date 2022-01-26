#! /usr/bin/python3

def print_sorted_dictionary_pairs(dict):
    for key in sorted(dict):
        print(key, dict[key])

def add_or_change_dictionary_value(dict, key, value):
    dict[key] = value

def delete_dictionary_entry(dict, key):
    if key in dict:
        del dict[key]
    else:
        print(key, 'not found in dictionary')

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

names_emails = dictionary_from_file('names_emails.txt')
for key in names_emails:
    print(key, names_emails[key])
print_sorted_dictionary_pairs(names_emails)
print()
add_or_change_dictionary_value(names_emails, 'George', 'george@hotmail.com')
add_or_change_dictionary_value(names_emails, 'Alan', 'alan.hurley@gmail.com')
print('Entries: ', len(names_emails))
print_sorted_dictionary_pairs(names_emails)
print()
delete_dictionary_entry(names_emails, 'xxxx')
delete_dictionary_entry(names_emails, 'George')
print_sorted_dictionary_pairs(names_emails)
print('Entries:', len(names_emails))