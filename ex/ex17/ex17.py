#! /usr/bin/python3

DATA_FILENAME = "data.txt"
data_file = open(DATA_FILENAME, 'r') # open the file for reading
date_string = data_file.readline()
date_string = date_string.strip()
year, month, day = tuple(date_string.split('-'))
year, month, day = int(year), int(month), int(day)

month_names = {1:'January', 2:'February', 3:'March', 4:'April',
5: 'May', 6: 'June', 7:'July', 8: 'August', 
9:'September', 10:'October', 11:'November', 12:'December'}

new_date_string = month_names[month] + ' ' + str(day) + ', ' + str(year)
print(new_date_string)