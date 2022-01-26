#! /usr/bin/python3

# tests regular expressions and returns 
# the first group if it can

import re
import os.path
import sys

def regex_match_with_group(regular_expression, line):
    pattern_object = re.compile(r"" + regular_expression)
    match_object   = pattern_object.search(line)
    if match_object :
        try :
            return_string = match_object.group(1)
            print("regular expression:", regular_expression)
            print("matches:", line)
            print("returns:",  return_string)
        except :
            print("Match found but no substring returned")
    else:
        print("No match")    

if len(sys.argv) < 3 :
    print("Usage: ", os.path.basename(sys.argv[0]), " REGULAR_EXPRESSION  STRING_TO_MATCH")
    sys.exit()

regex = sys.argv[1]
line  = sys.argv[2]

regex_match_with_group(regex, line)

