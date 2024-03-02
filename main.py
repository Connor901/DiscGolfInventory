from discs import Disc
from searches import *
from inven_manip import *
import os

build_inventory()
function_dict = {
                'flight numbers':flight_search, 
                'company':company_search, 
                'color':color_search,
                'type':type_search,
                'buy':buy,
                'sell':sell,
                'count':total_count,
                'quit':quit
                }
open = True
prompt = 'Welcome to your Disc Inventory, What would you like to do?'
function_list = [key.upper() for key in function_dict.keys()]

while open:
    os.system('cls')
    #prints starting screen
    print('{}\n{}'.format(prompt, '-' * len(prompt)))
    print('Search By:')
    for count, fun in enumerate(function_list):
        if count > 3:
            print(f'{fun}:')
        else:
            print(f'    {fun}')
    #checks if an argument was provided when calling a function
    request = input().lower().split(':',maxsplit=1)
    if len(request) == 1:
        args = None
    else:
        args = request[1]
    #Calls the requested function
    if request[0] in function_dict:
        function_dict[request[0]](args)