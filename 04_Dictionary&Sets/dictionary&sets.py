info = {
    "key" : "value",
    "name" : "Hannan Ahmed",
    "subjects" : ["python" , "java" , "c++"],
    "topic in this file:" : ("dict", "sets"),
    "cgpa" : 3.55,
    "grade" : "A",
    12 : 13
}
print (info)
print(type(info))

print (info['name'])
print(info['grade'])

#Dictionary are unordered , mutable(changeable) and dont allow duplicate keys.
info["name"] = "hanan"
info["surname"] = "meymon"

print (info)

null_dict = {
 "name" : "Hannan"
}
print(null_dict) #shows null

#nested dictionary 

student = {
    "name" : "hannan ahmed",
    'Subjects' :{
        "physics": 45,
        "chemistry":76
}
}
print (student["Subjects"] ['chemistry'])

#METHODS
#to print all keys :
print(student.keys()) # could also be typecast in list and float 
print(student.values())
print(list(student.keys())) #typecasting
print(student.items()) #pair values

#print(student["name2"])  #error
print(student.get("name2")) #None - error show nhikregi

student.update({"city" : "delhi"})
print(student)

#Sets In Python: (unordered , unique values , duplicate not allow)
#Sets are mutable but sets elements are immutable (REMEMBER !)

collection = {1,2,3,4,5,"hi", "my name is hannan"}
print(collection)
print(type(collection))

empty = set() #null set
#methods:
empty.add(1)
empty.add(2.3)
empty.add((1,2,4,5,6,)) #tuple
empty.add("hi, its my python journey!")
print(empty.pop())

#list is unhashable type here.

empty.remove(2.3)

print(empty)

empty.clear()
print(len(empty))
print(type(empty))

#union and intersection :
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))

# Store following word meanings in a python dictionary :
dictionary = {

    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of adds & figures"]
 
}
print(dictionary)

#You are given a list of subjects for students.
#Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

subjects = {
    "python", "java" , "c++" , "C", "python" , "javascript" , "c++",
    "python" , "java" , "c++" ,"C"
}
print(subjects)
print(len(subjects))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}

x = int(input("phy: "))
marks.update({"phy: ": x})

y = int(input("chem: "))
marks.update({"chem:": y})

z = int(input("maths: "))
marks.update({"maths:": z})

print(marks)

#Figure out a way to store 9 & 9.0 as separate values in the set.
#(You can take help of built-in data types)

value = {9, "9.0"}
print(value)

#OR
values ={
    ("float" , 9.0), 
    ("int" , 9)
}
print(values)