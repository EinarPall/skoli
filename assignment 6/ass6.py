# dæmi 1

# a_str = input("Input a string: ")

# print(a_str[0] + ' ' + a_str[-1])


## dæmi 2

# a_str = input("Input a string: ")

# print(a_str[-2:] + a_str[:-2])

### dæmi 3

# a_str = input("Input a string: ")
# upper = 0
# lower = 0
# for i in a_str:
#     if i >= 'a' and i <= 'z':
#         lower += 1
#     if i >= 'A' and i <= 'Z':
#         upper +=  1 
# print(lower)
# print(upper)

#### dæmi 4

# a_str = float(input("Input a float: "))

# a_str = "%.2f" % round(a_str,2)
# space = ''
# a_str = str(a_str)
# count_space = 12-(len(a_str))

# for i in range(1,count_space):
#     space += ' '

# print(space + a_str)

##### dæmi 5

# a_str = input("Input a string: ")
# lower,upper,numbers = 0,0,0 
# word = 1
# for i in a_str:
#     if i == ' ':
#         word += 1
#     if i >= 'a' and i <= 'z':
#         lower += 1
#     if i >= 'A' and i <= 'Z':
#         upper +=  1 
#     if i >= '1' and i <= '9':
#         numbers += 1

# letters = upper + lower + numbers
# answer = 'No. of letters: {}, no. of words: {}'.format(letters,word)
# print(answer)

###### dæmi 6

# name = input("Input a name: ")
# name = name.split()
# first_name = name[1]
# first = first_name[0].upper() + '. '
# last_name = name[0]
# last = last_name[0].upper() + last_name[1:-1]

# print(first + last)

####### dæmi 7

my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code

bin_str = ''
my_int2 = my_int 
if my_int == 0:
    bin_str = '0'
while my_int2 >= 1:
    counter = my_int2 % 2
    my_int2 = my_int2 // 2
    bin_str = str(counter) + bin_str

print("The binary of {} is {}".format(my_int,bin_str))






