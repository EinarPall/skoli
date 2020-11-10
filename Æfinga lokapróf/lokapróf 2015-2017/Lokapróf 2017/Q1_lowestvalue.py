def lowest_value(num1, num2):
    num_1 = int(num1)
    num_2 = int(num2)
    if num_1 < num_2:
        return '{} is lower'.format(num_1)
    else:
        return '{} is lower'.format(num_2)




def lowest_of_three(num1, num2, num3):
    num_1 = int(num1)
    num_2 = int(num2)
    num_3 = int(num3)
    if num_2 > num_1 < num_3:
        return '{} is the lowest number'.format(num_1)
    elif num_2 < num_3:
        return '{} is the lowest number'.format(num_2)
    else:
        return '{} is the lowest number'.format(num_3)

def lowest_from_list():
    num_list = input('Input list of numbers separated by commas: ')
    num_list = num_list.split(',')
    print(num_list)
    return min(num_list)


def main():
    num1 = input('Input number 1: ')
    num2 = input('Input number 2: ')
    higher_num = lowest_value(num1, num2)
    print(higher_num)
    num1 = input('Input number 1: ')
    num2 = input('Input number 2: ')
    num3 = input('Input number 3: ')
    lowest_num = lowest_of_three(num1, num2, num3)
    print(lowest_num)
    
    lowest_num = lowest_from_list()
    print(lowest_num)









main()