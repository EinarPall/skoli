# Programming Exercises

# 1 , 2 , 3

# num1 = int(input('veldu tölu: '))
# num2 = int(input('veldu tölu: '))
# num3 = int(input('veldu tölu: '))
# print(num1+num2)
# print(num1+num2+num3)
# print(num2*num3)

#### 4
# age = int(input('enter your age: '))
# name = input('enter your name: ')
# print('Hello, my name is',name,'and my age is',age,'.')

##### 5
# firstname = input('whats your first name?: ')
# lastname = input('what is your last name?: ')
# fullname = firstname + ' ' + lastname
# print('Your full name is',fullname)

###### 6 
# celsius = int(input('temerature in celsius: '))
# farenheit = int(celsius * 9/5 +32)
# print('This themparture is',farenheit,'in farenheit')

####### 7
# num1 = int(input('choose a number: '))
# num2 = int(input('choose a number: '))
# if num1 > num2:
#     print(num1,'is grater than',num2) 
# elif num2 > num1:
#     print(num2,'is grater than',num1) 
# else:
#     print('the numers are equal')

######## 8
# str_1 = input('enter a string: ')
# str_2 = input('enter a string: ')
# if str_1 == str_2:
#     print('The strings are the same length')

######### 9
# num1 = int(input('veldu tölu: '))
# num2 = int(input('veldu tölu: '))
# num3 = int(input('veldu tölu: '))
# if num1 < num2 and num1 < num3:
#     print(num1) 
# elif num2 < num1 and num2 < num3:
#     print(num2)
# else :
#     print(num3)1

######### fjö lausn
# numbers = []
# for i in range(1,4):
#     num = int(input('veldu tölu: '))
#     numbers.append(num)
# lowest_num = num
# for i in range(len(numbers)):
#     if int(numbers[i-1])< lowest_num:
#         lowest_num = numbers[i-1]
# print(lowest_num)

# virkar ekki
# for i in range(1,4):
#     num = int(input('veldu tölu: '))
#     'num' + str(i) = num 
#     print(num1)
#
# i = 1
# ('num' + str(i)) = i
# print(u)

########## 10
n =  int(input('veldu tölu: '))
if n < 10 and n >= 0:               
    print('Less than 10')
elif n >=10 and n < 20:
    print('between 10 and 20')
elif n >= 20:
    print('the value is too high!')
elif n < 0:
    print('too low')

########### 11
