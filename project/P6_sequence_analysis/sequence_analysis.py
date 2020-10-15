# Project 6
# Secuence Analysis
# greining á skrám 


# 1. forlykkja,með lengd uppá filename_list, sem runnar í gegnumn öll föllin fyrir hvert filename
# 2. opnum textaskjalið ef það er til
# 3. tökum textaskjal, breytum því í lista
# 4. tökum listann og breytum honum yfir í float og round með 4 aukastöfum, ef ekki hægt þá notar það ekki það stak
# 5. tökum floated lista og prentum út öll stökin í línu
# 6. fall sem prentar út uppsafnaða summu listans 
# 7. fall sem  flokkar listann og prentar hann út
# 8. fall sem finnur miðgildið í listanum 

# round fasti 

# 2 # fall sem opnar skjalið
def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('\nFile {} not found'.format(filename))

# 3 fall sem tekur textaskrá og setur upp í lista
def list_txt(file_object):
    list_of_lists = []
    for line in file_object :
        stripped_line = line.strip() # hér er hægt að int-a til að fá tölur í txt ekki sem strengi
        list_of_lists.append(stripped_line)
    return list_of_lists

# 4 breyta lista yfir í floated lista
def list_floated(file_list):
    file_list_floated = []
    for num in file_list:
        try:
            file_list_floated.append(float(num))
            file_list_floated.append(round(num,4))
        except: # ef það er ekki hægt að float-a þetta stak, þá er því slept í nýja listanum
            pass
    return file_list_floated


# 5 fall sem prentar út listann
def sequence(list_object):
    print('\tSequence:') 
    print('\t\t',end='')
    for num in list_object:
        print(num,end=' ')
    return


# 6 fall sem prentar út uppsafnaða summu listans
def cumulative(list_object):
    print('\tCumulative sum:'); print('\t\t',end='')
    try : 
        cumsum = 0; cumsum_list = []
        for num in list_object:
            cumsum += num
            cumsum = round(cumsum,4)
            print(cumsum,end=' ')
        return 
    except: # ef listinn er tómur
        return print('')


# 7 fall sem flokkar listann og prentar hann út (sorter tölur frá mínus í plús)
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

# 8 fall sem finnur miðgildið í listanum 
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


# 1
# Main program starts here 
def main():
    filename_list = input("Enter filenames: ").split()
    for filename in filename_list:
        try: 
            file_object = open_file(filename) # opnar textaskrána í read mode
            file_list = list_txt(file_object) # breytir textaskránum í lista með allt sem strengi
            list_float = list_floated(file_list)    # setur allt sem hægt er að int-a í strengnum í nýja lista
            print('\nFile',filename)
            list_squence = sequence(list_float)  # prentar út öll stök í listanum
            print('')
            list_cumsum = cumulative(list_float) # reiknar uppsafnaða summu stakana og prentar út
            print('')
            list_sorted = sort_sequence(list_float) #  flokkar öll gildin í listanum í stærðarröð og prentar út, minnst yfir í stærst
            print('')
            median = list_median(list_float) # fallið sem finnur miðgildið í listanum
        except: # ef skjalið finnst ekki eða er ekki til, en nær samt að runna open_file fallið sem skilar prentskipun um að það sé ekki til
            pass
main()







