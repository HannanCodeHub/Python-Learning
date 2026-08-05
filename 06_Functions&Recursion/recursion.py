# #print n to backwords:
# def show(n):
#     if(n == -1):
#         return
#     print(n)
#     show(n-1)

# show(5)

#factorial function:
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print (fact(4))

#Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n==0):
        return 0
    print (n)
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

#Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters

list = ["karachi" , "isb" , "sialkot" , "lahore" , "hyd"]

def print_list(list , idx = 0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(list)