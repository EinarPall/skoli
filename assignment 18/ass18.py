# Assignmet 18 

# dæmi 1

class Pair:
    def __init__(self,val1 = 0 ,val2 = 0):
        self.val1 = val1 
        self.val2 = val2
    
    def __str__(self):
        return f"Value 1: {self.val1}, Value 2: {self.val2}"

    def __add__(self,other):
        total_val1 = self.val1 + other.val1  
        total_val2 = self.val2 + other.val2
        return Pair(total_val1,total_val2)




# main
# pair1 = Pair()
# print(pair1)
# # Value 1: 20, Value 2: 30
# pair2 = Pair(40,50)
# pair3 = pair1 + pair2
# print(pair3)
# Value 1: 60, Value 2: 80


# dæmi 2

class MyString:
    def __init__(self,str1):
        self.str1 = str1
        # self.strlen = len(str1)

    def __str__(self):
        pass

    def __len__(self):
        return len(self.str1)

    def __gt__(self,other):
        return len(self) > len(other)

    def __sub__(self,other):
        return abs(len(other) - len(self))

## main
# str1 = MyString('this is a string')
# str2 = MyString('this is another one')
# print(str1 > str2)
# # False
# print(str1 - str2)
# 3
# print(len('hallo'))

# testcase 3
# str1 = MyString("What Does Tesla's Automated Truck Mean for Truckers?")
# str2 = MyString('Answer: Hard to say.')
# print(str1 > str2) # == True
# print(str1 - str2) # == 32
# print(str2 - str1) # == 32


# dæmi 3 

class Rectangle:
    def __init__(self, length = 1, width = 1):
        if width <= 0:
            self.__width = 1
        else:
            self.__width = width
        if length <= 0:
            self.__length = 1
        else:
            self.__length = length  
    
    def __str__(self):
        return f"Length: {self.__length}, Width: {self.__width}"

    def area(self):
        return self.__length * self.__width
        

    def perimeter(self):
        return 2*self.__length + 2*self.__width

    def __repr__(self):
        return f"Rectangle({self.__length},{self.__width})"

    def __eq__(self,other):
        return self.area() == other.area()

# area(self) == area(other) --- vitlaus ritháttur

## testcase 2 ##

# rec1 = Rectangle(2,-3)
# print(rec1.area()) #== 2
# rec1.perimeter() #== 6
# str(rec1) #== 'Length: 2, Width: 1'

# main
# rec1 = Rectangle()
# rec2 = Rectangle(2,3)
# print(rec1)
# print(rec2.area())
# print(rec2.perimeter())
# print(rec2.__repr__())
# print(rec1 == rec2)
#### main output ####
# Length: 1, Width: 1
# 6
# 10
# Rectangle(2,3)
# False



# dæmi 4 

class CashRegister:
    # var vitlaust að setja þetta uppí lista, þar sem summan skiptir bara máli og count, ekki stökin sjálf
    def __init__(self, tax_rate):
        self.__tax_rate = float(tax_rate/100)
        self.__item_count = 0
        self.__item_price = 0
        self.__item_tax = 0


    def __str__(self):
        return 'Items: %d, total price: %.2f, including tax: %.2f'% (self.__item_count, self.__item_price, self.__item_tax)
        #return f'Items: {float(len(self.__item_list))}, total price: {float(sum(self.__item_list))}, including tax: {float(sum(self.__tax_rate))}'

    def add_item(self, item_price, tax_or_not):
        self.__item_count += 1
        self.__item_price += item_price 
        if tax_or_not: 
            self.__item_tax += item_price * (1+self.__tax_rate)
        else:
            self.__item_tax += item_price

    def get_total(self):
        return self.__item_price

    def get_total_with_tax(self):
        return self.__item_tax
    
    def get_count(self):
        return self.__item_count
    
    def clear(self):
        self.__item_price = 0
        self.__item_tax = 0
        self.__item_count = 0


# from cash_register import CashRegister

# register1 = CashRegister(10.0)  # 10% tax rate
# register1.add_item(3.5, False)  # The price of the item is 3.5, no tax
# register1.add_item(10.0, True)  # The price of the item is 10.0, taxable 
# print(register1)

# print(register1.get_count())
# print(register1.get_total())
# print(register1.get_total_with_tax())

# register1.clear()
# print(register1)

# 'Items: {}, total price: {}, including tax: {}'.format(float(len(self.__item_list)),float(sum(self.__item_list)),float(sum(self.__tax_rate)))


# testcase 5
reg1 = CashRegister(7.5)
reg1.add_item(10.0, True)
reg1.add_item(15.5, True)
reg1.add_item(23.3, False)
print(reg1.get_count()) # == 3
print(reg1.get_total()) # == 48.8
print(reg1.get_total_with_tax()) # == 50.7125
print(str(reg1)) # == 'Items: 3, total price: 48.80, including tax: 50.71'
reg1.clear()
print(str(reg1)) # == 'Items: 0, total price: 0.00, including tax: 0.00'