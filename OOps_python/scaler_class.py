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

# s1 = Student()
# s2 = Student()
# print(s1)
# print(s2)

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

# s1 = Student("Mohan")
# s2 = Student("Mu")
# print(s1)
# print(s2)

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

# s1 = Student("Mohan")
# print(s1)


class Student:
    #__<>__ is called Dunder and are default functions.
    def __init__(self,new_roll_num,new_name="Mohan"):
        #make sure parameters with default values in the end
        self.name = new_name
        self.roll_num = new_roll_num
        # pass
    def __str__(self):
        return f"Student's Name:{self.name}, Roll number: {self.roll_num}"
    
    def __repr__(self):
        return f"Roll number: {self.roll_num}"

s1 = Student("Mohan")
print(s1)

###class Variables
##Automated allocation of roll number by incrementing a value - counter

class Student:
    #__<>__ is called Dunder and are default functions.
    def __init__(self,new_roll_num,new_name="Mohan"):
        #make sure parameters with default values in the end
        self.name = new_name
        self.counter = 0 #object variable
        self.counter+=1
        self.roll_num = self.counter
        # pass
    def __str__(self):
        return f"Student's Name:{self.name}, Roll number: {self.roll_num}"
    
    def __repr__(self):
        return f"Roll number: {self.roll_num}"

s1 = Student("Mohan")
print(s1)
s2 = Student("Mu")
print(s2)
s2.counter = 1000 #doesn't update the class variable

class Student:
    counter = 0 #class variable, not needed to use self
    #because it is independent of the object, it is specific to class not for object where as self is specific to object.
    def __init__(self,new_roll_num,new_name="Mohan"):
        #make sure parameters with default values in the end
        self.name = new_name
        Student.counter+=1
        self.roll_num = Student.counter
        # pass
    def __str__(self): 
        return f"Student's Name:{self.name}, Roll number: {self.roll_num}"
    
    def __repr__(self): #outputs something unique/representative
        return f"Roll number: {self.roll_num}"

s1 = Student("Mohan")
print(s1)
s2 = Student("Mu")
print(s2)
print(repr(s2))


class Student:
    counter = 0 #class variable, not needed to use self
    #because it is independent of the object, it is specific to class not for object where as self is specific to object.
    def __init__(self,new_roll_num,new_name="Mohan"):
        #make sure parameters with default values in the end
        self.name = new_name
        Student.counter+=1
        self.roll_num = Student.counter
        # pass
    def __str__(self): 
        return f"Student's Name:{self.name}, Roll number: {self.roll_num}"
    
    def intro(self):
        print(f"Hello my name is {self.name} and my roll no is {self.roll_num}")

s1 = Student("Mohan")
s1.intro()


# class Account:
#     counter = 0
#     def __init__(self,opening_bal=0):
#         Account.counter+=1
#         self.id = Account.counter
#         self.bal = opening_bal
    
#     def __str__(self):
#         return f"Account has Rs. {self.bal}"
# a1 = Account(100)
# a2 = Account()
# print(a1)
# print(a2)

class Account:
    counter = 0
    def __init__(self,opening_bal=0):
        Account.counter+=1
        self.id = Account.counter
        self.bal = opening_bal
        self.numTrans = 0
        self.maxTrans = 2

    def __str__(self):
        return f"Account has Rs. {self.bal}"

    def deposit(self,amount):
        if amount>0 and self.numTrans< self.maxTrans:
            self.bal+=amount
            self.numTrans+=1

    def withdraw(self,amount):
        if self.bal>amount and self.numTrans< self.maxTrans:
            self.bal -=amount
            self.numTrans+=1


# a1 = Account(100)
# # a2 = Account()
# a1.deposit(100)
# print(a1)
# a1.withdraw(5)
# print(a1) 

class SavingAccount(Account):
    pass
    

class CurrentAccount(Account): #override
    def __init__(self):
        super().__init__() #new
        self.maxTrans=5

sal = SavingAccount()
cal = CurrentAccount()
print(sal)
print(cal)
cal.deposit(100)
print(cal)
cal.deposit(100)
print(cal)
cal.deposit(100)
print(cal)
