# asssignment 7

# dæmi 1

# def every_other_letter(str):
#     b = ''
#     for i in range(len(input_str)):
#         if i%2 == 0:
#             b += str[i]
#     return b

# input_str = input("Enter a string: ")
# tilraun = every_other_letter(input_str)
# print('Every other character: ',tilraun)

## dæmi 2

# def count_digits(string):
#     num = sum(1 for c in string if c.isdigit())
#     return num

# input_str = input("Enter a string: ")
# digit_count = count_digits(input_str)
# print("No. of digits:", digit_count)

### dæmi 3

# def max_of_3(first,second,last):
#     if first > second and first > last:
#         max = first
#     elif second > first and second > last:
#         max = second
#     else:
#         max = last
#     return max

### eða 
def max_of_3(first,second,last):
    x =max(first,last,last)
    return x
###
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))

# maximum = max_of_3(first,second,third)
# print("Maximum:", maximum)

#### dæmi 4


# def is_prime(num):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#         else:
#             return True

# max_num = int(input("Input an integer greater than 1: "))


# for i in range(2,max_num+1):
#     prime = is_prime(i)
#     if prime == True:
#         print(i,'is a prime')
#     else:  
#         print(i,'is not a prime')



# # is_prime function definition goes here
# def is_prime(n):
#         if (n==1):
#             return False
#         elif (n==2):
#             return True
#         else:
#             for x in range(2,n):
#                 if(n % x==0):
#                     return False
#             return True
       
# # is_prime function definition goes here

# max_num = int(input("Input an integer greater than 1: "))

# for i in range(2,max_num+1):
#     tala = is_prime(i)
#     if tala == True:
#         print(i,"is a prime")
#     else:
#         print(i,"is not a prime")

# # Call the function here repeatadly from 2 to max_num and print out the appropriate message

##### dæmi 5
# eg virkar ekki
# def is_palindrome(string):
#     string = string.split(',')
#     for i in range(1,len(string)):
#         x += string[i:]
#         x = x[::-1]
#     return x

# in_str = input("Enter a string: ")
# if in_str == is_palindrome(in_str):
#     print('"{}" is a palindrome.'.format(in_str))
# else:
#     print('"{}" is not a palindrome.'.format(in_str))

# ## ekki ég virkar 


# def palindrome(input_str):
#     import string
#     modified_str = input_str.lower()
#     bad_chars = string.whitespace + string.punctuation
#     for char in modified_str:
#         if char in bad_chars:
#             modified_str = modified_str.replace(char,'')
#     if modified_str == modified_str[::-1]:
#         print('"{}" is a palindrome.'.format(input_str))
#     else:
#         print('"{}" is not a palindrome.'.format(input_str))
#     return

# in_str = input("Enter a string: ")
# palindrome(in_str)



###### dæmi 6  

def is_date_valid(date):
    from datetime import datetime
    date_format="%d.%m.%Y"
    if len(date) == 8:
        return True
        if 1 > date[1:2] > 31:
            return True
    else:
        return False


from datetime import datetime
date_format="%d.%m.%Y"
date_str = datetime.strptime(input("Enter a date: "),date_format)
if valid_date(date_str):
    print("Date is valid")
else:
    print("Date is invalid")  


