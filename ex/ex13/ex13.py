#! /usr/bin/python3

# adds the points in a scoring sheet
# and write the total score to the last line of the file

import os
import os.path
import sys
import re

# opens a file for reading if it can
# otherwise quits
def open_file_read(filename):
    try:
        file = open(filename, "r")
    except:
        print("Cannot open", filename)
    else:
        return file

# opens a file for writing
def open_file_write(filename):
    try:
        file = open(filename, "w")
    except:
        print("Could not open", filename)
    else:
        return file

if len(sys.argv) < 2:
    print("Usage:", os.path.basename(sys.argv[0]), "SCORING_SHEET_FILENAME")
    sys.exit()

filename = sys.argv[1]
file = open_file_read(filename)
new_filename = filename + ".new"
new_file = open_file_write(new_filename)
pattern = re.compile(r"\D*(\d{1,2})\s*points")
total = 0
for line in file:
    if "Score" not in line:
        new_file.write(line)
    match = pattern.match(line)
    if match:
        score = int(match.group(1))
        total += score
new_file.write("Score: " + str(total) + "\n")
file.close()
new_file.close()
os.system("mv " + new_filename + " " + filename)
