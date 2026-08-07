#class and Object

class Student :  # class
    name = "hannan"

s1 = Student() #object
print(s1.name)

class Car:
    color = "blue"
    model = "BMW"
    year = "2022"

car1 = Car()
print (car1.color)
print (car1.model)
print (car1.year)

#constructor (_init)

class Student :  # class

    college_name = "salim habib university" #class attr
    #Parameterized constuctor:
    def __init__(self, name, marks , age):  #khud e create hujata h wese tw krne ki zrurt nhn (hamesha arg pass karna hota h const mein.) 
        self.name = name  #obj attr > class att
        self.marks = marks
        self.age = age
        #print("adding new student ...")

    def welcome(self): #methods
        print("welcome student,", self.name)

    def get_marks(self):  #methods
        return self.marks

s1 = Student("hannan ahmed", 99, 22) #object
s1.welcome()
print(s1.get_marks())
print(s1.name , s1.marks , s1.age) #hannan

s2 = Student("shahryar ali", 95, 23)
print(s2.name, s2.marks , s2.age)

print(Student.college_name)
#def _init_(self) : default constructor

#Practice question:
#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

class Student:
    
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks :
            sum += val
        print("hi" , self.name , "your avg score is:", sum/3 )

    @staticmethod  #decorator
    def hello():
        print("hello!")

s1 = Student("Hannan", [98, 81, 97] )
s1.get_average()

Student.hello()

#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal , acc_numb):
        self.bal = bal
        self.acc_numb = acc_numb

    #debit method
    def debit(self, amount):
        self.bal -= amount
        print("PKR:" , amount, "was debited")
        print("total balance =" , self.get_balance())

    def credit(self, amount):
        self.bal += amount
        print("PKR:" ,amount , "was credited")
        print("total balance =" , self.get_balance())

    def get_balance(self):
        return self.bal

acc1 = Account(10000, 92191029)
acc1.debit(5000)
acc1.credit(200)
acc1.credit(27000)
acc1.debit(18700)

#del key :
class Name:
    def __init__(self, name):
        self.name = name 

s1 = Name("hannan")
print(s1.name)

del s1.name
print(s1.name)

#private:
class Account:
    def __init__(self, acc_no, pwd):
        self.acc_no = acc_no
        self.__pwd = pwd  #to make paswrd private : __  

acc1 = Account("1234", "abc123")

print(acc1.acc_no)

#Inheritance:
class Car:

     def __init__(self,type):
        self.type = type

     def start():
        print("car is starting..")

     def stop():
        print("car has stopped!")

class ToyotaCar(Car):

    def __init__(self, name, type):
       self.name = name
       super().__init__(type)

car1 = ToyotaCar("Fortuner", "electric")
print(car1.type)


#property:
class Student:
    def __init__(self, phy , chem ,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def CalcPercentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stud1 = Student(99,98,97)
stud2 = Student(89,78,88)
print(stud1.CalcPercentage)
print(stud2.CalcPercentage)


stud2.phy = 66
print(stud2.CalcPercentage)

#complex number program:
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(str(self.real) + "i + " + str(self.img) + "j")

    def __add__(self, numb2):
        newReal = self.real + numb2.real
        newImg = self.img + numb2.img
        return Complex(newReal, newImg)

    def __sub__(self, numb2):
        newReal = self.real - numb2.real
        newImg = self.img - numb2.img
        return Complex(newReal, newImg)    

numb1 = Complex(9, 4) 
numb1.showNum()
       
numb2 = Complex(5, 2) 
numb2.showNum()


sum = numb1 + numb2
print("addition of two complex numbers :")
sum.showNum()

sum = numb1 - numb2
print("subtraction of two complex numbers :")
sum.showNum()

#program:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2 

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# #program:
class Employee:
        def __init__(this, role , department, salary):
            this.role = role
            this.department = department
            this.salary = salary

        def ShowDetails(this):
            print("role =" , this.role)
            print("departmemt =", this.department)
            print( "salary =" , this.salary)

class Engineer(Employee):
    def __init__(this, name , age):
        this.name = name
        this.age = age
        super().__init__("Software Engineer", "IT" , 75000)


eng1 = Engineer("Hannan Ahmed" , "22")
eng1.ShowDetails()

#program :
class Order :
    def __init__(self, item , price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("kurkure", 20)
ord2 = Order("lays", 40)

print(ord1 > ord2)
