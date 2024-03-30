###WAP find the lenght of a list.(using is the parameter)
# cities = ["Karachi", "Kotri", "Hyderabad", "Tando Adam", "Shahdadpur", "Nawabsha", "Lundo"]
# district = ["Karachi", "Hyderabad", "Jamshoro", "Mirpurkhas", "Sanghar"]

# def print_len(len(list)):
#      print(list)
# print_len(len(cities))
# print_len(len(district))

###WAP to print the elements if a list in a single line.(List is the parameter)
# def printList(list):
#      for i in list:
#          (i, end=" ")
# printList(district)


###WAP to find the factorial of n.(n is the parameter)

# def fact (n):
#     x =1
#     for i in range(1,n+1):
#         x *= i
#     print(x,end = " ")
#         #i += 1
# fact(8)

###WAP to convet USD to PAk
# dollar = int(input("Enter the Dollar Amount : "))
# dollar_rate = 277.58 ### 1 United States Dollar equals
# def convert(value):
#     xchange = dollar_rate * dollar
#     print(dollar,"USD Xchange Amount pakistani Rupee =",xchange)

# convert(value=dollar)

# user = int(input("Enter the Number for check 'ODD' and 'EVEN' : "))
# def myfuc(val):
#     if(user%2 == 0):
#         print("EVEN NUMBER =",user)
#     else:
#         print("ODD NUMBER :",user)
#     return val
# myfuc(user) ## Call function 

### Calculate Factorial for useing Recursion Funcation
# def fact(val):
#     if(val == 1 or val == 0 ):
#         return 1
#     return fact(val-1)*val
    
# print("Factorial :",fact(5))

### Write a recursive function to calculate the sum of first n natural numbers
# def print_val(num):
#     if(num == 0):
#        return 0
#     return print_val(num-1) + num
# print(print_val(5))

### Write a recursive function to print all elements in a list.
### Hint : use list & index as parameters.
cities = ["Karachi", "Kotri", "Hyderabad", "Tando Adam", "Shahdadpur", "Nawabsha", "Lundo"]
def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    return print_list(list,index+1)
print_list(cities)
