#READ MODE:

# f = open ("C://Users\HANNAN AHMED//Desktop//STUDY MATERIAL//Python-Learning//07_File_Input_Output//demo.txt", "r")
# data = f.read()

# #to print initial char:
# data = f.read(6)

# #to print one line only:
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# print(data)
# print(type(line1))
# f.close()

#WRITE MODE: 
f = open ("demo.txt", "a")

f.write("\nDay 2-3 of learning python.")

f.close()

# read + overwrite (pointer start se) // no truncate
f = open ("demo.txt", "r+")

f.write("\nDay 4 of learning python.") # overwrite krdega yeh

f.close()

#w+ for truncate , a+ for append //no truncate

#WITH Syntax:

with open ("sample.txt", "r") as f:
    data = f.read()
    print(data)


with open ("sample.txt", "w") as f:
    f.write("lets learn basics")

#DELETING A FILE:
import os
# os.remove("C://Users\HANNAN AHMED//Desktop//STUDY MATERIAL//Python-Learning//07_File_Input_Output//demo.txt")


# Create a new file “practice.txt” using python. Add the following data in it:
# WAF that replace all occurrences of “java” with “python” in above file.
# Search if the word “learning” exists in the file or not.
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java

# Create practice.txt and write data into it
with open("practice.txt", "w") as f:
    f.write("""Hi everyone
we are learning File I/O
using Java.
I like programming in Java""")

# Read file
with open("practice.txt", "r") as f:
    data = f.read()

# Replace Java with Python
new_data = data.replace("Java", "Python")

# Write updated data back to file
with open("practice.txt", "w") as f:
    f.write(new_data)

# Search for the word "learning"
if "learning" in new_data:
    print("Yes, 'learning' exists in the file.")
else:
    print("No, 'learning' does not exist in the file.")

#WAF to find in which line of the file does the word “learning”occur first.
#Print -1 if word not found.

def check_for_line():
    word = "learning"

    with open("practice.txt", "r") as f:
        line_no = 1

        for line in f:
            if word in line:
                return line_no
            line_no += 1

    return -1

print(check_for_line())


#From a file containing numbers separated by comma, print the count of even numbers
import os

# Show which file is being opened
print("File Path:", os.path.abspath("numbers.txt"))

# Read the file
with open("C://Users//HANNAN AHMED//Desktop//STUDY MATERIAL//Python-Learning//numbers.txt", "r") as f:
    data = f.read().strip()

print("File Content:", repr(data))

# Split numbers
numbers = data.split(",")

count = 0

# Count even numbers
for num in numbers:
    num = num.strip()   # Remove spaces/newlines

    if num.isdigit():   # Check if it's a valid number
        if int(num) % 2 == 0:
            count += 1

print("Count of even numbers:", count)