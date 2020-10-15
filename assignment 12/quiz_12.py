# sp 2

# def scope_function(a_int):
#   new_int = a_int
#   a_int += 30

# scope_function(20)
# print("New int: ", new_int)


# sp 4 
# number = 5

# def func(number):
#     print(number, end= ' ')
#     number = 2
#     print(number, end= ' ')

# func(number)
# print(number)

#  sp 5
# def my_fun(param):
#     param.append(4) # þessi hefur áhrif á my_list
#     return param + [4]

# my_list = [1, 2, 3]
# new_list = my_fun(my_list)
# print(my_list, new_list)

## sp 6
# def make_password(alphas, symbol = '#'):
#     return symbol + alphas + symbol

# #make_password(symbol = '$', 'xyz'))
# make_password(symbol = '$', alphas = 'xyz') #virkar ekki

#### sp 7
# def list_manipulation(a_list, b_list):
#     b_list[0] = a_list[0]
#     a_list = b_list

# a_list = [1, 2, 3]
# b_list = [4, 5, 6]

# list_manipulation(b_list, a_list)
# print(a_list, b_list)

######## sp 8
# my_int = 4

# def my_function(first_int, second_int = 3):
#    my_int = 3
#    return first_int + second_int + my_int

# print(my_function(1,2), my_function(my_int))

####### sp 10
cc = 2

if False:
    cc = 66

def helmet():
    if True:
        cc = 40

helmet()

print(cc)