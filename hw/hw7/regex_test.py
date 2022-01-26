#! /usr/bin/python3

# a script for practising with regular expression matches

import re
import sys

# runs a regular exprssion on a string and displays
# a match if it finds one
def regex_test(regular_expression, line):
    pattern_object = re.compile(r"" +  regular_expression )
    match_object   = pattern_object.search(line)
    if match_object :
        print("Regular expression:", regular_expression)
        print("Matches:", line)
    else:
        print("Regular expression:", regular_expression)
        print("Does NOT match", line)

if len(sys.argv) < 3:
    print("Usage: " + os.path.basename(sys.argv[0]) + "REGULAR_EXPRESSION   STRING")
    sys.exit()

regex = sys.argv[1]
line  = sys.argv[2]

regex_test(regex, line)


          
