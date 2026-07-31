# Variables in Python

name = "Hannan"
age = 22
height = 5.9

print(name)
print(age)
print(height)

# Arithmetic Operators

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Input and Output

name = input("Enter your name: ")
print("Welcome,", name)

# Data Types

name = "Hannan"      # str
age = 22             # int
height = 5.9         # float
is_student = True    # bool

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#print sum of two numbers

num1 = 1000
num2 = 300
sum = num1 + num2

print(sum)

#program to input 2 numbers and put their sum 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2

print("The sum of the two numbers is:", sum)

#program to input 2 floating numbers and print their average
num1 = float(input("Enter first floating number: "))
num2 = float(input("Enter second floating number: "))  

print ("The average of the two floating numbers is:", (num1 + num2) / 2)

#program to input side of a square and print its area

side = float(input("Enter the side of the square: "))
area = side * side 

print("The area of the square is:", area)

#program to input 2 integer numbers, print true if A is greater than B, else print false

a = int( input("Enter first integer number: "))
b = int( input("Enter second integer number: "))

print(a >= b)