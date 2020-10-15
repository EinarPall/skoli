# hlutapróf 2 6-10-2020
##

# dæmi3-5

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

# fall sem sem reynir að inta allt í fallinu en halda sama lista formi
def int_numbers(data_list):
    int_data_list = []
    for lists in data_list:
        str_list = []
        for list_str in lists:
            try:
                str_list.append(int(list_str))
                #int_data_list.append(int(list_str))
            except:
                str_list.append(list_str)
        int_data_list.append(str_list)
    return int_data_list


# 1 aðalforritið
def main():
    try:
        filenmae = input('Enter file name: ')
        file_object = open_file(filenmae)
        data_list = get_data_list(file_object)
        int_data_list = int_numbers(data_list)
        print(int_data_list[:2]) # vil bara sjá fyrstu 2 listana(línurnar) í listanum
    except:
        pass
main()





