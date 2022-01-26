#! /usr/bin/python3

# Create a file object for reading and return the object
def open_file_read(filename):
    try: 
        file = open(filename, "r")
        return file
        file.close()
    except: 
        print("File is not found")

# Create a dictionary where the id is the key and a list of grades is the value
def quiz_dictionary_create(file):
    quiz_scores = {}
    if file:
        for line in file:
            fields = line.split()
            id = fields[0]
            scores = []
            for score in range(1, len(fields)):
                scores.append(fields[score])
            quiz_scores[id] = scores
        return quiz_scores

# Create a dictionary where the id is the key and the average score is the value
def average_dictionary_create(dict):
    quiz_grades = {}
    for id in dict:
        grades = dict[id]
        total = 0
        for grade in grades:
            total += int(grade)
        average = round(total/len(grades))
        quiz_grades[id] = average
    return quiz_grades

# Print the key and value for each entry in the dictionary sorted by key
def print_dictionary(dict):
    for id in sorted(dict):
        print(id, dict[id])

# Test code
file = open_file_read("quiz_scores.txt")
scores = quiz_dictionary_create(file)
print_dictionary(scores)
print()
averages = average_dictionary_create(scores)
print_dictionary(averages)