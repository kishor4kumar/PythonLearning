print("Hello World!\nWelcome to Python")


a = 5
print("a =", 5)
a = "High five"
print("a =", a)

#arithmatic operations
x = 14
y = 4

# Add two operands
print('x + y =', x+y) # Output: x + y = 18

# Subtract right operand from the left
print('x - y =', x-y) # Output: x - y = 10

# Multiply two operands
print('x * y =', x*y) # Output: x * y = 56

# Divide left operand by the right one 
print('x / y =', x/y) # Output: x / y = 3.5

# Floor division (quotient)
print('x // y =', x//y) # Output: x // y = 3

# Remainder of the division of left operand by the right
print('x % y =', x%y) # Output: x % y = 2

# Left operand raised to the power of right (x^y)
print('x ** y =', x**y) # Output: x ** y = 38416

x = 5
# x += 5 ----> x = x + 5
x +=5
print(x) # Output: 10

# x /= 5 ----> x = x / 5
x /= 5
print(x) # Output: 2.0

#Get Input from User
# inputString = input('Enter a sentence:')
# print('The inputted string is:', inputString)


#Python Comments
# This is a comment
"""This is a 
    multiline
    comment."""
'''This is also a
     multiline
     comment.'''

#type conversion
num_int = 123  # integer type
num_flo = 1.23 # float type

num_new = num_int + num_flo

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

num_int = 123     # int type
num_str = "456"   # str type

# print(num_int+num_str) # run time error TypeError: unsupported operand type(s) for +: 'int' and 'str'

# explicitly converted to int type
num_str = int(num_str) 

print(num_int+num_str)

#python numeric types
# Output: <class 'int'>
print(type(5))

# Output: <class 'float'>
print(type(5.0))

# <class 'complex'>
c = 5 + 3j
print(type(c))

#python lists

# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed data types
my_list = [1, "Hello", 3.4]

language = ["French", "German", "English", "Polish"]

# Accessing first element
print(language[0])


# Accessing fourth element
print(language[3])

#python tuples - immutable list i.e cannot change values in language
language = ("French", "German", "English", "Polish")
print(language)
#You can access elements of a tuple in a similar way like a list.
print(language[1]) #Output: German
print(language[3]) #Output: Polish
print(language[-1]) # Output: Polish
#You cannot delete elements of a tuple, however, you can entirely delete a tuple itself using del operator.
del language
# NameError: name 'language' is not defined
#print(language)

#STRINGS
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


strval = 'programiz'
print('strval = ', strval)

print('strval[0] = ', strval[0]) # Output: p

print('strval[-1] = ', strval[-1]) # Output: z

#slicing 2nd to 5th character
print('strval[1:5] = ', strval[1:5]) # Output: rogr

#slicing 6th to 2nd last character
print('strval[5:-2] = ', strval[5:-2]) # Output: am

str1 = 'Hello '
str2 ='World!'

# Output: Hello World!
print(str1 + str2)

# Hello Hello Hello
print(str1 * 3)

#Sets
#A set is an unordered collection of items where every element is unique (no duplicates).
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set of integers
my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set) # Output: {1, 2, 3, 4}

my_set.update([3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set) # Output: {1, 2, 3, 5}

A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B) 
# Also equivalent to B.union(A)
print(A | B) # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print (A & B) # Output: {2, 3}

# Set Difference
print (A - B) # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}

#Dictionaries
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

person = {'name':'Jack', 'age': 26, 'salary': 4534.2}
print(person['age']) # Output: 26

person = {'name':'Jack', 'age': 26}

# Changing age to 36
person['age'] = 36 
print(person) # Output: {'name': 'Jack', 'age': 36}

# Adding salary key, value pair
person['salary'] = 4342.4
print(person) # Output: {'name': 'Jack', 'age': 36, 'salary': 4342.4}


# Deleting age
del person['age']
print(person) # Output: {'name': 'Jack', 'salary': 4342.4}

# Deleting entire dictionary
del person

#Range
print(range(1, 10)) # Output: range(1, 10)
numbers = range(1, 6)

print(list(numbers)) # Output: [1, 2, 3, 4, 5]
print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
print(set(numbers)) # Output: {1, 2, 3, 4, 5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99} 
print(dict.fromkeys(numbers, 99))

# Equivalent to: numbers = range(1, 6)
numbers1 = range(1, 6 , 1)
print(list(numbers1)) # Output: [1, 2, 3, 4, 5]

numbers2 = range(1, 6, 2)
print(list(numbers2)) # Output: [1, 3, 5]

numbers3 = range(5, 0, -1)
print(list(numbers3)) # Output: [5, 4, 3, 2, 1]

