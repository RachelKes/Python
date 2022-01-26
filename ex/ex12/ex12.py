#! /usr/bin/python3

import re

def ip_address_from_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print('Could not open', filename)
    else:
        pattern_object = re.compile(r'\D*(\d+\.\d+\.\d+\.\d+)')
        for line in file:
            match_object = pattern_object.match(line)
            if match_object:
                ip_address = match_object.group(1)
                print(ip_address)

def regex_test_with_group(regex, string):
    pattern_object = re.compile(r'' + regex)
    match_object = pattern_object.match(string)
    if match_object:
        try:
            return_string = match_object.group(1)
            print('regular expression:', regex)
            print('matches:', string)
            print('returns:', return_string)
        except:
            print("Match found but no substring returned")
    else:
        print("No match")

ip_address_from_file("apache_log.txt")
regex_test_with_group('(\d\d\d)', '123456789')
regex_test_with_group("(\d{5})", "123456789")
regex_test_with_group("(\w{6})", "123456789")
regex_test_with_group("(\w{6})", "abcdefghijk")
regex_test_with_group("\d+(\d\s+\w{2})", "12345 abcdefghijk")
regex_test_with_group(".*(b{3})", "---bbbbbbbbb---")
regex_test_with_group("\D*(\d{2,5})", "---12---------")
regex_test_with_group("\D*(\d{2,5})", "---12345---------")
regex_test_with_group("([abc]{2})", "bcaewrosdf")
regex_test_with_group( "\W*([a-d]+)", "---------bacdnmonpn---------")
regex_test_with_group("<td>(.*?)</td>", "<td>Class 4</td> <td>February 6th</td>")
