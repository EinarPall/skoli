


def options():
    print('Please choose one of the options below:')
    print('a. Display the sum of the first N natural numbers.')
    print('b. Display the sum of the first N Fibonacci numbers.')
    print('c. Display the approximate value of e using N terms.')
    print('x. Exit from the program.\n')
    option = input('Enter option: ')
    n = input('Enter N: ')
    return n, option

op = options()
print(op)
letter = (op[1])
n = int(op[0])

print(n)
print(letter)



