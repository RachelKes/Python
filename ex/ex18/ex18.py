#! /usr/bin/python3

# represents a calendar date
class Date:
    def __init__(self, data_string):
        self.year, self.month, self.day = tuple(data_string.split("-"))
        self.year = int(self.year)
        self.month = int(self.month)
        self.day = int(self.day)

    # converts a month number into a month name
    def get_month_name(self):
        month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                       7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        return month_names[self.month]

    # returns a date in standard format
    def format_date(self):
        return self.get_month_name() + " " + str(self.day) + ", " + str(self.year)

# open a file and returns the first line in
# that file without the newline


def get_first_line(filename):
    data_file = open(filename, 'r')
    date_string = data_file.readline()
    data_file.close()
    return date_string.strip()


DATA_FILENAME = "data.txt"
data_string = get_first_line(DATA_FILENAME)
data_date = Date(data_string)
print(data_date.format_date())
