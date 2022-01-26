#! /usr/bin/python3

# Find the highest score in the file and print that score with the student who got the score

# Create a file object for reading and return the file object
def open_file_read(filename):
    try:
        file = open(filename, "r")
        return file
        file.close()
    except: 
        print("File not found.") 
        return None

# Find the highest score, first and last name of the student
def highest_score(file):
    max_score = 0
    max_name = ""
    for line in file:
        score, first, last = line.split()
        score = int(score)
        name = first + " " + last
        if score > max_score:
            max_score = score
            max_name = name
    return max_score, max_name

# Test Code
filename = input("File name: ")
file = open_file_read(filename)
if file:
    max_score, max_name = highest_score(file)
    print()
    print("Highest score", max_score, max_name)
