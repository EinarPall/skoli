# project 7 

# opnum tvær skrár, 
## þar sem fyrri inniheldur vægi námsþátta 
## og seinni einkunnir nemenda

# Fastar 
SPACE_COL_1 = 16
SPACE_OTHER_COL = 14
ROUND_GRADE = 2

# fall sem opnar skjölin
def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError: 
        return print('File {} not found'.format(filename))

# fall sem tekur parts og setur upp lista með tuples
def parts_list(file_grades):
    ''' fall sem tekur línu fyrir línu í skrá og setur upp í lista '''
    parts_list = []
    for line in file_grades:
        parts_list.append(line.strip().split(' ')) # listi 
    for weight in range(len(parts_list[1])):
        parts_list[1][weight] = float(parts_list[1][weight]) # nota þessa aðferð á fleiri stöðum
    return parts_list

# fall sem tekur lista með tveimur listum og parar saman stök með sama sæti í þeim báðum og gerir nýjan lista tuple með pörunum inn í listanum
def parts_tuple(parts_list):
    ''' fall sem parar saman stök í lista og skilar í túplum í lista ''' 
    list_tuple = []
    length = len(parts_list[0])
    for i in range(length):       
        course = parts_list[0][i]
        weights = parts_list[1][i]
        course_weight = []
        course_weight.append(course)
        course_weight.append(weights)
        list_tuple.append(tuple(course_weight))
    return list_tuple

def get_data_list(file_object):
    ''' fall sem tekur skrá og býr til lista með með nöfnum og einkunnum sem streng
        inní stórum lista ''' 
    data_list = [] 
    for line_str in file_object:
        data_list.append(line_str.strip().split('   '))    
    return data_list

def get_list_tuple_names_grades(data_list):
    ''' fall sem tekur lista með nöfnum og einkunnum, 
    float-ar einkunnir inní lista sem fer inní túplu með nöfnum inní einn stórann lista '''
    for index in data_list:
        index[1] = index[1].split(' ') # splittar einkunnum nemanda og setur upp í lista
        for num in range(len(index[1])):
            index[1][num] = float(index[1][num]) # float-ar hverja og eina einkunn
    for i in range(len(data_list)):  # túplar utan um einkunnir og nafn nemanda
        data_list[i] = tuple(data_list[i])
    return data_list

# algorithm fyrir avg útfærslu
# fall sem reiknar vegna lokaeinkunn og bætir við grades listann in í tupluna
# án þess að búa til nýjan lista
# notum partslist[1] sem er vægi
# og svo einkunnalistann
# appendum svo inní túpluna meðaltalinu

def weighted_average(list_tuple_names_grades,parts_list):
    ''' fall sem reiknar vegið meðaltal einkuna og setur uppí lista '''
    grades_list = [] 
    for i in range(len(list_tuple_names_grades)): # bý til lista með einungis grades
        grades_list.append(list_tuple_names_grades[i][1])
    weight = parts_list[1] # nær í vigt námsþátta
    weighted_average_list = []
    for grades in grades_list:
        i = 0
        avg = 0
        for grade in grades: # hver og ein einkunn nemanda reiknuð við námsþátt
            avg += grade * weight[i]
            i += 1
        weighted_average_list.append(avg)
    return weighted_average_list

# fall sem setur wgt avg inní tupluna fyrir aftan grades
def avg_grades_into_tuple(list_tuple_names_grades,wgt_avg_list):
    ''' fall sem bætir meðaleinkunn inní túpluna í stóra listanum '''
    for i in range(len(list_tuple_names_grades)):
        list_tuple_names_grades[i] += tuple([wgt_avg_list[i]]) # gera stakið að lista áður en því er breytt í túplu
    return list_tuple_names_grades


def course_assessment():
    ''' fall sem para saman námsmat og vægi þeirra úr skrá frá notenda '''
    filename_parts = input('Enter filename for parts: ') #'P7_skra1.txt' 
    file_parts = open_file(filename_parts)    
    list_parts = parts_list(file_parts)
    tuple_parts = parts_tuple(list_parts)
    return tuple_parts, list_parts

def student_grades():
    ''' fall sem parar saman nemanda og einkunnir úr skrá frá notenda '''
    filename_grades = input('Enter filename for grades: ') #'P7_skra2.txt' 
    file_grades = open_file(filename_grades)
    list_names_grades = get_data_list(file_grades)
    list_tuple_names_grades = get_list_tuple_names_grades(list_names_grades)
    return list_tuple_names_grades


def print_outcome(parts_list,list_tuple_all_info):
    ''' fall sem að prentar út niðurstöður á skýran hátt '''
    courses = parts_list[0]
    print('\n{:>{}s}'.format('Student ID',SPACE_COL_1),end = '')
    for course in courses:
        print('{:>{}s}'.format(course,SPACE_OTHER_COL),end = '') # námsþættir
    print('{:>{}s}'.format('Course grade',SPACE_OTHER_COL))
    for tuples in list_tuple_all_info:
        print('{:>{}s}'.format(tuples[0],SPACE_COL_1),end = '') # nöfn nemenda
        for grade in tuples[1]:
            print('{:>{}}'.format(grade,SPACE_OTHER_COL),end = '') # einkunnir nemenda
        print('{:>{}}'.format(round(tuples[2],ROUND_GRADE),SPACE_OTHER_COL)) # vegið meðaltal


def main():
    try:
        # skrá 1
        tuple_parts, list_parts = course_assessment()
        print(tuple_parts)
        # skrá 2
        list_tuple_names_grades = student_grades()
        print(list_tuple_names_grades)
        # reiknað meðaltal
        wgt_avg_list = weighted_average(list_tuple_names_grades,list_parts)
        list_tuple_all_info = avg_grades_into_tuple(list_tuple_names_grades,wgt_avg_list)
        print(list_tuple_all_info)
        # niðurstöður prentaðar
        print_outcome(list_parts,list_tuple_all_info)
    except TypeError:
        pass
main()
