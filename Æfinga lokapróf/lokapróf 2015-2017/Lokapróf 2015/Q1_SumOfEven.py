#six integers into an array
# Calculates sum of even numbers and writes out sum
def readNumbers():
    num_list = input('Input 6 numbers separated by commas: ')
    print(num_list)
    num_list = num_list.split(',')
    int_list = [int(i) for i in num_list]
    return int_list

def sumOfEven(int_list):
    sum_of_even = 0
    for i in int_list:
        if i % 2 == 0:
            sum_of_even += i
    return sum_of_even


def main():
    a_list = readNumbers()
    sum_even = sumOfEven(a_list)
    print(sum_even)

main()