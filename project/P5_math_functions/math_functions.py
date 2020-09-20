

def sum_natural(n_str):
    total = 0
    n = int(n_str)
    if n < 2:
        return None
    else:
        for i in range(n + 1):
            total += i
    return total


def sum_fibonacci(n_str):
    n = int(n_str)
    f1 = 0
    f2 = 1
    total = 1
    for i in range(2,n):
        f3 = f1 + f2
        # print(f3)
        total += f3 
        f1 = f2 
        f2 = f3
    return total 

def print_input():
    print('Please choose one of the options below:')
    print('a. Display the sum of the first N natural numbers.')
    print('b. Display the sum of the first N Fibonacci numbers.')
    print('c. Display the approximate value of e using N terms.')
    print('x. Exit from the program.\n')
    option = input('Enter option: ')
    n = input('Enter N: ')
    return n , option

option = ""

n_option = print_input()
n = int(n_option[0])
option = n_option[1]

while option != 'x':
    if option == 'a':
        print('Natural number sum:',sum_natural(n))
    elif option == 'b':
        print('Fibonacci sum:',sum_fibonacci(n)) 
    elif option == 'c':
        print('yada sum:',sum_fibonacci(n)) 
    else:
        print('Unrecognized option',n)
        print_input()
    option = input('Enter option: ')
    n = input('Enter N: ')










