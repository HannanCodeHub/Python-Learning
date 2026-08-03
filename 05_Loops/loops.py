#WHILE-LOOP

count = 1;
while count <= 10:
    print("hello!" , count)
    count += 1

#print numbers from 1 to 5 :
i =1
while i <= 5:

    print(i)
    i += 1

print("loop ended.")

#print numbers from 5 to 1 :
i =5 #iterator.
while i >= 1 :

    print(i)
    i -= 1  #iteration.

print("loop ended.")

#Print numbers from 1 to 100:

i = 1 
while i <= 100:
    print(i)
    i += 1 

print("program ended.")


#Print numbers from 100 to 1:

i = 100 #starting condition
while i >= 1: #stopping condition
    print(i)
    i -= 1

print("Program ended.")

#Print the multiplication table of a number n.

n =  int(input('enter number:'))
i = 1
while i <= 10:
    print( n * i)
    i += 1
    
#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0 
while idx < len(nums):
    print (nums[idx])
    idx += 1

#print the name of heroe's: 

heroes = ['hannan ahmed', "sharukh khan" , 'salman khan']
idx = 0 
while idx < len(heroes):
    print (heroes[idx])
    idx += 1

#Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

# x = 49
x = int(input("enter a number:"))
i = 0
while i < len(nums):
    if (nums[i] == x):
        print( x, "FOUNDED AT INDEX:", i)
    i += 1

else:
        print("not found.")

#Break & Continue:

#Break:

i = 1
while i <= 5:
    print(i)
    if (i == 3):
        break 
    i += 1 

print("end of loop.")

#continue:

i = 1
while i <= 5:
    if (i == 3):
        i += 1
        continue  #skip 
    print(i)
    i += 1 

print("end of loop.")

#FOR LOOP:
nums = [1,2,3,4,5,6,7]

for val in nums:
    print (val)

str = "hannanAhmed"

for char in str:
    if(char == 'm'):
        print("char m founded.")
        break
    print (char)
else:
    print("end")

#Print the elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

elements = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for val in elements : 
    print(val)

#Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81,100,49)

x = 49
idx = 0

for el in num :
    if (el == x ):
        print("number found at idx:" ,idx )
        break
    idx +=1


#Range: (start, stop , step)
seq = range(5)
for i in seq:
    print(i)

for i in range(10): #range(stop)
    print(i)

for i in range(2,10): #range(start ,stop)
    print(i)

for i in range(2,10,2): #range(start, stop , stepsize)
    print(i)

#print even numbers:
for i in range(2,101,2):
    print(i)

#Print numbers from 1 to 100.
for i in range(1 , 101):
    print(i)

#Print numbers from 100 to 1.
for i in range(100, 0 , -1):
    print(i)

#Print the multiplication table of a number n:
n = int(input("enter a number:"))

for i in range(1,11):
    print(n*i)

# for i in range(3,33, +3):
#    print(i)

#PASS STATEMENT :
for i in range(5):
    pass

print("some useful work.")

#WAP to find the sum of first n numbers. (using while)
n = int(input("Enter a number: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Sum of first", n, "numbers =", sum)

#WAP to find the factorial of first n numbers. (using for)
n = 5 
f = 1 
for i in range ( 1, n +1 ):
    f *= i 

print ( "factorial of 5 is :" , f)
