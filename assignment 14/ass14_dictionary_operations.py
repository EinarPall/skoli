# assignment 14

# dæmi 3

def menu_selection():
    choice = input('Menu: \n(a)dd, (r)emove, (f)ind: ').lower()
    return choice

def execute_selection(choice, a_dict):
    if choice == 'a':
        try: 
            key = input('Key: ')
            value = input('Value: ')
            the_dict = add_to_dict(key,value,a_dict)
        except :
            print("Error. Key already exists.")
            return a_dict
    elif choice == 'r':
        try: 
            key = input('Key to remove: ')
            the_dict = remove_from_dict(key,a_dict)
        except:
            print("Key not found.")
            return a_dict
    elif choice == 'f':
        try:
            key = input('Key to locate: ')
            value = find_key(key,a_dict)
            print(value)
        except:
            print("Key not found." )
            return a_dict

    return the_dict


def add_to_dict(key,value,a_dict):
        a_dict[key] = value
        return a_dict
        

def remove_from_dict(key,a_dict):
    del a_dict[key]
    return a_dict

def find_key():
    value = a_dict[key]
    return value

def dict_to_tuples(a_dict):
    items = []
    for item in a_dict.items():
        items.append(item)
    #sorted_items = sorted(items) 
    return items  #sorted_items

def main():
    more_input = True
    a_dict = {}
    
    while more_input:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more_input = again.lower() == 'y'
    
    tuple_list = dict_to_tuples(a_dict)
    print(sorted(tuple_list))

main()


















