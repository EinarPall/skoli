# hlutapróf 2 6-10-2020
##

# dæmi 2

# fall til að tékka hvort n_str sé heiltala
def valid_num(n_str):
    try:
        int(n_str)
        return True
    except:
        False

# uppsöfnuð summa heiltalna
def sum_natural(n_str):
    if valid_num(n_str):
        total = 0
        for i in range(int(n_str) + 1):
            total += i
        return print('The result is:',total)
    else:
        pass


def factorial_natural(n_str):
    if valid_num(n_str):
        total = 1
        for i in range(1,int(n_str) + 1):
            total = i * total
        return print('The result is:',total)
    else:
        pass


def menu():
    print('1: Compute the sum of 1..n')
    print('2: Compute the product of 1..n')
    print('9: Quit')
    choice = input('Choice: ')
    return choice 



def main():
    choice = menu()
    while choice != '9':
        if choice == '1':
            n_str = input('Enter value for n: ')
            sum_natural(n_str)
        elif choice == '2':
            n_str = input('Enter value for n: ')
            factorial_natural(n_str)
        choice = menu()
main()




