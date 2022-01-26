#! /usr/bin/python3

class DVD:
    # Define the attributes
    def __init__(self, title, studio, director):
        self.title = title
        self.studio = studio
        self.director = director

    # Return the value of the title attribute
    def get_title(self):
        return self.title

    # The method returns the value of the studio attribute
    def get_studio(self):
        return self.studio

    # The method returns the value of the director attribute
    def get_director(self):
        return self.director

    # The method displays a string consisting of the value of the title attribute,
    # the studio attribute, and the director attribute
    def print_dvd(self):
        print(self.title + ", " + self.studio + ", " + self.director)


# Test Code
dvd = DVD("Forbidden Planet", "Metro-Goldwyn-Mayer", "Fred M. Wilcox")
print(dvd.get_title())
print(dvd.get_studio())
print(dvd.get_director())
dvd.print_dvd()
