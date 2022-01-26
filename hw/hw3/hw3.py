#! /usr/bin/python3

# create a file object for reading and return the object
def open_file_read(filename):
    try:
        file = open(filename, "r")
        return file
        file.close()
    except:
        print("File is not found.")
        return None

# read the file and create a dictionary where the state names are the keys and the values are population
def state_dictionary_create(file):
    data_dict = {}
    for line in file:
        fields = line.strip() 
        fields = fields.split(",")
        state = fields[0]
        population = fields[1]
        data_dict[state] = population
    return data_dict

# print the key and value for each enty in the dictionary sorted by key
def print_dictionary(dict):
    for state in sorted(dict):
        print(state, dict[state])

# Test Code
filename = input("File name: ")
file = open_file_read(filename)
if file:
    state_populations = state_dictionary_create(file)
    if state_populations:
        print_dictionary(state_populations)

