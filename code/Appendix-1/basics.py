# DATA TYPE AND STRUCTURES

type(1+2)
x = 1; y=2; z=x+y; type(z)
x = 1; y=2; z=x/y; type(z)
x = 1000000; y=2000000; z=x/y; type(z)
x = 1.5; y=2.5; z=x*y; type(z)

my_name = 'kamakshaiah musunuru'
type(my_name)

# tuples

x, y = (1, 2)
print(x, y)

x = (1, 2, 3, 4, 5)
print(x[0])
print(x[1])

# lists

x = list()
type(x) # is a class

list_methods = [func for func in dir(list) if callable(getattr(list, func)) and not func.startswith('__')]
len(list_methods)
print(list_methods)

import random
random.randint(1, 2)
list(range(5))
x = list(range(5))
print(x)

y = [random.randint(1, 2) for i in range(5)]
print(y) 

y = [random.randint(1, 2) for i in range(5)]
print(y)

y = [round(random.random(), 2) for i in range(5)]
print(y)

y = [round(random.random()*100, 2) for i in range(5)]
print(y)

# dictionary

data_dict = dict(a=1, b=[round(random.random()*100, 2) for i in range(5)])
print(data_dict)
print(data_dict.keys())
print(data_dict.items())
print(data_dict.values())

import statistics as sts
list(data_dict.values())
list(data_dict.values())[1]

sts.mean(list(data_dict.values())[1])

# sets

x = set()
type(x) # is a class

education = [random.randint(1, 3) for i in range(10)]
print(education)
educ_factor = ['primary' if education[i] == 1 else 'secondary' if education[i] == 2  else 'higher' for i in range(len(education))]
educ_dict = dict(data=education, levels=set(educ_factor))
print(educ_dict['data'])
print(educ_dict['levels'])

list(educ_dict['levels'])[0]

method_list = [func for func in dir(set) if callable(getattr(set, func)) and not func.startswith("__")]
print(method_list)
len(method_list)

# I/O

a=2
b=3
c=a+b
##print("The Sum of %d and %d is %d" %(a, b, c))
##print('The sum of ' + repr(a) + ' and ' + repr(b) + ' is ' + repr(c))
print(f'The sum of {a} and {b} is {c}') # very useful

import os
os.getcwd() # 'C:\\Program Files\\Python310'
os.chdir('D:\\Miscel')
os.getcwd() # 'D:\\Miscel'
os.listdir()

os.mkdir('pythonwork')
os.listdir()

os.rmdir('pythonwork')
os.listdir()

# FILE MANAGEMENT

file_path = os.path.join('pythonwork', 'test.txt')
print(file_path)

with open(file_path, 'w') as fw:
    for i in range(5):
        fw.write(str(i))
    print('Done')
with open(file_path, 'r') as fr:
    x = fr.read()
    print('Done')
    
print(x)

for i in x:
    int(i)

# csv files 
with open('pythonwork\\gender.csv', 'r') as gf:
    gender = gf.readlines()

print(gender)

for i in gender:
    print(i.replace('\n', ''))

with open('pythonwork\\gender.csv', 'r') as gf:
    data = gf.readlines()

print(data)

for i in data:
    a, b = i.split(',')
    j.append(a)
    k.append(b)
    print('Done')

print(j)

k_ = []
for i in k:
    k_.append(i.replace('\n', ''))
    
print(k_)

c = 0; d = 0
for i in j:
    if i == 'male':
        c = c + 1
    else:
        d = d + 1

print(c, d)
print('gender: ' + repr(c) + ', ' + 'age: ' + repr(d))

# FUNCTIONS

# SEE THE OTHER MODUEL FUNCTIONS.PY
