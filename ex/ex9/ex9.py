#! /usr/bin/python3

def set_create_from_file (filename):
    new_set = set()
    try:
        file = open(filename, "r")
    except:
        print("Could not open", filename)
    else:
        for line in file:
            new_set.add(line.strip())
        file.close()
        return new_set

def print_set (name, this_set):
    print(name)
    print('-----------------------')
    for element in this_set:
        print(element)
    print()
    

it244_ids = set_create_from_file('it244_ids.txt')
it341_ids = set_create_from_file('it341_ids.txt')
print_set('it244_ids.txt', it244_ids)
print_set('it341_ids.txt', it341_ids)

print_set('it244_ids.difference(it341_ids.txt)', it244_ids.difference(it341_ids))
print_set('it341_ids.difference(it244_ids.txt)', it341_ids.difference(it244_ids))

print_set('it244_ids.intersection(it341_ids.txt)', it244_ids.intersection(it341_ids))
print_set('it341_ids.intersection(it244_ids.txt)', it341_ids.intersection(it244_ids))