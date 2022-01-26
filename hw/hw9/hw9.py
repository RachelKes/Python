#! /usr/bin/python3

# Define the class DVD
class DVD:
    def __init__(self, title, studio, director, released):
        self.__title = title
        self.__studio = studio
        self.__director = director
        self.__released = released

    def get_title(self):
        return self.__title

    def get_studio(self):
        return self.__studio

    def get_director(self):
        return self.__director
    
    def get_released(self):
        return self.__released

    def __str__(self):
        return self.__title + ", " + self.__studio + ", " + self.__director + ", " + self.__released

# Test Code
dvd = DVD("Forbidden Planet", "Metro-Goldwyn-Mayer", "Fred M. Wilcox", "1956")
print(dvd.get_title())
print(dvd.get_studio())
print(dvd.get_director())
print(dvd.get_released())
print(dvd)

