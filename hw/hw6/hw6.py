#! /usr/bin/python3

import os, sys

# get a certain number of command line arguments, and return them as a tuple
def get_command_line_arguments(arg_number):
        if  len(sys.argv) < arg_number:
            print("Usage:", os.path.basename(sys.argv[0]), "Argument_1", "Argument_2")
            sys.exit()
        return sys.argv[1], sys.argv[2]      

# print the pathnames of directories listed in the Unix PATH variable.
def print_path_dirs():
    for value in os.environ['PATH'].split(":"):
        print(value)

# count the number of files with a .py extension and return that value.
def executable_file_count(dir):
    os.chdir(dir)
    count = 0
    for entry in os.listdir(os.getcwd()): 
        if entry.endswith(".py"):
            count += 1
    return count

# Test Code
get_command_line_arguments(2)
agr1, arg2 = get_command_line_arguments(1)
print(agr1, arg2)
print()
print_path_dirs()
print()
dir = "/home/ghoffman/course_files/it117_files"
py_count = executable_file_count(dir)
print("Python files", py_count)
