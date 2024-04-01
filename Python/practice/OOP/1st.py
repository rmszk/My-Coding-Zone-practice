# ###Class Blue print 
# from ipaddress import collapse_addresses
# from re import A


# class person:
#     name = "Rao Muhammad shahroz Khan"
#     occupation = "Software Developer"
#     age = 24
#     def info(self):
#         print(f"{self.name} ia a {self.occupation}")
#         print("Age",self.age)

# ### Object
# a = person()
# a.info()

# b = person()
# b.name = "Rao Ziyan"
# b.occupation = "student"
# b.age = 12
# b.info()

### using class With Constructors
class python_class:
    collage_name = "Minhaj-ul-Quran"

    ### Paramitarize Constructor
    def __init__(self, name, Roll_No, Age):
        self.name = name
        self.rollno = Roll_No
        self.age = Age
    def print_info(self):
        print(self.collage_name,f"\nName {self.name} \nRoll No {self.rollno} \nAge {self.age}")

a = python_class("shahroz",48539,24)
b = python_class("Areeba",48510,22)
c = python_class("Umar",48511,20)
d = python_class("Usman",48512,18)
a.print_info()
b.print_info()
c.print_info()
d.print_info()
