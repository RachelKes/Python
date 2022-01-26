#! /usr/bin/python3

# Define the class Dog
class Dog:
    def __init__(self, name, breed, owner):
        self.__name = name
        self.__breed = breed
        self.__owner = owner
        self.__score = 0
    
    def get_name(self):
        return self.__name
    
    def get_breed(self):
        return self.__breed
    
    def get_owner(self):
        return self.__owner

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score

    def __str__(self):
        return self.__name + " " + self.__breed + " " + self.__owner

    def __gt__(self, other):
        return self.__score > other.__score

    def __lt__(self, other):
        return self.__score < other.__score

    def __eq__(self, other):
        return self.__score == other.__score

    def __ne__(self, other):
        return self.__score != other.__score

# Test Code
d1 = Dog("Frank", "Doberman", "Malcom Smith")
print("name: ", d1.get_name())
print("breed: ", d1.get_breed())
print("owner: ", d1.get_owner())
print("score: ", d1.get_score())
d1.set_score(95)
print("score: ", d1.get_score())
print(d1)
d2 = Dog("Rover", "German Shepard", "Bill Busby")
print(d2)
d2.set_score(82)
print("d1 > d2 :", d1 > d2)
print("d1 < d2 :", d1 < d2)
print("d1 == d2 :", d1 == d2)
print("d1 != d2 :", d1 != d2)
