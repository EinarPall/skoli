
# fall til að tékka hvort n_str sé tala og hærri en 2
def valid_num(n_str):
    if n_str.isnumeric() and int(n_str) >= 2:
        return int(n_str)
    else:
        print('Error: {} was not a valid number.'.format(n_str),'\n')
        return False

# a
def sum_natural(n_str):
    if valid_num(n_str):
        total = 0
        for i in range(int(n_str) + 1):
            total += i
        return print('Natural number sum:',total,'\n')

# b
def sum_fibonacci(n_str):
    if valid_num(n_str):
        f1 = 0
        f2 = 1
        total = 1
        for i in range(2,int(n_str)):
            f3 = f1 + f2
            # print(f3)
            total += f3 
            f1 = f2 
            f2 = f3
        return print('Fibonacci sum:',total,'\n') 

# c
def approximate_euler(n_str):
    if valid_num(n_str):
        import math
        total = 0
        for i in range(int(n_str)):
            denominator = 1/math.factorial(i)
            total += denominator
        total = round(total,5)
        return print('Euler approximation:',total,'\n') 



def print_input():
    options = 'abc'
    print('Please choose one of the options below:')
    print('a. Display the sum of the first N natural numbers.')
    print('b. Display the sum of the first N Fibonacci numbers.')
    print('c. Display the approximate value of e using N terms.')
    print('x. Exit from the program.\n')
    option = input('Enter option: ')
    if option in options:
        n = input('Enter N: ')
        return n , option
    else:
        n = 0
        return n , option


def menu_or_not(option):
    n = 0
    if option in 'abc':
        option = input('Enter option: ')
        if option in 'abc':
            n = input('Enter N: ')
        return n , option
    else:
        n_option = print_input()
        n = n_option[0]
        option = n_option[1]
    return n , option


# byrjun 
n_option = print_input()
n = n_option[0]  
option = n_option[1]


while option != 'x':
    if option == 'a':
        sum_natural(n)
    elif option == 'b':
        sum_fibonacci(n) 
    elif option == 'c':
        approximate_euler(n) 
    else:
        print('Unrecognized option',option)
    n_options = menu_or_not(option)
    n = n_options[0]
    option = n_options[1]




def valid_choice(option):
    option = input('Enter option: ')
    n = input('Enter N: ')




