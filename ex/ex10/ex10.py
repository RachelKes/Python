#! /usr/bin/python3

import os
import sys
import platform

def print_args():
    arg_count = 0
    for arg in sys.argv:
        arg_count += 1
        print("Argument #", arg_count, ":\t", arg)

def print_dir(dir_path):
    contents = os.listdir(dir_path)
    for entry in sorted(contents):
        print(entry)

def print_var(var_name):
    try:
        var_value = os.environ[var_name]
    except:
        print(var_name, "is not an environment variable")
    else:
        print(var_name + ": " + var_value)

print("sys.argv:", sys.argv)
print_args()
print()
if platform.node() == "pe15":
    print("Contents of /home/ghoffman/course_files/it117_files/ex10_test")
    print_dir("/home/ghoffman/course_files/it117_files/ex10_test")
else:
    print("Contents of current directory")
    print_dir(".")
print()
print_var("shell")
print_var("SHELL")
