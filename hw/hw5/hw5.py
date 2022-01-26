#! /usr/bin/python3

# Create a file object for reading and return the object
def open_file_read(filename):
    try:
        file = open(filename, 'r')
    except:
        print("Could not open", filename)
    else:
        return file
        file.close()

# Read the file and create a set of the words in that file
def word_set_from_file(filename):
    file = open_file_read(filename)
    words = set()
    for line in file:
        fields = line.strip()
        fields = fields.split()
        for element in fields:
            words.add(element.lower())
    return words

# Print the elements of the set in alphabetical order
def ordered_word_set_print(set):
    set = sorted(set, reverse = False)
    for element in set:
        print(element)
      
# Read the file and count the words in the file
def word_count(filename):
    count = 0
    file = open_file_read(filename)
    for line in file:
        line = line.strip()
        line = line.split()
        count += len(line)
    return count

# Return the difference between the two sets
def set_difference(set_1, set_2):
    return set_1.difference(set_2)

# Test Code
filename_1 = 'gettysburg.txt'
set_1 = word_set_from_file(filename_1)
ordered_word_set_print(set_1)
print()
print("Words in " + filename_1 + ":" + str(word_count(filename_1)))
filename_2 = 'gettysburg_hay.txt'
set_2 = word_set_from_file(filename_2)
print()
print("Words in " + filename_1 + " not in " + filename_2)
ordered_word_set_print(set_difference(set_1, set_2))
print()
print("Words in " + filename_2 + " not in " + filename_1)
ordered_word_set_print(set_difference(set_2, set_1)) 