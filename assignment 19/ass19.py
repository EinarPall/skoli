## assignment 19

# dæmi 1

class NaturalNumber:
    def __init__(self, num = 0):
        try:
            if 0 <= num  and num % 1 == 0:
                self.__num = num
            else: 
                self.__num = None
        except TypeError:
            self.__num = None
    
    def __str__(self):
        return f'{self.__num}' 

    def __add__(self, other):
        try: 
            outcome = self.__num + other.__num
            return NaturalNumber(outcome)
        except TypeError: 
            return None

    def __sub__(self, other):
        try:
            outcome = self.__num - other.__num
            return NaturalNumber(outcome)
        except TypeError:
            return None
        
    def __mul__(self, other):
        try:
            outcome = self.__num * other.__num
            return NaturalNumber(outcome)
        except TypeError:
            return None


# from natural_number import NaturalNumber

# num1 = NaturalNumber(1)
# print(num1)

# num1 = NaturalNumber(3)
# num2 = NaturalNumber(4)
# num3 = num1 + num2
# print(num3)

# num2 = NaturalNumber(2)
# num3 = num1 * num2
# print(num3)

# num3 = num1 - num3
# print(num3)

# testcase 3
# num1 = NaturalNumber(4)
# num2 = NaturalNumber(3)
# num3 = num1 * num2
# num4 = NaturalNumber(-1) * num2
# assert str(num3) == '12'
# assert str(num4) == 'None'


# dæmi 2

class Student:
    def __init__(self, ID, grade_list):
        self.studendet_ID = ID
        self.grade_list = grade_list
        self.grade_avg = sum(self.grade_list)/len(self.grade_list)
    def __str__(self):
        return f'Student ID: {self.studendet_ID}\nGrades: {self.grade_list}' 

    def __lt__(self, other):
        if self.grade_avg < other.grade_avg:
            return True
        else:
            return False

# dæmi um input
# student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
# student2 = Student(2, [9.5, 9.0, 8.9, 9.8])
# print(student1)

# if student1 < student2: # ef þetta satt þá prentar þetta út staðreyndina
#     print("student1 < student2")


# dæmi 3 

class SavingsAccount(object):
    __IR = 0.05
    __BR = 0.1
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return 'Balance: %.2f'% (self.amount)

    def update_balance(self):
        #IR_amount = self.amount * (1 + SavingsAccount.__IR)
        bonus_amount = self.amount * (1 + SavingsAccount.__BR + SavingsAccount.__IR)
        self.amount = bonus_amount
        #return SavingsAccount(bonus_amount)


class DebitAccount(SavingsAccount):
    __IR = 0.02
    def __init__(self, amount):
        SavingsAccount.__init__(self,amount)

    def update_balance(self):
        IR_amount = self.amount * (1 + DebitAccount.__IR)
        self.amount = IR_amount


# main og input
def print_accounts(accounts):
    for account in accounts:
        print(account)
    print()

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

# sav1 = SavingsAccount(1000)
# deb1 = DebitAccount(1000)
# sav2 = SavingsAccount(2000)
# deb2 = DebitAccount(4000)

# accounts = [sav1, deb1, sav2, deb2]
# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)
# update_accounts(accounts)

# print_accounts(accounts)

### dæmi 4

class HourlyEmployee():
    def __init__(self,employee, hour_wage):
        

class SalariedEmployee():

class Manager():



# dæmi um input og notkun
# from employee import HourlyEmployee, SalariedEmployee, Manager

def print_salaries(staff):
    for employee in staff:
        name = employee.get_name()
        hours = int(input("Hours worked by " + name + ": "))
        pay = employee.weekly_pay(hours)
        print("{}: {:.2f}".format(name, pay))

# The main program starts here
staff = []
staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
staff.append(SalariedEmployee("Sally Lin", 52000.0)) # 52000 is the annual salary
staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
print_salaries(staff)