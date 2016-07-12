"""
Prints out all the melons in our inventory
"""

from melons import melon_info


# def print_melon():
#     for melon, value in melon_info.items():
#         print melon
#         for attribute, value in attributes.items():
#             print "{}: {}".format(attribute, value)
#         print

# print_melon()

def print_melon():  #define function print_melon
    for melon, value in melon_info.items():  #for each 'melon, value' tuple in dictionary melon_info
        print melon  #print to console melon
        for value, value2 in value.items():  #and then for each "key, value" within each melon dictionary
            print "{}: {}".format(value, value2) #print key, value
        print  #add a new line?

print_melon()

# key and value can be named anything
