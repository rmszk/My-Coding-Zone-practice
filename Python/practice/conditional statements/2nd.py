# ###Q(1)
# a = int(input("Enter the your fisrt Number:"))
# b = int(input("Enter the your Second Number:"))

# if a > b:
#     print(f"{a} is Greater then {b}")
# elif b > a:
#     print(f"{b} is Greater then {a}")
# else:
#     print(f"{a} Both the number are equal {b}")


# ###Q(2)
# gender = input("Please Provide your gender as 'F' or 'M':")

# if gender == "m" or gender == "M":
#     print("Good Morning Sir..!")
# elif gender == "f" or gender == "F":
#     print("Good Morning Ma`am..!")
# else:
#     print("Invaild Char please Try Again")

# ###Q(3)
# num = int(input("Enter the Number for the check even and Odd:"))
# if num%2 == 0:
#     print(f"This is even Number {num}")
# else:
#     print(f"This is Odd Number {num}")

# ###Q(4)
# name = input("Please tell your Name:")
# age = int(input("Please tell your Age:"))

# if age >= 18:
#     print(f"Hello {name} You are a Valid Voter")
# elif age < 18 and age > 0:
#     print(f"Hello {name} you are a not valid Voter")
# else:
#     print(f"Invalid Input {age} Please Tye Again")

# ###Q(5)
# year = int(input("please tell your year:"))

# if year%4 == 0 and year%100 != 0:
#     print("Leap Year")
# elif year%100 == 0 and year%400 == 0:
#     print("leap year")
# else: 
#     print("Not a leap year")

###(6)
alph = input("Please give me Character:")
if alph in "aeiouAEIOU":
    print("Its a Vowel",alph)
else:
    print("Its a consonent",alph)