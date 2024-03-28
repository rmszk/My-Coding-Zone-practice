# i = 1
# while i  <= 10:
#     print("Rao Muhammad shahroz Khan",i)
#     i+=1

# i = 1
# while i <= 5:
#     print(i)
#     i +=1

# print("Loop Ended")


#-----Question 1 table------#
# n = 5
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i +=1

#------Question 2 table------#

# table_No = int(input("Enter the Number for Table : "))
# len = int(input("Enter the table lenght for print : "))
# x = 1
# while x <= len:
#     multiple = table_No * x
#     print(table_No,"X",x,"=",multiple)
#     x +=1


# #---Question: print the elements of the following list a loop
# num = [1, 4, 9, 16, 17, 20, 22, 25, 36, 49, 64, 81, 100]
# lenght = len(num)-1
# i = 0
# while i <= lenght:
#     print(num[i])
#     i +=1


# Search for a number X in this tuple using loop:
# srch = int(input("Enter a number for your searching in the tuple : "))
# num1 = (1, 4, 9, 16, 17, 20, 22, 25, 36, 49, 64, 81, 100)
# x = 0
# while x < len(num1):
#     if(num1[x] == srch):
#      print("this number exist in this tuple index number ",x)
#     else:
#      print("this number not exist in the tuple")
#     #print(num1[x])
#     x += 1


#print the elements of the following list using a loop
# list = [1, 5, 7, 8, 10, 13, 16, 20, 24, 28, 30, 40, 50, 60, 70, 80, 90, 100]

# for val in list:
#   print(val)

#search for a number X this tuple using loop.
# tup = (1, 5, 7, 8, 10, 13, 16, 20, 24, 28, 30, 40, 50, 60, 70, 80, 90, 100)
# x = 13
# indx = 0
# for val1 in tup:
#   if(val1 == x):
#     print("NUMBER FOUND THAT Index ",indx)
#     break
#   indx += 1


####using For & range()
####Print number from 1 to 100
# for i in range(1, 100):
#     print(i)

####print number from 100 to 1
# for i in range(100, 0, -1):
#     print(i)


####print the multiplication table of a number N.
# n = int(input("enter the number : "))
# for i in range(1, 11):
#     val = i*n
#     print(val)

####WAP to find the sum first N Numbers,(Using while)
# i = 1
# n = 5
# sum = 0
# while i <= n:
#     sum += i 
#     i +=1
# print(sum)


# n = 5 
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Total Number of sum ",sum)


####WAP to find the Factorial of first N numbers,(using for)
n1 = 5
fact = 1
for i in range(1,n1+1):
    fact *= i
print("Factorial Number =",fact)