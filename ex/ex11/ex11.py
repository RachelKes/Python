#! /usr/bin/python3

import re

def regex_test(pattern_string, line):
    pattern_object = re.compile(r"" + pattern_string)
    match_object = pattern_object.search(line)
    if match_object:
        print("Regular expression:", pattern_string, "Matches:", line)
    else:
        print("Regular expression:", pattern_string, "Does NOT match", line)

regex_test("man", "A man, a plan, a canal. Panama")
regex_test(".*man", "A man, a plan, a canal. Panama")

regex_test("th.n", "than")
regex_test("th.n", "then")
regex_test("th.n", "thing")

regex_test("be+", "behind")
regex_test("be+", "bee")

regex_test("th?", "theme")
regex_test("th?", "tan")

regex_test("\d", "than")
regex_test("\d", "123")

regex_test("\D", "than")
regex_test("\D", "123")

regex_test("\w", "than")
regex_test("\w", "123")

regex_test("\W", "than")
regex_test("\W", "123")