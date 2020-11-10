#skrifa inn N(valin tala á milli 3-20) 
# print smalles num 
# If N outside legal rang, program quits

def receiveInput(length):
    num_list = []
    for i in range(1, length+1):
        num = int(input())
        if 3 <= num <= 20:
            num_list.append(num)
        else:
            break
    return num_list


def findSmallest(num_list):
    return min(num_list)






def main():

    num_amount = int(input('How many numbers will you enter?\n\n'))
    num_list = receiveInput(num_amount)
    smallest_num = findSmallest(num_list)
    print()
    print('Smallest num is {}'.format(smallest_num))



main()