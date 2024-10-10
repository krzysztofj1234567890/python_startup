# https://www.geeksforgeeks.org/advanced-python-tutorials/

print("========== List Comprehension ==========")

print( "----- 1") 
numbers = [12, 13, 14,] 
doubled = [x *2  for x in numbers] 
print(doubled)

print( "----- 2")
List = [character for character in [1, 2, 3]] 
print(List)

print( "----- range")
matrix = [ [j for j in range(5)] for i in range(3)]    
print(matrix)

print( "========== Python Dictionary Comprehension ==========")

print( "----- 1" )
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
myDict = { k:v for (k,v) in zip(keys, values)}  
print (myDict)

print( "========== Python lambda ==========")

print( "----- even number")
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

print( "----- 2")
ala = lambda val: True if val%2 == 0 else False
print( ala(13))

print( "----- filter out digits")
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

print( "----- not equal a")
kj1 = lambda val: ''.join( [ch for ch in val if ch !='a'])
print( kj1('abcd'))

print( "----- sort")
l = ["1", "2", "9", "0", "-1", "-2"]
print("Sorted numerically:", sorted(l, key=lambda x: int(x)))

print( "----- filter out positive numbers")
print("Filtered positive even numbers:", list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

print( "----- lambda and map")
print("Operation on each item using lambda and map()", list(map(lambda x: str(int(x) + 10), l)))

print( "========== filter() in python ==========")
print( "----- Python Filter Function with a Custom Function")
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)
print('The filtered letters are:')
for s in filtered:
    print(s)

print( "----- Python Filter Function with a lambda")
seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

print( "========== reduce() in python ==========")
print( "-----  apply a particular function passed in its argument to all of the list elements")
import functools

lis = [1, 3, 5, 6, 2]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print( "----- calculates the sum of a and b")
def my_add(a, b):
    result = a + b
    return result
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6 ]
print( reduce(my_add, numbers))

print( "----- multiply all numbers")
print( reduce(lambda a, b: a * b, numbers) )

print( "========== map() in python ==========")
print( "----- map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable")
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

print( "----- Add two lists using map and lambda" ) 
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

print( "----- Add t3wo lists using map and lambda" ) 
numbers3 = [7, 8, 9]
result = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
print(list(result))

print( "========== Classes and objects ==========")

print( "----- Person class" ) 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
print(p1.name)
print(p1.age) 
print( p1 ) 
p1.myfunc()

print( "----- Inheritance" ) 
class Student(Person):
  def __init__(self, name, age, year):
    super().__init__(name, age)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.name, self.age, "to the class of", self.graduationyear) 
x = Student("Mike", 23, 2019)
x.welcome()

print( "========== Json ==========")
print( "----- Parse JSON - Convert from JSON to Python")
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"]) 

print( "----- Convert from Python to JSON")
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y) 

print( "----- nested json")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

print( "========== Exceptions ==========")
print( "----- try except else finally")
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 

