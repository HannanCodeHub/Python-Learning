#Lists in Python
marks = [29,40,53,44,45]
print(marks)

print(type(marks)) #type 
print(len(marks)) #length

#marks of individual index:
print(marks[0])

#multiple type of data in single list:
student = ["hannan" , 22 , 98 , "karachi"]
print(student)

#strings are immmuttable (unchange) while lists are immutable (changed)
student = ["hannan" , 22 , 98 , "karachi"]
print(student[0])

student[0] = "ahmed"
print (student)

#List Slicing:
marks = [90,89,53,54,34,45]

print (marks[1:4])
print (marks[:5])
print (marks[-3:-1])

#List methods:
list = [1,2,3]

list.append(4) 
print(list)

list.sort() #return none 
list.reverse()
print (list.sort(reverse=True))
print (list)
list.insert(1,5)
print(list)


list = ['a', 'b', 'm', 'k','c']
list = (list.sort())
print(list)

#Tuples In Python: (immutable sequence of data like strings)
tup = (8,3,4,5,6,2)
print (tup[1])

#empty tuple
tup =()
print(tup)
print(type(tup))

tup =(1,) #, for tuple 
print(tup)
print(type(tup))

#slicing is same as in lists

#methods in tuple:
tup = (2,4,6,7,2,2)
print(tup.index(6))
print(tup.count(2))

#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
a = input("enter ur 1st fav movie: ")
b = input("enter ur 2nd fav movie: ")
c = input("enter ur 3rd fav movie: ")
movie = [a,b,c]
movie.sort()
print(movie)

#WAP to check if a list contains a palindrome of elements.
list1 = [1,0,1]
list2 = [1,2,3]

#Palindrome:
list1_copy = list1.copy()
list1_copy.reverse()

if(list1 == list1_copy):
    print("it is palindrome.")
else:
    print("it is not a palindrome.")

#Not a palindrome:
list2_copy = list2.copy()
list2_copy.reverse()

if(list2 == list2_copy):
    print("it is palindrome.")
else:
    print("it is not a palindrome.")

#WAP to count the number of students with the “A” grade in the tuple.
grade = ['A' , 'B', 'C' , 'A' , 'A', 'D' , 'C']
print(grade.count("A"))
grade.sort()
print(grade)