# def menu():
#     print('1: Compute the sum of 1..n')
#     print('2: Compute the product of 1..n')
#     print('9: Quit')
#     choice = input('Choice: ')
#     n_str = input('Enter value for n: ')
#     return choice,n_str

# a,b = menu
# print(a,b)



# 2 # fall sem opnar skjalið
def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('File {} not found'.format(filename))

# 2  fall sem setur upp í lista fyrstu tvær línurnar
def get_data_list(file_object):
    data_list = [] # list list string er uppbyggingin
    for line_str in file_object:
        data_list.append(line_str.strip().split('\t')) # tab á milli í gögnunum
    return data_list 


def int_numbers(data_list):
    int_data_list = []
    for lists in data_list:
        for list_str in lists:
            str_list = []
            try:
                # str_list.append(int(list_str))
                int_data_list.append(int(list_str))
            except:
                int_data_list.append(list_str)
    return int_data_list



# 1 aðalforritið
def main():
    try:
        filenmae = input('Enter file name: ')
        file_object = open_file(filenmae)
        data_list = get_data_list(file_object)
        int_data_list = int_numbers(data_list)
        print(int_data_list) # vil bara sjá fyrstu 2 listana(línurnar) í listanum
    except:
        pass
main()
