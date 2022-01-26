#! /usr/bin/python3

import re

def test_regular_expression(regex, test_string):
    pattern = re.compile(r"" + regex)
    match = pattern.search(test_string)
    if match:
        try:
            return match.group(1)
        except:
            print("Match found but no substring returned")
    else:
        print(regex, "does not match", test_string)
        return ""

line_1 = "123.134.32.12 - - [12/Feb/2016:00:03:21 +0000] GET /08_exercise_it117.html  HTTP/1.1 200 56810323"
line_2 = "Mar 16 11:58:13  sshd[12041]: Accepted password for pe15 from 65.96.149.57 port 60695 ssh2"

regex_1  = "(\d+\.\d+\.\d+\.\d+)"
regex_2  = "\[(\d+)"
regex_3  = "/(\D+)/"
regex_4  = "/(\d+)"
regex_5  = ":(\d+:\d+:\d+)"
regex_6  = "GET\s+/(\w+\.\w+)"
regex_7  = "(\D+)"
regex_8  = "(\d+:\d+:\d+)"
regex_9  = "for\s+(\w+)\s+"         
regex_10 = "port\s+(\d+)"

print("regex_1",  regex_1, "\t ", test_regular_expression(regex_1, line_1))
print("regex_2",  regex_2, "\t ", test_regular_expression(regex_2, line_1))
print("regex_3",  regex_3, "\t ", test_regular_expression(regex_3, line_1))
print("regex_4",  regex_4, "\t ", test_regular_expression(regex_4, line_1))
print("regex_5",  regex_5, "\t ", test_regular_expression(regex_5, line_1))
print("regex_6",  regex_6, "\t ", test_regular_expression(regex_6, line_1))
print("regex_7",  regex_7, "\t ", test_regular_expression(regex_7, line_2))
print("regex_8",  regex_8, "\t ", test_regular_expression(regex_8, line_2))
print("regex_9",  regex_9, "\t ", test_regular_expression(regex_9, line_2))
print("regex_10", regex_10,"\t ", test_regular_expression(regex_10,line_2))