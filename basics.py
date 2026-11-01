# Python basics — run this file: python basics.py

# 1) Print and comments
# A line starting with # is a comment. print() shows text on the screen.
print("Hello, Python!")


# 2) Variables
# A variable is a name that stores a value. You do not declare a type.
name = "Swathi"
age = 21
height = 5.6
is_student = True

print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))


# 3) Strings
greeting = "Hello"
full = greeting + " " + name  # concatenation
print(full)
print(name.upper())           # SWATHI
print(name.lower())           # swathi
print(len(name))              # number of characters
print(f"{name} is {age} years old")  # f-string: insert values into text


# 4) Numbers
a = 10
b = 3
print(a + b)   # 13  add
print(a - b)   # 7   subtract
print(a * b)   # 30  multiply
print(a / b)   # 3.333...  division (always float)
print(a // b)  # 3   integer division
print(a % b)   # 1   remainder
print(a ** b)  # 1000  power (10^3)


# 5) Lists (ordered, changeable)
fruits = ["apple", "banana", "mango"]
print(fruits[0])       # first item: apple
print(fruits[-1])      # last item: mango
fruits.append("orange")
print(fruits)
print(len(fruits))


# 6) Tuples (ordered, not changeable)
point = (10, 20)
print(point[0])


# 7) Dictionaries (key -> value)
person = {
    "name": "Swathi",
    "city": "Hyderabad",
    "age": 21,
}
print(person["name"])
print(person.get("city"))
person["age"] = 22
print(person)


# 8) Sets (unique values, unordered)
colors = {"red", "blue", "red"}
print(colors)  # red appears only once


# 9) If / elif / else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")


# 10) Loops
for fruit in fruits:
    print("I like", fruit)

for i in range(3):  # 0, 1, 2
    print("count:", i)

n = 0
while n < 3:
    print("while:", n)
    n = n + 1


# 11) Functions
def add(x, y):
    return x + y

def greet(who="friend"):
    return f"Hi, {who}!"

print(add(2, 5))
print(greet(name))
print(greet())


# 12) Input (uncomment to try)
# user_name = input("What is your name? ")
# print("Nice to meet you,", user_name)


# Quick cheat sheet
# int     -> whole number: 1, 20
# float   -> decimal: 3.14
# str     -> text: "hello"
# bool    -> True / False
# list    -> [1, 2, 3]
# tuple   -> (1, 2)
# dict    -> {"key": "value"}
# set     -> {1, 2, 3}
# None    -> no value
