"""A module to support password_manager"""
import os
import json
import hashlib

from time import sleep
from cryptography.fernet import Fernet

def printify(words=''):
    """Print but better"""
    for letter in words:
        print(letter, end='', flush=True)
        sleep(0.01)
    print()

def clear(last_words='', time=0, stop=True):
    """clears the console"""
    printify(last_words)
    if stop:
        input()
    sleep(time)
    os.system('clear')


def read_file(database):
    """Reads the file then returns it"""
    with open(database) as file:
        info = json.load(file)
        return info
    
def write_file(database, written):
    """Edits the file then saves it"""
    with open(database, 'w') as file:
        json.dump(written, file, indent=2, sort_keys=True)


def hashed(unhashed):
    """hashes the data and returns it"""
    return hashlib.sha256(str.encode(unhashed)).hexdigest()

def get_key(filename):
    temp_data = read_file(filename)
    key = bytes(temp_data['owner_data']['key'], 'utf8')
    return Fernet(key)
   
def encrypts(filename, plain_text_string):
    """encrypts the unencrypted data"""
    crypto = get_key(filename)
    
    string = crypto.encrypt(bytes(plain_text_string, 'utf8'))
    return str(string, 'utf8')
    
def decrypts(filename, encrypted_string):
    """decrypts the encrypted data"""
    crypto = get_key(filename)
    
    decrypt_value = crypto.decrypt(bytes(encrypted_string, 'utf8'))
    return str(decrypt_value, 'utf8')
