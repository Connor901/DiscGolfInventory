from discs import Disc
import sys
import pandas
import os

#takes a csv with disc info and converts it into Disc objects
def build_inventory():
    discs = pandas.read_csv('inventory.csv')
    for i in range(len(discs)):
        row = discs.iloc[i]
        Disc(row['Company'], row['Name'], int(row['Speed']), int(row['Glide']), int(row['Turn']), int(row['Fade']), row['Color'])

def buy(*arg):
    os.system('cls')
    new_disc = input('Input your new disc in this format\nCompany,Name,Speed,Glide,Turn,Fade,Color\n{}\n'.format('-' * 40))
    try:
        info = new_disc.split(',')
        info = [attribute.lower() for attribute in info]
        #sets flight numbers to integers for disc.type to work
        info[2:6] = map(int, info[2:6])
        Disc(*info)
    except:
        print('Please input your disc as in the format above')
        input('Press enter to continue')
        buy(None)
    update_inventory()

disc_attributes = ['company', 'name', 'speed', 'glide', 'turn', 'fade', 'color']
def sell(*args):
    os.system('cls')
    sell_disc = input('Input the disc you would like to sell in this format\nCompany,Name,Speed,Glide,Turn,Fade,Color\n{}\n'.format('-' * 40))
    sell_disc = sell_disc.split(',')
    sell_disc = [data.lower() for data in sell_disc]
    #converts flight numbers to ints
    sell_disc[2:6] = map(int, sell_disc[2:6])
    try:
        #goes through each disc
        for disc in Disc.all_discs:
            try:
                #checks the attribute of the disc against the request
                for index, attribute in enumerate(disc_attributes):
                    #if it doesnt match, raises an error and moves on to the next disc 
                    if getattr(disc, attribute) != sell_disc[index]:
                        raise('Not the right disc')  
                #if it passes all of the attribute checks it removes it from all_discs and updates the csv file
                Disc.all_discs.remove(disc)
                update_inventory()
                print('Disc has been sold')
                input('Press enter to continue')
                return
            except:
                continue
        input('That Disc was not found in your inventory')
        return
    except:
        print('Please input your disc as in the format above')
        input('Press enter to continue')
        sell(None)

def quit(*args):
    os.system('cls')
    sys.exit()

def update_inventory():
    discs_dict = {'Company':[], 'Name':[], 'Speed':[], 'Glide':[], 'Turn':[], 'Fade':[], 'Color':[]}
    #takes all of the discs and throws the attributes into a dictionary that can be turned into a csv file
    for disc in Disc.all_discs:
        discs_dict['Company'].append(disc.company)
        discs_dict['Name'].append(disc.name)
        discs_dict['Speed'].append(disc.speed)
        discs_dict['Glide'].append(disc.glide)
        discs_dict['Turn'].append(disc.turn)
        discs_dict['Fade'].append(disc.fade)
        discs_dict['Color'].append(disc.color)
    disc_csv = pandas.DataFrame(discs_dict)
    disc_csv.to_csv('inventory.csv')

def total_count(*args):
    os.system('cls')
    print(f'You have {Disc.total} discs in your inventory')
    input('Press enter to continue')