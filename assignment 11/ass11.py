


# #list_to_int_tuple function goes here
# def list_to_int_tuple(file_list):
#     file_list_int = []
#     for num in file_list:
#         try:
#             file_list_int.append(int(num))
#         except: # ef það er ekki hægt að float-a þetta stak, þá er því slept í nýja listanum
#             pass
#     return tuple(file_list_int)

# # Main program starts here - DO NOT change it
# a_list = input("Enter elements of list separated by commas: ").strip().split(',')
# a_tuple = list_to_int_tuple(a_list)
# print(a_tuple)

## dæmi 2

# def get_list():
#     a_list = input("Enter elements of list separated by commas: ").strip().split(',')
#     a_list = [int(i) for i in a_list]
#     return a_list

# def even_sum(a_list):
#     total = 0
#     for num in a_list:
#         if num % 2 == 0:
#             try:
#                 total += num
#             except:
#                 pass
#         else:
#             pass
#     return total

# # Main program starts here - DO NOT change it
# a_list = get_list()
# print(even_sum(a_list))

#dæmi 3
# def get_emails():
#     mail = input('Email address: ')
#     mail_list = []
#     while mail != 'q':
#         mail_list.append(mail)
#         mail = input('Email address: ')
#     return  mail_list

# def get_names_and_domains(email_list):
#     new_list = []
#     for mail in email_list:
#         list(mail)
#         split_list = mail.split('@') 
#         new_list.append(tuple(split_list))
#     return new_list

# # Main program starts here - DO NOT change it

# email_list = get_emails()
# print(email_list)
# names_and_domains = get_names_and_domains(email_list)
# print(names_and_domains)



# a = 'einar@hr'
# aa = list(a)
# b = aa.split('@')[1]
# print(b)

# s = "I<3 cs"
# list(s)
# print(s.split('<'))

# virkar ekki
    # #names_domains = []
    # # for mail in email_list:
    # #     #names_and_domains = 
    # for i in range(len(email_list)):
    #     email_list.split('@')
    # return email_list                 # email_list #names_and_domains



# dæmi 4

def input_floats(a_list):
    if len(a_list) >= 2:
        return a_list
    else:
        return print('At least two scores needed!')

def list_floated(a_list):
    file_list_floated = []
    for num in a_list:
        file_list_floated.append(float(num))
    return file_list_floated

def sorted_list(a_list):
    sort_list = sorted(a_list)
    return sort_list

def sum_minus_two_lowest(sort_list):
    return sum(sort_list[2:])

def main():
    a_list = input("Enter scores separated by space: ").strip().split(' ')
    start_list = input_floats(a_list)
    floated_list = list_floated(start_list)
    sort_list = sorted_list(floated_list)
    print('Sum of scores (two lowest removed):',sum_minus_two_lowest(sort_list))
main()









