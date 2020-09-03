# assignment 1.9.2020

############################sp1

# upto = int(input("Input an int: "))  # Do not change this line

# for i in range(1,upto):
#     print(i)


################################## sp2
# highest = int(input("Input an int: "))

# for i in range(1,highest+1):
#     if i % 3 == 0:
#         print(i)

####################################### sp3

# first = int(input("Input the first integer: "))
# second = int(input("Input the second integer: "))

# product=0
# for i in range(1,second+1):
#     product=product+first

# print(product)

################################################## sp 4

# max_days = int(input("Input max number of days: "))
# target = int(input("Input dollar target: "))
# total = 0
# days = 0
# for nr_of_days in range(1,max_days+1):
#     dollars = 2**(i-1)
#     total += dollars
#     if total >= target: 
#         days = nr_of_days
#         break
# print('Days needed:',days)

#lengri
# max_days = int(input("Input max number of days: "))
# target = int(input("Input dollar target: "))
# total = 0
# days = 0
# for i in range(1,max_days+1):
#     dollars = 2**(i-1)
#     total += dollars
#     days += 1
#     if total >= target: 
#         break
# if total < target:
#     days = 0

# print('Days needed:',days)

######################################################################## sp 5


# # ekki nested for
num = int(input("Input an int: ")) # Do not change this line

# total = 0
# for i in range(1,num+1):
#     # 1=1
#     # 1+2=3
#     total += i
#     print(total)
#     #for i in range(1,num)

# nested
for i in range(1,num+1):
    for j in range(0,i):
        i = i+j
    print(i) 



############################################################################################# sp6
# ég
# length = int(input("Input the length of series: "))
# total=0
# for i in range(1,(length*2)+1):
#     if i % 2 == 0:
#         print(i)
#         if i % 4 == 0:
#             i = -1 * i
#             print(i)

# print(total)

# annar, virkar
# length = int(input("Input the length of series: "))
# loka=0
# changer=1
# for i in range(1,length+1):
#     total = i * changer * 2
#     changer = -changer
#     loka += total
#     print(total)

# print('Sum:',loka)




















