def lowest_from_list(num_list):
    stripped = num_list.strip(',')
    
    lowest_num = min(num_list)
    return lowest_num

num_list = input('Input list of numbers separated by commas: ')
lowest_num = lowest_from_list(num_list)
print(lowest_num)