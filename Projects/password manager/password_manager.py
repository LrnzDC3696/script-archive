'''
This is a my password manager using dictionaries password_manager
I would also like to thank the people in
python community discord server (https://discord.gg/python) and
tortoise community server (https://discord.gg/7jQzu7BN3H) who helped me ssolve some problems

APPLIED:
    loops
    functions
    dictionary
    json files
    EAFP (Easier to Ask Forgiveness than Permission)
'''
from getpass import getpass
from my_manager import *

def new_user(database):
    """Will be called if the file does not exist or it's empty"""
    printify('It seems you are a new user!')
    
    while True:
        printify('remember to press q to quit\nPlease fill the following with your correct info\n')
        printify('Email: ')
        email = input()
        if email == 'q':
            return
        
        printify('Chosen username: ')
        username = input()
        if username == 'q':
            return
        
        printify('Chosen password: ')
        password = getpass('')
        if password == 'q':
            return
        
        printify('Your chosen password again: ')
        temp_passw = getpass('')
        if temp_passw == 'q':
            return
            
        if temp_passw == password:
            printify('You have succestully created your account')
            clear()
            break
        printify('Sorry there was an error with your password please try again\n')
    
    password = hashed(password)
    key = str(Fernet.generate_key(), 'utf8')
    the_json = {
        'owner_data':
            {'username':username,'password':password,'email':email,'key':key},
        'sites':
            {}
        }
        
    write_file(database, the_json)
    clear('Press enter to continue')
    start(DATA_BASE)

def start(filename):
    """The code stars here"""
    while True:
        printify('\nWhat do you want to do now?')
        printify('1 for adding\n2 for changing\n3 for checking\n4 for deleting\nq for quiting')
        choice = None
        
        while choice not in ('q', *REDIRECT.keys()):
            choice = input('Your choice: ').lower()
        if choice == 'q':
            break
        
        clear(stop=False)
        REDIRECT.get(choice)(filename)

def adding(filename):
    """Adds the given info to the json file"""
    printify('Welcome you are currently adding a new website and password value\n')
    temp_data = read_file(filename)
    
    printify(f'{list(temp_data["sites"].keys())} are the sites that already has passwords\n')
    printify('Please enter your chosen website name: ')
    site_name = input()
    if site_name in temp_data['sites'].keys():
        printify('that website already has a password\nreturning to start...\n')
        return
    printify('Please enter the new website password: ')
    site_password = getpass('')
    temp_data['sites'].update({site_name: encrypts(filename, site_password)})
    write_file(filename, temp_data)
    clear('The new site and password has been added have fun!\nPress enter to continue')
    
def changing(filename):
    """Changes the password"""
    printify('Welcome you are currently changing a new website and password value\n')
    temp_data = read_file(filename)
    printify(list(temp_data['sites'].keys()))
    site_name = input('Please enter the website name: ')
    if site_name not in temp_data['sites'].keys():
        printify('that site name is not in our database\nreturning to start.')
        return
    printify('Please enter the new website password: ')
    site_password = getpass('')
    temp_data['sites'].update({site_name:encrypts(filename,site_password)})
    clear('You have updated your password!\nPress enter to continue')
    
def checking(filename):
    """Used to checking the password for some website"""
    printify('Welcome you are currently checking the password of the website values\n')
    temp_data = read_file(filename)
    printify(list(temp_data['sites'].keys()))
    printify('Please enter the website name: ')
    site_name = input()
    if site_name not in temp_data['sites'].keys():
        printify('that site name is not in our database\nreturning to start.')
        return
    printify(f'The password for that site is {decrypts(filename, temp_data["sites"][site_name])}')
    clear('Press enter to continue')
    
def deleting(filename):
    """Deletes the website"""
    printify('Welcome you are currently deleting a website and password value\n')
    temp_data = read_file(filename)
    printify(f'{list(temp_data["sites"].keys())} please choose what website do you want to delete')
    site_name = input('Please enter the website name: ')
    if site_name not in temp_data["sites"].keys():
        printify('that site name is not in our database\nreturning to start.')
        return
    del temp_data["sites"][site_name]
    write_file(filename, temp_data)
    clear(f'The website {site_name} has been deleted\nPress enter to continue')


REDIRECT = {
    '1':adding,
    '2':changing,
    '3':checking,
    '4':deleting
    }
    
DATA_BASE = 'information.json'
VERSION = '2.0.9'


if __name__ == '__main__':
    printify(f'Welcome to the password manager version:{VERSION}\n')
    printify('+-----------------------------------------+')
    
    try:
        with open(DATA_BASE) as f:
            try:
                data = json.load(f)
                del data
            except json.decoder.JSONDecodeError:
                new_user(DATA_BASE)
    except FileNotFoundError:
        new_user(DATA_BASE)
    
    try:
        user_json = read_file(DATA_BASE)
        owner = user_json['owner_data']
    except FileNotFoundError:
        new_user(DATA_BASE)

    while True:
        printify('remember to press q to quit\nYou are currently logging in:')
        printify('Your username:')
        temp_username = input().lower()
        if temp_username == 'q':
            break
                           
        printify('Your password: ')
        temp_password = getpass()
        if temp_password == 'q':
            break
        
        if temp_username == owner['username'] and hashed(temp_password) == owner['password']:
            clear('You have logget in !!!\nPress Enter to continue')
            start(DATA_BASE)
            break
        printify('Log In Failed please try again\n')
