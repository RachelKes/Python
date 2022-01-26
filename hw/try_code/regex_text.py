import re

def regex_test(regular_expression, line):
	pattern_object = re.compile(r'' + regular_expression)
	match_object = pattern_object.search(line)
	if match_object:
		print("Regular expression:", regular_expression)
		print("Matches:", line)
	else:
		print("Regular expression:", regular_expression)
		print("Does NOT match", line)

