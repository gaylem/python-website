# Data Types

# Int
576894
12
-1
-9834837
# No decimal point

# Float - any number with decimal
2727.0
2.2
-9.7

# String - quotes (seq of characters or nums)
'Hello'
"hello"
"'hello'"

# Bool
True
False 

# Output printing

print('print me')
print(4.5, 'hello')
print(4.5, 'hello', end='|')
print(4.5, 'hello', end='\n')
print(4.5, 'hello')

# Variable
hello = 'tim'
world = 'word'
world = hello
hello = 'no'

print(hello, world) # no tim

hello_world = 'hello world'
# don't start with numbers or leave spaces
# snake case

# user input
name = input('Name: ')
print(name)
age = input('Age: ')
print('Hello', name, 'you are', age, 'years old')

#Arithmetic Operator
x = 9
y = 3.5
result = x + y # - * / 
print(result)
# division returns a float regardless of whether the original numbers were int
# can convert to int with int()

a = 10
b = 3
result_two = a // b # 3 (integer result, removes decimal points)

c = 10
d = 3
result_three = c ** d # exponent

result_four = x % y # like modulo in JS

# Order of operations = BEDMAS (Brackets, Exp, Division, Mult, Addition, subtraction)

num = input ('Number: ') # turns what we type in to a string
print(int(num - 5)) 
print(float(num - 5)) # if there is one float you will get a float result

# String methods
hello = 'hellO'.upper() # makes string uppercase
print(type(hello)) # <class 'str'>
# .capitalize() makes first letter of each word capitalize
print(hello.lower().count('o')) #count is case sensitive, returns 1

x = 'hello'
y = '3'

print(x + y) # hellohellohello 

# Conditional Operators
# == , != , > , < 
# Can use greater than and less than to compare strings ('a' > 'Z' == True) due to ASCII

# Chained Conditionals

x = 7
y = 8
z = 0

result1 = x == y
result2= y > x
result3 = z < x + 2

# not, and, or (in order of operations)
result4 = result1 or not result2 or result3
print(result4)
# not flips the result, like bang operator

# If/Else/Elif
name = input('Name: ')
if name == 'Tim' or 'tim':
  print('You are great,', name)
elif name == 'Joe' or 'joe':
  print('Bye, ', name)
else: 
  print('No')

# Collection (unordered or ordered group of elements)

# List
x = [4, True, 'hi']
print(len(x)) # 3
x.append('hello')
x.extend([4, 5, 5, 5, 5, 6])
x.pop()
# Lists are mutable, can change individual elements with bracket notation just like JS
y = x # references x but does not create a copy
y = x[:] # creates a copy

# Tuples - immutable
x = (0,0,2,2)
print(x[0])
x[0] = 5 # won't work, neither will methods
# you can have lists in lists, tuples in lists

# for loop
for i in range(10): # creates collection of nums based on input, 10 is ending range (does not include/print 10)
  print(i)
# start, stop, step 

x = [3, 4, 5, 6]
for i in range(len(x)):
  print(x[i])

for i, element in enumerate(x):
  print(i, element)

# while loops
i = 0
while i < 10:
  print('run')
  i += 1

# slice operator 

x = [0, 1, 2, 3, 4, 5, 6]
y = ['hi', 'hello', 'goodbye']
s = "hello"
#sliced = x[start:stop:step]
sliced = x[0:4:2]
sliced = s[::-1] # reverse a list or string
sliced = x[::2] # hlo
# works on tuples
print(sliced)

# Sets
# All we care about is if something is there or not there
# Fast lookups, removals, additions

x = set()
s = {4, 32, 2, 2}
# x = {} creates a dictionary
print(type({}))
print(s)
s.add(5) # adds to end
s.remove(5)
print(4 in s) # checks if el is in set, returns true or false
s2 = [4, 32, 2, 2]
print(5 in s2) # this will take longer bc its a list
# union, difference, intersection 

# Dictionaries (Hash table or map)

x = {'key': [1, 2, 3]}
print(x['key'])

x['key2'] = 5
x[2] = 8
print('key' in x)
print(list(x.values()))

del x['key'] #delete

for key, value in x.items():
  print(key, value)

# Comprehension 
x = [x for x in range(5)] # for loop
print(x) # [0, 1, 2, 3, 4]

y = [i for i in range(100) if i % 5 == 0] # returns list with all increments of 5
z = {i:0 for i in range(100) if i % 5 == 0} # dictionary
a = {i for i in range(100) if i % 5 == 0} # set
b = tuple(i for i in range(100) if i % 5 == 0) # tuple

# Functions
def func():
  print('run')
  def func2():
      print('hi')

# Functions are objects so you can return them
      
def func3(x, y):
  print('run', x, y)

print(func3(5, 6))

def func4(x, y, z=None):
  return x * y, x / y # returns value as tuple

r1, r2 = func(5, 6, 7)

# Unpack Operator

def func(x):
  def func2():
    print(x)

  return func2

func(3)() # closure, calls internal function

# *args and **kwargs

def func(*args, **kwargs):
  pass

x = [1, 233, 34343, 666]
print(*x) # unpacks whats in tuple or list and prints without commas or brackets
print(x) # prints out the tuple or list

def func(x, y):
  print(x, y)

pairs = [(1, 2), (3, 4)]
for pair in pairs:
  func(*pair)

# dictionaries
for pair in pairs:
  func(**{'x': 2, 'y': 5})

def func(*args, **kwargs): # kwargs stands for keyword arguments
  print(args, kwargs) # pass in unlimited amount of arguments and keyword arguments

func(1, 2, 3, 4, one=0, two=1)
# {1, 2, 3, 4} {'one': 0, 'two':1}

# Scope and globals
x = 'tim'

def func(name):
  global x
  x = name

# tim won't change without global, never use this
  
# Exceptions

raise Exception('Bad') 
raise FileExistsError('Boo!')

# Try / Except Block
try:
  x = 7 / 0
except Exception as e:
  print(e)
finally: # will run no matter what
  print('finally')

# Lambda - one line anonymous func
x = lambda x: x + 5
x(2) # 7

x = [1, 3, 4, 4, 5, 7, 8]

mp = map(lambda i: i + 2, x)
print(list(mp))

mp2 = filter(lambda i: i % 2 == 0, x) # returns true or false if element is even and returns list with only truthy vals

# f strings (new in python 3.6) - like template literals
tim = 89
x = f'hello {6 + 8} {tim}'
x = F'hello {7 + 10}'

















