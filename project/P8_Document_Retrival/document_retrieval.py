# Project 8
# Document Retrival
# 1 biður notnendann um document collection
import string

#Fastar
DOC_SPLITTED = '<NEW DOCUMENT>'

def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    file_object = open(filename, "r")
    return file_object


def doc_sentence_list(file_object):
    ''' fall sem skiptir docs upp í lista '''
    doc_list = [[]]
    count = 0
    for line in file_object:
        #line = line.lower()
        line = line.strip()
        if line == DOC_SPLITTED:
            doc_list.append([])
            count += 1
            pass
        else:
            doc_list[count].append(line)

        #line.strip(string.punctuation) # nota þetta þegar  við erum komnir með allt sem stök orð
    return doc_list #Doc_list er listi þar sem hvert doc hefur hverja setningu sem lista í lista

def doc_word_list(doc_list):
    ''' Fall sem tekur allar línur í doc og sameinar í einn lista þar sem öll orð eru stakir strengir í einum stórum lista með hinum docs'''
    new_list = []
    for lst in doc_list:
        another_list = []
        for lst_str in lst:
            lst_str = lst_str.strip(string.punctuation)
            lst_str = lst_str.lower().split(' ')
            another_list.append(lst_str) #another_list er listi þar sem hver lína í doc er listi með stökum orðum inní another_list
        #print(another_list)
        new_list.append(another_list) #new_list er þar sem another_lists koma saman í einn lista
    #print(new_list)
    words_in_list_for_doc = []
    for u in range(len(new_list)): #Hversu mörg doc eru í textaskjalinu
        temp_list = []
        for i in range(len(new_list[u])): #Hversu margar línur eru í document númer u
            temp_list += new_list[u][i] #Sameinar línur, línur eru stök orð sem strengir, fyrir hvert doc í temp_list
        #print(temp_list)
        words_in_list_for_doc.append(temp_list) #Öll orð í doc sem stök í einum lista í stórum lista
    #print(words_in_list_for_doc)
    return words_in_list_for_doc

def menu():
    ''' prentar út valmöguleika fyrir textaskránna'''
    print('What would you like to do?')
    print('1. Search Documents\n2. Print Document\n3. Quit Program')
    choice = input('> ')
    return choice


def searc_for_words(words_in_list,search_words):
    ''' fall sem leitar að orðum í hverju skjali fyrir sig og skilar út lista með lista fyrir hvert leitarorð, með númerum af docs
    þar sem leitarorð finnst. ''' 
    match_single_list = []
    #print(search_words)
    for word in search_words: 
        temp_list = []
        for i in range(len(words_in_list)):
            for word_2 in words_in_list[i]: #word_2 öll orð sem koma fram í doc númer i
                if word == word_2:
                    if i not in temp_list: #Þarf ekki að taka fram ef orðið kemur oftar en einu sinni fyrir í doc
                        temp_list.append(i)
                    else:
                        pass
        match_single_list.append(temp_list) #Listi inn í lista þar sem númer á docs þar sem leitarorð finnst
    return match_single_list 
    

def pair_search_result(match_single_list):
    ''' fall sem parar saman í hvaða skjölum leitarorðin eru, þar sem orðin verða að vera sameiginleg.
        Skilar út lista með númeri/um á docs, þar sem öll leitaorðin eru í '''  
    set_list = []
    if len(match_single_list) > 1 : #Ef fleiri en eitt leitarorð, þarf að finna sniðmengi fyrir númer doc
        for single_list in match_single_list:
            set_list.append(set(single_list))
        result = set_list[0] # viðmiðunar set 
        for s in set_list[1:]:
            result &= s # intersection viðmiði við öll hin settin
        return sorted(result)
        #print(set_list)                
    else: 
        return sorted(match_single_list[0]) #Ef eitt leitarorð, þá öll númer á öllum skjöl um þar sem það finnst. #[0] út af lista inn í lista


def print_doc_by_choice(doc_in_lists,doc_num):
    ''' fall sem prentar út það document sem notandi velur '''
    print('Document #{}'.format(doc_num))
    for line in doc_in_lists[doc_num]:
        print(line)
    print('')


def execute_selection(choice, words_in_list, doc_in_lists):
    ''' fall sem sem frakvæmir aðgerð á docs að ósk notanda'''
    if choice == '1':
        searc_words = input('Enter search words: ').lower().split(' ')
        # fallið sem leitar að orðinu og nr hvað listarnir eru í því
        docs_with_words_list_single = searc_for_words(words_in_list,searc_words)
        docs_with_words_list_combined = pair_search_result(docs_with_words_list_single)
        if len(docs_with_words_list_combined) > 0: # ef docs with wordslist combined er tómur ss. leitarorð fannst ekki í neinu doc
            print('Documents that fit search:',end=' ')
            for num in docs_with_words_list_combined:
                print(num,end=' ')
            print('\n')
        else: 
            print('No match.\n')
        return choice
    elif choice == '2':
        doc_num = int(input('Enter document number: '))
        if doc_num > len(words_in_list): # ef reynt er að prenta út doc sem er ekki til, lengd af words_in_list er fjöldi docs í skjali
            print('No match.\n')
        else:
            print_doc_by_choice(doc_in_lists, doc_num)
        return choice
    else:
        choice = '3'
        print('Exiting program.')
        return choice



def new_file_process():
    ''' fall sem athugar hvort file sé til '''
    try: 
        file_name = input('Document collection: ') #'P8-1.txt'
        file_object = open_file(file_name)
        choice = '1' # viljum setja í gang while lykkju inní main fallinu
        file_object.close()
        return choice, file_object, file_name # þurfum allt þetta í main
    except FileNotFoundError: 
        print('Documents not found.')
        choice = '3' # viljum hætta hér, ekki setja í gang while lykkju
        return choice, None, None 



def main():
    choice, file_object, file_name = new_file_process()
    #  

    while choice != '3': 
        file_object = open_file(file_name)
        # menu
        choice = menu()
        # fall 2
        doc_in_lists = doc_sentence_list(file_object)
        #print(doc_in_lists)
        # fall 3
        words_in_list = doc_word_list(doc_in_lists)
        #print(words_in_list)
        # vinnur með choice
        choice = execute_selection(choice,words_in_list, doc_in_lists)
        # print(search_match_list)
        file_object.close()

main()