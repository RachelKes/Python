#! /usr/bin/python3

# Define the superclass Product
class Product:
    def __init__(self, name, sku, price, source):
        self.__name = name
        self.__sku = sku
        self.__price = float(price)
        self.__source = source

    def get_name(self):
        return self.__name
    
    def get_sku(self):
        return self.__sku
    
    def get_price(self):
        return self.__price

    def get_source(self):
        return self.__source

    def __str__(self):
        return self.__name + ": " + self.__sku + " " + str(self.__price) + ", " + self.__source

# Define the subclass Dry_Good inherits attributes and methods from the superclass Product
class Dry_Good (Product):
    def __init__(self, name, sku, price, source, weight):
        Product.__init__(self, name, sku, price, source)
        self.__weight = int(weight)
    
    def __str__(self):
        return super().__str__() + ", " + "Weight: " + str(self.__weight)

    def get_weight(self):
        return self.__weight
    
if __name__ == "__main__":
    p_1 = Product("Large Economy Tide", "132532112352", 4.57, "P&G")
    print(p_1)
    print(p_1.get_name())
    print(p_1.get_sku())
    print(p_1.get_price())
    print(p_1.get_source())
    dg_1 = Dry_Good("Large Economy Tide", "132532112352", 4.57, "P&G", 40)
    print(dg_1)
    print(dg_1.get_weight())