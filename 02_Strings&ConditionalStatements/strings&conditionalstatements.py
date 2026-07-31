# Strings + Conditional Statements

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# String methods
name = name.strip()          # Remove extra spaces
print("Original Name:", name)
print("Upper:", name.upper())
print("Lower:", name.lower())
print("Title:", name.title())
print("Length:", len(name))

# String slicing
print("First Character:", name[0])
print("Last Character:", name[-1])
print("First 3 Characters:", name[:3])

# Conditional Statements
if len(name) == 0:
    print("Name cannot be empty!")

elif age < 18:
    print(f"Hello {name.title()}, you are a Minor.")

elif age >= 18 and age < 60:
    print(f"Hello {name.title()}, you are an Adult.")

else:
    print(f"Hello {name.title()}, you are a Senior Citizen.")

# Membership Operator
if "a" in name.lower():
    print("Your name contains the letter 'a'.")
else:
    print("Your name does not contain the letter 'a'.")

# Comparison
if name.lower() == "hannan":
    print("Welcome back, Hannan!")
else:
    print("Nice to meet you!")

# Nested Condition
if age >= 18:
    if len(name) >= 5:
        print("You are eligible and your name has at least 5 characters.")
    else:
        print("You are eligible but your name is short.")

#WAP to input user’s first name & print its length.
name = str(input("enter your name:"))
print (len(name));

#WAP to find the occurrence of ‘$’ in a String.
occurence = "let$$set$this"
print(str.count("$"))

#WAP to check if a number entered by the user is odd or even
num = int(input("enter number to check odd/even :"))
rem = num %2 

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

#WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

if(num1 >= num2 and num1>= num3):
    print("Nummber 1 is greater.", num1)
elif(num2 >= num3):
    print("Number 2 is greater.", num2 )
else: 
     print("number 3 is greater.", num3)

#WAP to check if a number is a multiple of 7 or not.
x= int(input("enter a number:"))
if(x % 7 == 0):
    print("the number is multiple of 7.")
else: 
    print("the number is not multiple of 7.")