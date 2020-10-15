# dæmi 1

# def music_func(music = 'Classic Rock',group = 'The Beatles',singer = 'Freddie Mercury'):
#     print('The best type of music is',music)
#     print('The best music group is',group)
#     print('The best lead vocalist is',singer)

# def main():
#     music, group, singer = input("Input music, group, singer: ").split(',')
#     music_func(music, group, singer)
#     music_func()

# main()

# dæmi 2


# def remove_evens(int_list): 
#     temp_list = int_list[:] # deep copy
#     for num in temp_list:
#         if num % 2 == 0:
#             int_list.remove(num)


# def remove_evens2(int_list):
#     new_list = []
#     for num in int_list:
#         if num % 2 == 0:
#             pass
#         else:
#             new_list.append(num)
#     return new_list

# # Main starts here
# a_list = [1,2,2,3,4,5]
# print(a_list)
# remove_evens(a_list)
# print(a_list)
    
# b_list = [1,2,3,4,4,5,6,7,8,9,10]
# c_list = remove_evens2(b_list)
# print(b_list)
# print(c_list)


####### dæmi 3

def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('\nFile {} not found'.format(filename))

def list_file(file_object):
    ''' function who puts txt file into one flat list '''
    list_of_lists = []
    for line in file_object :
        stripped_line = line.strip().split(' ') 
        list_of_lists.append(stripped_line)
    return sum(list_of_lists,[])

# fall sem tekur út punctations
def no_punctuation(file_list):
    import string
    no_punc_list = []
    for list_str in file_list:
        no_punc_list.append(list_str.strip(string.punctuation))
    return no_punc_list

# fall sem tekur út 
def unic_list(file_list):
    unic_list = []
    for list_str in file_list:
        if list_str not in unic_list:
            unic_list.append(list_str)
    return unic_list
      


def main():
    filename = input('Enter filename: ')
    file_object = open_file(filename)
    file_list = list_file(file_object)
    #print(file_list)
    #print(sorted_list)
    list_no_punc = no_punctuation(file_list)
    #print(list_no_punc)
    unique_list = unic_list(list_no_punc)
    sorted_list = sorted(unique_list)
    print(sorted_list)
main()

######## dæmi 4
######## dæmi 5







