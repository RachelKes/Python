#! /usr/bin/python3
class Computer:
    def __init__(self, manufacturer, model, serial_number, processor, ram, hostname, disk_size):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__serial_number = serial_number
        self.__processor = processor
        self.__ram = ram
        self.__hostname = hostname
        self.__disk_size = disk_size
    
    def get_manufacturer (self):
        return self.__manufacturer

    def get_model(self):
        return self.__model
    
    def get_serial_number(self):
        return self.__serial_number
    
    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram
    
    def get_hostname(self):
        return self.__hostname
    
    def get_disk_size(self):
        return self.__disk_size

c1 = Computer('Apple', "Power Mac", "34145", "3.7 GHz Quad-Core Intel Xeon E5", '12 GB', 'Neptune', '250 GB')
print(c1.get_manufacturer())
print(c1.get_model())
print(c1.get_serial_number())
print(c1.get_processor())
print(c1.get_ram())
print(c1.get_hostname())
print(c1.get_disk_size())
