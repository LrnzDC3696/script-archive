'''
This is a my password manager using dictionaries password_manager 1.0
I would also like to thank the people in
python community discord server (https://discord.gg/python) and
tortoise community server (https://discord.gg/7jQzu7BN3H) who helped me ssolve some problems
'''

def start():
    while True:
        print('\nWhat do you want to do now?')
        print('1 for adding\n2 for changing\n3 for checking\n4 for deleting\nq for quiting')
        choice = None
        while choice not in ('q', *redirect.keys()):
            choice = input('Your choice: ').lower()
        if choice == 'q':
            break
        redirect.get(choice)(my_info)

def adding(some_dict):
    print('Welcome you are currently adding a new website and password value\n')
    print(f'{list(some_dict.keys())} are the sites that already has passwords')
    site_name = input('Please enter the new website name: ')
    if site_name in some_dict.keys():
        print('that website already has a password\nreturning to start...\n')
        return
    site_password = input('Please enter the new website password: ')
    some_dict.update({site_name:site_password})
    print('The new site and password has been added have fun!')
    return some_dict
    
def changing(some_dict):
    print('Welcome you are currently changing a new website and password value\n')
    print(list(some_dict.keys()))
    site_name = input('Please enter the website name: ')
    if site_name not in some_dict.keys():
        print('that site name is not in our database\nreturning to start.')
        return
    site_password = input('Please enter the new website password: ')
    some_dict.update({site_name:site_password})
    print('You have updated your password!')
    return some_dict
    
def checking(some_dict):
    print('\nWelcome you are currently checking the password of the website values\n')
    print(list(some_dict.keys()))
    site_name = input('Please enter the website name: ')
    if site_name not in some_dict.keys():
        print('that site name is not in our database\nreturning to start.')
        return
    print(f'The password for that site is {some_dict[site_name]}')
    
def deleting(some_dict):
    print('Welcome you are currently deleting a website and password value\n')
    print(f'{list(some_dict.keys())}\nChoose which site do you want to delete')
    site_name = input('Please enter the website name: ')
    if site_name not in some_dict.keys():
        print('that site name is not in our database\nreturning to start.')
        return
    del some_dict[site_name]
    print(f'The website {site_name} has been deleted')
    print(some_dict.keys())



my_info = {
    'google.com':'001password',
    'twitter.com':'002password',
    'discord.com':'003password'
    }

owner = {
    'username':'deirdre',
    'password':'password',
    'email':'example_deirdre@gmail.com'
    }
    
redirect = {
    '1':adding,
    '2':changing,
    '3':checking,
    '4':deleting
    }




if __name__ == '__main__':
    
    print('Welcome to the password manager 0.1\n')
    print('+---------------------------------+')

    while True:
        print('remember to press q to quit')
        
        temp_username = input('please put in your username: ').lower()
        if temp_username == 'q':
            break
        
        temp_password = input('please put in your password: ')
        if temp_password == 'q':
            break
        
        if temp_username == owner['username'] and temp_password == owner['password']:
            print('You have logged in')
            start()
        else:
            print('did not work')
            print('try again\n')
