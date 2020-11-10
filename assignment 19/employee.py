### dæmi 4 í assignment 19


class HourlyEmployee():
    __MAX_HOURS = 40
    __HOURS_EXCESS_WAGE_ratio = 1.5
    def __init__(self,name, hour_wage):
        self.__name = name
        self.__hour_wage = hour_wage

    def weekly_pay(self, inp_hours):
        outcome = 0
        if inp_hours > HourlyEmployee.__MAX_HOURS :
            outcome += HourlyEmployee.__MAX_HOURS * self.__hour_wage
            outcome += (inp_hours - HourlyEmployee.__MAX_HOURS) * self.__hour_wage * HourlyEmployee.__HOURS_EXCESS_WAGE_ratio
        else:
            outcome += inp_hours * self.__hour_wage
        return outcome

    def get_name(self):
        return self.__name


class SalariedEmployee(): # parent af Manager 
    def __init__(self, name, annual_salary):
        self._name = name
        self._annual_salary = annual_salary

    def get_name(self):
        return self._name

    def weekly_pay(self,hours):
        return self._annual_salary/52


class Manager(SalariedEmployee): # child of SalariesEmployee
    def __init__(self, name ,annual_salary, bonus):
        SalariedEmployee.__init__(self, name , annual_salary)
        self.__bonus = bonus

    def get_name(self):
        return self._name

    def weekly_pay(self,hours):
        return int(self._annual_salary/52 + self.__bonus)

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
staff.append(Manager("Mary Smith", 91000.0, 60.01))
print_salaries(staff)
## testcase 4
emp3 = Manager("Mary Smith", 91000.0, 60.0)
print(emp3.weekly_pay(60)) # == 1810