# ### Read File Method 
# f = open("/workspaces/My-Coding-Zone-practice/P"
#          "ython/practice/File I O/sample.txt","r")
# data = f.read()
# print(data)
# f.close()

###Write File Method
# f = open("/workspaces/My-Coding-Zone-practice/P"
#          "ython/practice/File I O/sample.txt","a")
# data = f.write("\nMobile No, : 03028124650")
# print(data)
# f.close()


### With Syntax Use Read Function

# with open("/workspaces/My-Coding-Zone-practice/P"
#           "ython/practice/File I O/sample.txt","r") as file:
#     data = file.read()
#     print(data)

### With Syntax Use Appendi Function
# with open("/workspaces/My-Coding-Zone-practice/P"
#           "ython/practice/File I O/sample.txt","a") as file1:
#     data1 = file1.write("\nName : Rao Muhammad shahroz Khan\nFather Name : Rao Abdul Munim khan\nAge : 24"
#                         "\nMobile No. : 03028124650\nCity : Shahdadpur\nDistric : Sanghar")

###Let's Practices
###Create a new file "Practice,txt" using python.Add the following data in it.
# with open("practice.txt","w") as file2:
#     data2 = file2.write("Hi everyone\nWe are learning File I/O\n"
#                         "Using python\nI like programming in python.")




###WAF that replace all occurrences of "Python" with "Java"in above file
# with open("practice.txt","r") as file2:
#     data2 = file2.read()
#     new_data = data2.replace("python","java")
#     print(new_data)

#     with open("practice.txt","w") as file2:
#         file2.write(new_data)


###Search if the word "Learning" Exists in the file or not


# word = "learning"
# def check_word():
#     with open("practice.txt","r") as file4:
#        data4 = file4.read()
#     if(data4.find(word) != -1):
#         print("FOUND")
#     else:
#         print("NOT FOUND")
# check_word()

###WAF to find in which line of file does the word "Learning" occur first.
####print-1 if word not found.
# def check_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as file5:
#         while data:
#             data = file5.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_line()


###from a file containing numbers seperated by comma,print the count of even numbers.

count =0
with open("practice.txt","r") as f:
    data = f.read()
    #print(data)
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            typecast = int(num)
           # print(typecast)
            if(typecast%2 == 0):
                count += 1
            num = ""
        else:
            num += data[i]
print(count)


count =0
with open("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        cast = int(val)
        if(cast % 2 == 0):
            count += 1
print(count)

