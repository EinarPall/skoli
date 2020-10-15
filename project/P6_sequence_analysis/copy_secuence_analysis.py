# Project 6
# Secuence Analysis
# greining á skrám 


# 1. eitthvað sem finnur út hvað margar textaskrár voru settar inn
# kanski for lykkja með lengd uppá filename_list og fer svo í gegnum öll hin föllin fyrir það skjal
# 1.  tökum textaskjal, breytum því í lista
# 2.  tökum listann og breytum honum yfir í int og round með 4 aukastöfum, ef ekki hægt þá notar það ekki það stak
# 3.  

# fall sem opnar skjalið
# fall sem tekur textaskrá og setur upp í lista
# fall sem sorter tölur frá mínus í plús
# fall sem prentar út allar línurnar í einni línu



# fall sem opnar skjalið
def open_file(filename):
    file_object = open(filename, "r")
    return file_object


# fall sem tekur textaskrá og setur upp í lista
def list_txt(file_object):
    list_of_lists = []
    for line in file_object :
        stripped_line = line.strip() # hér er hægt að int-a til að fá tölur í txt ekki sem strengi
        #line_list = stripped_line.split()
        list_of_lists.append(stripped_line)
    return list_of_lists
# a_file.close()   lokar textaskránni

# print(list_of_lists)





# def open_file(filename):
#     try: 
#         file_object = open(filename, "r")
#         return file_object
#     except FileNotFoundError:
#         return False

# fall sem sorter tölur frá mínus í plús
def sort_sequence(file_object):
    sort = sorted(file_object)
    return sort

#print(sort_sequence(file_object))

def cumulative(file_object): 
    cu_list = [] 
    length = len(file_object) 
    cu_list = [sum(file_object[0:x:1]) for x in range(0, length+1)] 
    return print(cu_list[1:])


# def sequence(file_object):
#     for line in file_object:
#         print(line, end=' ')
#     return 

# fall sem prentar út allar línurnar í einni línu
def sequence(file_object):
    for line in file_object:
        line = line.strip() # tekur bil fyrir framan og aftan í hverri línu í .txt
        line = line.replace('\n','') # losna við new line úr textaskránni
        line = float(line)
        line = round(line,4)
        print(line, end=' ')




def main():
    
    filename = 'P6_data1.txt' #input("Enter filename: ")
    print('File',filename)
    file_object = open_file(filename)
    
    file_list = list_txt(file_object)
    print(file_list)

    print('\tSequence:') # kanski hafa þetta í falli 
    print('\t\t',end='') # kanski hafa þetta í falli 
    file_sequence = sequence(file_object)
    # print('')
    # print('\tCumulative sum:')
    # print('\t\t',end='')
    # file_cumulative = cumulative(file_object)
    print('')
    print('\tSorted sequence:')   # hér er hægt að skrifa \t til að fá tab bil
    print('\t\t',end='')
    file_sorted = sort_sequence(file_object)
    print(file_sorted)


main()








# Main program starts here
filename_list = input("Enter filenames: ").split()
process_all_files(filename_list)






