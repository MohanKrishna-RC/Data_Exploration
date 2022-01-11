"""
Class -- template
object/instance -- real object
"""

"""
Class will have two things
1. Properties/Characteristics -- variables
2. Methods -- functions, perform mutations in the properties
"""
# class Student:
#     #__<>__ is called Dunder
#     def __init__(self):
#         #self variable contains the reference to the specific object
#         print("this statement ",self)
#         self.name = "No Name"
#         # pass
    
# a1 = Student()
# # print(a1.name)  #returns "No Name"
# a2 = Student()
# a2.name = "Mohan"
# print(a2.name)

class Student:
    #__<>__ is called Dunder and are default functions.
    def __init__(self,new_name="Mohan"):
        #self variable contains the reference to the specific object
        self.name = new_name
        # pass
    def __str__(self):
        return f"Student's Name:{self.name}"
    #python automatically call the str funciton whenever we call print function.But if we define 
    # str function python calls str.

s1 = Student()
s2 = Student()
print(s1)
print(s2)

class Student:
    #__<>__ is called Dunder and are default functions.
    def __init__(self,new_name):
        #self variable contains the reference to the specific object
        self.name = new_name
        # pass
    def __str__(self):
        return f"Student's Name:{self.name}"
    #python automatically call the str funciton whenever we call print function.But if we define 
    # str function python calls str.

s1 = Student("Mohan")
s2 = Student("Mu")
print(s1)
print(s2)

class Student:
    #__<>__ is called Dunder and are default functions.
    def __init__(self,new_name,roll_num=11):
        #make sure parameters with default values in the end
        self.name = new_name
        self.roll_num = roll_num
        # pass
    def __str__(self):
        return f"Student's Name:{self.name}, Roll number: {self.roll_num}"
    #python automatically call the str funciton whenever we call print function.But if we define 
    # str function python calls str.

s1 = Student("Mohan")
print(s1)