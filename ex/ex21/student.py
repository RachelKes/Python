class Student:
    '''
    a class representing a student in one of my classes
    '''
    
    def __init__(self, id, last_name, first_name):
        self.__id             = id
        self.__last_name      = last_name
        self.__first_name     = first_name
        self.__preferred_name = ''
        self.__phonetic_name  = ''
        self.__email          = ''
        self.__unix_username  = ''
        
    def get_id(self):
        return self.id
    
    def get_last_name(self):
        return self.__last_name
    
    def get_first_name(self):
        return self.__first_name
    
    def get_preferred_name(self):
        return self.__preferred_name
    
    def get_phonetic_name(self):
        return self.__phonetic_name
    
    def get_email(self):
        return self.__email
    
    def get_unix_username(self):
        return self.__unix_username
    
    def set_preferred_name(self, preferred_name):
        self.__preferred_name = preferred_name
    
    def set_phonetic_name(self, phonetic_name):
        self.__phonetic_name = phonetic_name
    
    def set_email(self, email):
        self.__email = email
    
    def set_unix_username(self, unix_username):
        self.__unix_username = unix_username
        
    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ', ' + self.__id
    
    def get_full_name(self):
        if self.__preferred_name:
            return self.__preferred_name + ' ' + self.__last_name
        else:
            return self.__first_name + ' ' + self.__last_name
        
    def get_sort_name(self):
        if self.__preferred_name:
            return self.__last_name + ', '  + self.__preferred_name
        else:
            return self.__last_name + ', '  + self.__first_name 
        
    
