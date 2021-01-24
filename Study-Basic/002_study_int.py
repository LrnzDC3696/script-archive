"""Link to the source https://youtu.be/khKv-8q7YmY"""

NUM_1 = 100
NUM_2 = 50.50

print(f'{type(NUM_1)} This is an int because it is a whole number.')
print(f'{type(NUM_2)} This is a float because it has a decimal point.')
print()

print('Arithmetic Operations\n')

#addition
print(1+1)

#subtraction
print(2-2)

#multiplication
print(3*3)


#division
print(4/4)

#floor division
print(5//5)
#the difference here is that / returns a float and // drops the decimal

#exponents
print(6**6)

#modulation
print(8%7)
#this returns the decimal(s)


#things in the parenthesis are calculated first
print(1 * 2 + 3)
print((1*2) + 3)
print(((1*2) + 3) + 5)


#incremation
NUM_3 = 55
NUM_3 += 5
print(NUM_3)



print('\nMethods\n')
#abs method
MSG = 'abs(x) method will return the absolute value of x'
print(abs(-3))
print()

#round method
ROUND_MSG = 'round(x) will return the rounded value of x'
print(round(17.4729))
print(round(1.123456789987654321, 6))
print()

#int method
INT_MSG = 'int(x) will return the int version of x'
print(int("100"))
print()



print('\nComparisons\n')

#is equal
print(1==9)

#is not equal
print(2!=8)

#is greater than
print(33>7)

#is greater than or equal
print(4 >= 92)

#is less than
print(83 < 88)

#is less than or equal
print(82 <= 13)
