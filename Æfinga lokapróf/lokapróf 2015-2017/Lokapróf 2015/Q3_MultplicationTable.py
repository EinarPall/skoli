#Program that prints out a multiplication table dimension max 8x8



def get_size():
    size = int(input('Input table size: '))
    if size > 8:
        print('Invalid size')
    else:
        return size

def multiplication(size):
    for i in range(1,size+1):
        print('\t{}'.format(i), end='')
    tabs = '-'*size*8
    print('\n\t{}'.format(tabs))


    for i in range(1,size+1):
        print('\n{} |'.format(i),end='')
        for j in range(1, size+1):
            num = i*j
            print('\t{}'.format(num), end='')




# def print_table(size, multiply):
#     for i in range(0, size):
#         print('{}\t')


def main():
    size = get_size()
    multiply = multiplication(size)





main()