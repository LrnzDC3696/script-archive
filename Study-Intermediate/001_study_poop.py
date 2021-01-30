"""Studying Class n Objects source: https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc"""

"""This is a class. Class is like the blueprint of something"""
class Pet:
    
    """This is a class variable"""
    number_of_cat = 0
    food = 19
    
    """This is a contructor"""
    def __init__(self, name, animal, love = 0, is_sleeping = False, hunger=55):
        
        """this is a instance variables"""
        self.name = name
        self.animal = animal
        self.love = love
        self.is_sleeping = is_sleeping
        self.hunger = hunger
        
        Pet.number_of_cat += 1
    
    """This is a instance method"""
    def beautify(self):
        print('I feel loved')
        self.love += 100
        print(self.love)
    
    """This is a classmethod"""
    @classmethod
    def add_food(cls, amount):
        cls.food += amount
    
    """Using classmethod as alternative constructor"""
    @classmethod
    def from_string(cls, cat):
        name, animal, love = cat.split('-')
        return cls(name, animal, love)
        
    """This is a static method we don't pass cls or self we only use it if it has logical connection to the class"""
    @staticmethod
    def is_bathing_day(day):
        return day.weekday() == 5

class Person:
    def __init__(self, name, age, pet=None):
        self.name = name
        self.age = age
        self.pet = pet

    def feed_pet(self):
        self.pet.hunger += Pet.food
        print(f'Pet {self.pet.name} has been feeden and now has hunger of {self.pet.hunger}')

"""PETS ARE HERE"""
Animal3 = Pet('doge','dog',3,True)
Animal2 = Pet('Kate','cat',7)
Animal1 = Pet('torty','tortoise',2,False)

"""PEOPLE ARE HERE"""
Human1 = Person('xZlain',100, Animal1)
Human2 = Person('Drei',50, Animal2)

"""PRINTING INSTANCE VARIABLES"""
print(Human1.name, Human1.age, Human1.pet.name)
print(Human2.name, Human2.age, Human2.pet.name)

"""USING INSTANCE METHODS"""
print(Human1.pet.name)
Human1.pet.beautify()
Human1.feed_pet()

"""USING THE CLASSMETHOD"""
Pet.add_food(44)
new_pet1 = Pet.from_string('Chan-Bird-0')

"""USING STATIC METHOD"""
import datetime
my_day = datetime.datetime.now()
print(Pet.is_bathing_day(my_day))
