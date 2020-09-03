###sp5
##my_int = int(input("Enter a positive integer: "))
##
##while my_int > 0:
##    if my_int % 2 == 1:
##        my_int = my_int // 2
##    else:
##        my_int = my_int - 1
##
##print(my_int)

# sp6
##number = int(input("Enter a positive integer: "))
##count = 0
##
##while number > 1:
##    if number % 2 == 0:
##        number = number // 2
##    elif number % 3 == 0:
##        number = number // 3
##    else:
##        number = number - 1
##    count = count + 1
##
##print(count)

#sp8
####i = 1
####j = 1
####
####while i < 5:
####    i += 1
####    j += i
####print(i,j)

#sp10

num = int(input("Enter a number: "))

while True:
    if num % 3 == 0:
        break
    print(num)
    num -= 1
