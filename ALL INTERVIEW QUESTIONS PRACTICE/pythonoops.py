# class myclass: #Class
#     name="Rahul"
#     age=23
#     rollno=23240025

# p1=myclass() #object
# print(p1.name)
# print(p1.age)
# print(p1.rollno)

"""

class Teacher:
    def __init__(self,name,age,rollno): #constructor
        self.name=name
        self.age=age
        self.rollno=rollno

    def __str__(self):
        return f"{self.name} and age is {self.age}"
    
    def myFun(self): #object method
        print("Hello My name is : "+ self.name)

p1=Teacher("Rahul",23,23240025)
print(p1)
p1.myFun()

p1.age=25
print(p1.age)
# del p1.age  # delete object Properties
# del p1  #Delete Object
print(p1.age)

class Person:
    pass  #pass statement
    

"""

class BankAccount:
    def __init__(self):
        self.__balance=0.0
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid Deposited")

    def withdraw(self,amount):
        if amount>0 & amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawal")
    def get_balance(self):
        return self.__balance
    

p1=BankAccount()
p1.deposit(1000)
p1.withdraw(300)
print(p1.get_balance())