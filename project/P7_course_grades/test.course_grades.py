# # import string library function  
# import string  
  
# print("Hello") 
# # Storing the characters space, tab etc 
# result = string.whitespace 
  
# # Printing the values 
# print(result) 
# print("Geeksforgeeks") 

# tup = tuple('hallo')
# print(tup)


# # eys fall - ekki í notkunn
# # def grades_to_tuple(new_list):
# #     '''Skipta einkunum upp í tuple'''
# #     grades = []
# #     for line_str in new_list:
# #         grades.append(line_str.split(','))
# #     return grades


# # inní get grades
#     int_list = []
#     for list_in_list in new_list:
#         for list_str in list_in_list:
#             int_list.append(float(list_str))
#     return int_list


# u = [['1','2','3.5','6'],['1','2.4','5.7','8']]
# k = []
# c = []
# k.append(u[0])
# for weight in u[1]:
#     c.append(float(weight))
# k.append(c) 
# print(k)


# u = [['1','2','3.5','6'],['1','2.4','5.7','8']]
# k = []
# c = []
# k.append(u[0])
# for i in range(len(u[1])):
#     u[1][i] = float(u[1][i])
#     #c.append(float(weight))
# k.append(c) 
# print(k)
# print(u)

# def avg_grades_into_tuple(list_tuple_names_grades,wgt_avg_list):
#     for i in range(len(list_tuple_names_grades)):
#         list_tuple_names_grades[i] += tuple(wgt_avg_list[i])
#         return list_tuple_names_grades



# list_tuple_names_grades = [('nemi1@ru.is', [8.7, 9.4, 7.6, 8.9, 6.9]), ('nemi2@ru.is', [9.4, 8.3, 6.7, 7.8, 8.4]), ('nemi3@ru.is', [6.5, 7.4, 8.2, 6.7, 6.9])]
# wgt_avg_list = [7.870000000000001, 8.030000000000001, 7.130000000000001]
# print(len(list_tuple_names_grades))
# for i in range(len(list_tuple_names_grades)):
#         list_tuple_names_grades[i] = list_tuple_names_grades[i] + tuple([wgt_avg_list[i]])

# print(list_tuple_names_grades)

# u = 'hello' 
# a = u.center(16)
# b = 'hello'.rjust(16) # samtals 16 með lengd orðs
# print(b)
# print('               1')

# print('{:>16s}'.format('hello'))


# e = (1,)+tuple([2])
# print(e)

# a = 222.00
# b = 2.57989
# print(a%3)
# print(b%3)
# print(float(a))
# print('{:>14.3} {:>14.3} '.format(b, a ))



u = [['nemi1@ru.is', '8.7 9.4 7.6 8.9 6.9'], ['nemi2@ru.is', '9.4 8.3 6.7 7.8 8.4'], ['nemi3@ru.is', '6.5 7.4 8.2 6.7 6.9'], ['nemi4@ru.is', '8.5 7.4 8.2 6.7 6.9']]

# for index in u:
#     index[1] = index[1].split(' ')
#     for num in index[1]:
#         index[1] = index.append(float(num))
# print(u)


for index in u:
    index[1] = index[1].split(' ')
    for num in range(len(index[1])):
        index[1][num] = float(index[1][num])
for i in range(len(u)):
    u[i] = tuple(u[i])
print(u)






