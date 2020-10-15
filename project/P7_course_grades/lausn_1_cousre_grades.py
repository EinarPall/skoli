# project 7 

# opnum tvær skrár, 
## þar sem fyrri inniheldur vægi námsþátta 
## og seinni einkunnir nemenda
# 


# 2 # fall sem opnar skjölin
def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('File {} not found'.format(filename))

# Upplýsingarnar úr skrá 1 skal lesa inn í sér falli sem skilar lista af túplum
# fall sem tekur parts og setur upp lista með tuples
def parts_list(file_grades):
    ''' fall sem tekur línu fyrir línu í skrá og setur upp í lista '''
    parts_list = []
    # tup = (,)
    for line in file_grades:
        parts_list.append(line.strip().split(' ')) # lsiti
    for weight in range(len(parts_list[1])):
        parts_list[1][weight] = float(parts_list[1][weight]) # nota þessa aðferð á fleiri stöðum
    return parts_list

# fall sem tekur lista með tveimur listum og parar saman stök með sama sæti í þeim báðum og gerir nýjan lista tuple með pörunum inn í listanum
def parts_tuple(parts_list):
    ''' fall sem parar saman stök í lista og skilar í túplum í lista ''' 
    list_tuple = []
    length = len(parts_list[0])
    for i in range(length):        # parts_list:
        course = parts_list[0][i]
        weights = parts_list[1][i]
        course_weight = []
        course_weight.append(course)
        course_weight.append(weights)
        list_tuple.append(tuple(course_weight))
    return list_tuple

# eys fall 
def get_data_list(file_object):
    ''' fall sem býr til lista með með nöfnum og einkunnum sem streng
        inní stórum lista '''
    data_list = [] 
    for line_str in file_object:
        data_list.append(line_str.strip().split('   '))    
    return data_list

def get_list_tuple_names_grades(data_list):
    for index in data_list:
        index[1] = index[1].split(' ')
        for num in range(len(index[1])):
            index[1][num] = float(index[1][num])
    for i in range(len(data_list)):
        data_list[i] = tuple(data_list[i])
    return data_list





# gera [[name][name][name]]
def name_list(data_list):
    ''' Einangra nöfn og set þær inn í einn stóran lista'''
    temp_list = []
    for line in data_list:
        temp_list.append((line[0]))
    names_list = []
    for line in temp_list:
        names_list.append(line.split(','))
    return names_list


# eys fall
def get_grades(data_list):
    ''' Einangra einkunnir og set þær inn í einn stóran lista'''
    new_list = []
    #print(data_list)
    for per_list in data_list:
        new_list.append(per_list[1].split(' '))
    grades_list = []
    for list_in_list in new_list:
        temp_list = []
        for list_str in list_in_list:
            temp_list.append(float(list_str))
        grades_list.append(temp_list)
    return grades_list

def collab(list_grades,list_names):
    ''' fall sem sameinar lista með nöfnunum og lista með einkunum,
        setur einkunnar listann inní nafna listann'''
    u = 0 
    for names in list_names:
        names.append(list_grades[u])
        u += 1
    return list_names

def tuple_collab(collab_list):
    ''' fall sem tekur lista inní lista og breytir í túplu inní listanum '''
    final_list = []
    for names_grades in collab_list:
        final_list.append(tuple(names_grades))
    return final_list

# fall sem reiknar vegna lokaeinkunn og bætir við grades listann in í tupluna
# án þess að búa til nýjan lista

# notum partslist[1] sem er vægi
# og svo einkunnalistann
# appendum svo inní túpluna meðaltalinu

def weighted_average(grades_list,parts_list):
    weight = parts_list[1]
    weighted_average_list = []
    for grades in grades_list:
        i = 0
        avg = 0
        for grade in grades:
            avg += grade * weight[i]
            i += 1
        weighted_average_list.append(avg)
    return weighted_average_list

# fall sem setur wgt avg inní tupluna fyrir aftan grades
def avg_grades_into_tuple(list_tuple_names_grades,wgt_avg_list):
    ''' fall sem bætir meðaleinkunn inní tupluna í lista '''
    for i in range(len(list_tuple_names_grades)):
        list_tuple_names_grades[i] += tuple([wgt_avg_list[i]]) # gera stakið að lista áður en því er breytt í túplu
    return list_tuple_names_grades


def part_1():
    ''' fall sem vinnur með skrá og skilar lista með tuplum '''
    filename_parts ='P7_skra1.txt' #input('Enter filename for parts: ') #'P7_skra1.txt' 
    file_parts = open_file(filename_parts)    
    list_parts = parts_list(file_parts)
    #print(list_parts)
    tuple_parts = parts_tuple(list_parts)
    #print(tuple_parts)
    return tuple_parts, list_parts

def part_2():
    ''' fall sem vinnur með uppgefna skrá skilar út ákveðnum lista '''
    filename_grades = 'P7_skra2.txt' #input('Enter filename for grades: ') #'P7_skra2.txt' 
    file_grades = open_file(filename_grades)
    list_names_grades = get_data_list(file_grades)
    #print(list_names_grades)
    #### virkar ## list_tuple_names_grades = get_list_tuple_names_grades(list_names_grades)
    #print(list_tuple_names_grades)
    list_grades = get_grades(list_names_grades)
    #print(list_grades)
    list_names = name_list(list_names_grades)
    #print(list_names)
    collab_list = collab(list_grades,list_names)
    #print(collab_list)
    list_tuple_names_grades = tuple_collab(collab_list)
    # print(list_tuple_names_grades)
    return list_tuple_names_grades, list_grades

def print_outcome(parts_list,list_tuple_all_info):
    courses = parts_list[0]
    #print(courses)
    #print(list_tuple_all_info)

    print('\n{:>16s}'.format('Student ID'),end = '')
    for course in courses:
        print('{:>14s}'.format(course),end = '')
    print('{:>14s}'.format('Course grade'))
    for tuples in list_tuple_all_info:
        print('{:>16s}'.format(tuples[0]),end = '')
        for grade in tuples[1]:
            print('{:>14}'.format(grade),end = '')
        print('{:>14.3}'.format(tuples[2]))




def main():
    # partur 1
    tuple_parts, list_parts = part_1()
    print(tuple_parts)
    ### partur 2
    list_tuple_names_grades, list_grades = part_2()
    print(list_tuple_names_grades)
    wgt_avg_list = weighted_average(list_grades,list_parts)
    #print(wgt_avg_list)
    list_tuple_all_info = avg_grades_into_tuple(list_tuple_names_grades,wgt_avg_list)
    print(list_tuple_all_info)
    print_outcome(list_parts,list_tuple_all_info)
main()
