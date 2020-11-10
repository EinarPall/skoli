## assignment 15

# dæmi 2


def get_set():
    a_list = input('Input a list of integers separated with a comma: ').strip().split(',')
    a_list = [int(i) for i in a_list]
    return make_set(a_list)

def make_set(a_list):
    return set(a_list)


def union(set_1,set_2):
    return set_1 | set_2


def intersection_set(set_1, set_2):
    return set_1 & set_2

def difference(set_1,set_2):
    return set_1 - set_2

def menu():
    print('1. Intersection\n2. Union\n3. Difference\n4. Quit')
    choice = input('Set operation: ')
    return choice

def execute_selection(choice, set_1,set_2):
    if choice == '1':
        return intersection_set(set_1,set_2)
    elif choice == '2':
        return union(set_1,set_2)
    elif choice == '3':
        return difference(set_1,set_2)
# minus fyrir difference


def main():
    set_1 = get_set()
    set_2 = get_set()
    print(set_1)
    print(set_2)
    choice = '1'
    while choice != '4':
        choice = menu()
        result = execute_selection(choice,set_1,set_2)
        if result != None:
            print(result)
        else: 
            choice = '4'
main()












