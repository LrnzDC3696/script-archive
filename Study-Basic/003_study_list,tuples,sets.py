"""Link to the source https://youtu.be/W8KRzm-HUcc"""

print('LISTS')
print('Lists are mutable so it can be changed')
LISTS = []
LISTS = list()

BODY = ['head','shoulders','knees','toes']
print(len(BODY))
print(BODY)

#to access a specific value (it always starts at 0)
print(BODY[0])
print(BODY[-1])

#assumes that from start
print(BODY[:2])
print(BODY[:1])

#assumes that until to last
print(BODY[2:])
print(BODY[3:])
print()

print('Adding value to lists using append()')
FRUITS = ['apple','banana','mango','orange']
FRUITS.append('maple')
print(FRUITS)
print()

print('Adding value to lists using insert()')
PLACES = ['KOREA','AMERICA', 'CHINA', 'RUSSIA']
PLACES.insert(2, 'JAPAN')
print(PLACES)
print()

print('the difference between the two add methods is that append adds it at the end while insert adds at the chosen index')



print('Combining two lists using extend()')
LIST_1 = ['hamburger','sausage','fries']
LIST_2 = ['egg','orange juice','fried rice']
LIST_1.extend(LIST_2)
print(LIST_1)
print()



print('Removing value from a list using remove()')
LIST_1.remove('egg')
LIST_2.remove('fried rice')
print(LIST_1)
print(LIST_2)

print('Removing value from a list using pop()')
LIST_1.pop()
REMOVED = LIST_2.pop()
print(LIST_1)
print(LIST_2)
print(REMOVED)
print()

print('the difference here is that, remove() needs what you want to delete while pop() removes the last one and returns it')
print()


print('Reversing list using reverse()')
NUMBER = [10,9,87,69,4,21]
NUMBER.reverse()
print(NUMBER)

print('Sorting lost values using sort()')
print(NUMBER)
NUMBER.sort()
print(NUMBER)
NUMBER.sort(reverse=True)
print(NUMBER)

print('Sorting lost values using sorted()')
print(FRUITS)
print(sorted(FRUITS))

print('the difference here is that sorted() returns a sorted list while sort() does not')

print('I got tired and did not put the other methods')


print('Turning a list into a string using join()')
TEST = ['SCIENCE', 'MATH', 'AGRICULTURE']
TSET = ', '.join(TEST)
print(TSET)
print()

print('Turning a string into a list using split()')
print(TSET.split(', '))
print('\n')




print('TUPLES')
print('Tuples are immutable so they can\'t be changed')
TUPLES = ()
TUPLES = tuple()

print('Most methods of list can\'t be used in tuples')
TUP = ('1', '2', '3', '4', '5')
print(TUP)

print(TUP.count('1'))
print(TUP.index('5'))





print('SETS ')
print('Sets are unordered and have no duplicate values')
SETS = set()

NEW_SET = {'no', 'yes', 'maybe', 'yes'}
OLD_SET = {'sure', 'probably', 'no'}

print('Checking the similarity of two sets')
print(NEW_SET.intersection(OLD_SET))

print('Checking the difference of two sets')
print(NEW_SET.difference(OLD_SET))

print('Combining two sets')
print(NEW_SET.union(OLD_SET))
