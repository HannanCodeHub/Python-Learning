# #functions are used to reduce redundancy
# #function definition:
# def calc_sum(a, b):
#     sum = a + b 
#     print(sum)
#     return sum

# calc_sum(5,10)  
# calc_sum(2,10) 
# calc_sum(9,0)

# def hello():
#     print("hello world")

# hello()
# hello()
# hello()

# #average of 3 numbers:
# def avg_number(a,b,c):
#     sum = a + b + c
#     avg = sum / 3 
#     print(avg)


# avg_number (2,4,5)
# avg_number (2,2,2)
# avg_number(1,2,3)
 
# #WAF to print the length of a list. ( list is the parameter)
# cities = ["karachi", "lahore" , "hyderabad" , "sialkot" , "larkana" , "lahore"]

# def print_len(list):
#     print(len(list))

# print_len(cities)

# #WAF to print the elements of a list in a single line. ( list is the parameter)
# cities = ["karachi", "lahore" , "hyderabad" , "sialkot" , "larkana" , "lahore"]

# def print_list(list):
#     for item in list:
#         print(item, end =" ")

# print_list(cities)

# #WAF to find the factorial of n. (n is the parameter):
# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i 
#         print(fact)

# calc_fact(6)

# #WAF to convert USD to PKR:
# def convert(usd_val):
#     pkr_val = usd_val * 256
#     print(usd_val , "USD =", pkr_val , "PKR")

# convert(100)

#WAF to print ddd and even function:
def number(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")

number(500)
