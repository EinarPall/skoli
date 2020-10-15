# for i in range(10):
#     print(i, end=' ')

#a_file = open("P6_data1.txt")

# lines = a_file.readlines()
# for line in lines:
#     print(line,end=' ')


# u = list(a_file)
# print(u)

#row = [[]] 
#crimefile = open(fileName, 'r') 
# for line in a_file.readlines(): 
#     tmp = []
#     for element in line[0:-1].split(','):
#         tmp.append(element)
# row.append(tmp)

# print(tmp)


# a_file = open("sample.txt", "r")

# virkar 
# list_of_lists = []
# for line in a_file:
#   stripped_line = line.strip() # hér er hægt að int-a til að fá tölur í txt ekki sem strengi
#   #line_list = stripped_line.split()
#   list_of_lists.append(stripped_line)

# # a_file.close()   lokar textaskránni

# print('\t',list_of_lists)

# 1
def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('\nFile {} not found'.format(filename))
# 2 _
def list_txt(file_object):
    list_of_lists = []
    for line in file_object :
        stripped_line = line.strip() # hér er hægt að int-a til að fá tölur í txt ekki sem strengi
        #line_list = stripped_line.split()
        list_of_lists.append(stripped_line)
    return list_of_lists

# 3 breyta í float í breytu heitum
def list_int(file_list):
    file_list_int = []
    for num in file_list:
        try:
            file_list_int.append(float(num))
            file_list_int.append(round(num,4))
        except: # ef það er ekki hægt að float-a þetta stak, þá er því slept í nýja listanum
            pass
    return file_list_int


# 4
def sequence(list_object):
    print('\tSequence:') 
    print('\t\t',end='')
    for num in list_object:
        print(num,end=' ')
    return


# 5 
def cumulative(list_object):
    print('\tCumulative sum:')
    print('\t\t',end='')
    try : 
        cumsum = 0
        cumsum_list = []
        for num in list_object:
            cumsum += num
            cumsum = round(cumsum,4)
            print(cumsum,end=' ')
            #cumsum_list.append(cumsum)
        return #print(cumsum_list)
    except:
        return print('')


# 6 
def sort_sequence(list_object):
    print('\tSorted sequence:')
    print('\t\t',end='')
    try:
        sort = sorted(list_object)
        for num in sort:
            print(num, end=' ')
        return
    except:
        return print('') 

def list_median(list_object):
    print('\tMedian:')  
    print('\t\t',end='')
    import statistics
    try:
        median = statistics.median(list_object)
        median_rounded = round(median,4)
        return print(median_rounded)
    except:
        return print('')

# prufun á byrjun í kóða
def main():
    filename_list = input("Enter filenames: ").split()
    #print(filename_list)
    for filename in filename_list:
        try: 
            file_object = open_file(filename) # opnar textaskrána í read mode
            file_list = list_txt(file_object) # breytir textaskránum í lista með allt sem strengi
            # 2.
            list_float = list_int(file_list)    # setur allt sem int í strengnum
            #print(list_float)
            print('\nFile',filename)
            list_squence = sequence(list_float)  # prentar út öll stök í listanum
            print('')
            list_cumsum = cumulative(list_float) # reiknar uppsafnaða summu stakan og prentar út
            print('')
            list_sorted = sort_sequence(list_float) #  flokkar öll gildin í listanum í stærðarröð og prentar út, minnst yfir í stærst
            print('')
            median = list_median(list_float)
        except: 
            pass
        
        

main()
# P6_data1.txt P6_data2.txt 