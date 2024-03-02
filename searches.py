from discs import *
import os

def company_search(company):
    #clears screen
    os.system('cls')
    #checks if a company argument was added when company search was called
    if company == None:
        prompt = "Please select from your list of companies:"
        #Prints out a list of companies that you have discs from
        print('{}\n{}'.format(prompt, len(prompt) * '-'))
        for comp in Disc.company_list:
            print(comp.upper())
        company = input().lower()
    #checks if user inputed a valid value
    if company.lower() not in Disc.company_list:
        print('Please select a company within your list of companies')
        input()
        company_search(None)
        return
    os.system('cls')
    #Searches all discs list for objects that meet the search criteria
    print(f'Here are all the discs you own from {company.capitalize()}')
    search(company, 'company')

flight_numbers = ['Speed','Glide','Turn','Fade']
def flight_search(args):
    os.system('cls')
    #checks if an argument was added when function was called
    if args == None:
        prompt = "Please select which flight number you would like to search by:"
        print('{}\n{}'.format(prompt, len(prompt) * '-'))
        for value in flight_numbers:
            print(value)
        args = input()
    args = str(args)
    #Checks if 2 search conditions were provided
    try:    
        number, value = args.split(' ')
        number = number.lower()
        value = int(value)
    except:
        print('Please type in your search term in the form of "flight_number value"')
        input()
        flight_search(None)
        return
    os.system('cls')
    #Prints discs that meet search conditions
    print(f'Here are all the discs you own with {number.capitalize()} {value}')
    search(value, number)

color_list = ['red', 'orange', 'blue', 'yellow', 'green', 'purple', 'clear', 'black', 'pink', 'brown', 'white', 'grey', 'glo']
def color_search(color):
    os.system('cls')
    #checks if an argument was added when function was called
    if color == None:
        prompt = "Please select from the list of colors:"
        print('{}\n{}'.format(prompt, len(prompt) * '-'))
        for _color in color_list:
            print(_color.capitalize())
        color = input()
    color = color.lower()
    #checks if search term was formatted correctly
    if color not in color_list:
        print('Please select a color from above')
        input()
        color_search(None)
        return
    os.system('cls')
    #displays results based on search criteria
    print(f'Here are all the your discs that are {color}')
    search(color, 'color')

def type_search(_type):
    os.system('cls')
    #checks if an argument was added when function was called
    if _type == None:
        prompt = "Please select from the list of types:"
        print('{}\n{}'.format(prompt, len(prompt) * '-'))
        for _types in Disc.TYPES:
            print(Disc.TYPES[_types].upper())
        _type = input()
    _type = _type.lower()
    #checks if search term was formatted correctly
    if _type not in Disc.TYPES.values():
        print('Please select a type from the list above')
        input()
        type_search(None)
        return
    os.system('cls')
    #displays discs based on search criteria
    print(f'Here are all the {_type.capitalize()}\'s you have')
    search(_type, '_type')

#Searches through all discs for objects that posesses a desired attribute
def search(key, atribute):
    for disc in Disc.all_discs:
        if getattr(disc, atribute) == key:
            print(f'{disc.name.upper()} {disc.flight_nums} {disc.color.capitalize()}')
    #Allows the user to see the displayed results before going back to the home menu
    input('Press enter to continue')