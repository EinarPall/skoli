# Project 8
# Document Retrival
# 1 biður notnendann um document collection



def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    file_object = open(filename, "r")
    return file_object
 


def doc_sentence_list(file_object):
    ''' fall sem skiptir upp docs í lista '''
    import string
    doc_list = [[]]
    count = 0
    for line in file_object:
        line = line.lower()
        line = line.strip()
        line = line.strip(string.punctuation)
        if line == 'new document':
            doc_list.append([])
            count += 1
            pass
        else:
            doc_list[count].append(line)

        #line.strip(string.punctuation) # nota þetta þegar  við erumsdfomnir með allt sem stök orð
    return doc_list

def doc_word_list(doc_list):
    new_list = []
    for lst in doc_list:
        another_list = []
        for lst_str in lst:
            lst_str = lst_str.split(' ')
            another_list.append(lst_str)
        new_list.append(another_list)
    #print(new_list)
    third_list = []
    for u in range(len(new_list)):
        forth_list = []
        for i in range(len(new_list[u])):
            forth_list += new_list[u][i]
        third_list.append(forth_list)
    return third_list

def menu():
    print('What would you like to do?')
    print('1. Search Documents\n2. Print Document\n3. Quit Program')
    choice = input('> ')
    return choice

#def searc_for_words(words_in_list,search_words):
def searc_for_words(words_in_list,search_words):
    match_single_list = []
    #print(search_words)
    for word in search_words:
        temp_list = []
        k = 0
        for i in range(len(words_in_list)):
            for word_2 in words_in_list[i]:
                if word == word_2:
                    if i not in temp_list:
                        temp_list.append(i)
                    else:
                        pass
        match_single_list.append(temp_list)
    return match_single_list
    

def pair_search_result(match_single_list):
    ''' pair search result for every search word in document '''
    set_list = []
    if len(match_single_list) > 1 :
        for single_list in match_single_list:
            set_list.append(set(single_list))
        #print(set_list)                
        return set.intersection(*set_list)
        #print(gildi) 
        # for num in gildi:
        #     print(num)
    else: 
        return match_single_list[0]
        

def print_doc_by_choice(doc_in_lists,doc_num):
    ''' fall sem prentar út það document sem notandi velur '''
    print('Document #{}'.format(doc_num))
    for line in doc_in_lists[doc_num]:
        print(line)
    print('')


def execute_selection(choice, words_in_list, doc_in_lists):
    ''' fall sem fer inní önnu föll eftir því hvað choice er '''
    if choice == '1':
        searc_words = input('Enter search words: ').lower().split(' ')
        # fallið sem leitar að orðinu og nr hvað listarnir eru í því
        docs_with_words_list_single = searc_for_words(words_in_list,searc_words)
        docs_with_words_list_combined = pair_search_result(docs_with_words_list_single)
        if len(docs_with_words_list_combined) > 1:
            print('Documents that fit search:',end=' ')
            for num in docs_with_words_list_combined:
                print(num,end=' ')
            print('\n')
        else: 
            print('No match.\n')
            new_file_process()
        return choice
    elif choice == '2':
        doc_num = int(input('Enter document number: '))
        if doc_num > len(words_in_list):
            print('No match.\n')
            new_file_process()
        else:
            print_doc_by_choice(doc_in_lists, doc_num)
        
        return choice
    else:
        choice = '3'
        print('Exiting program.')
        return choice


def new_file_process():
    try: 
        file_name = input('Document collection: ') #'P8-1.txt'
        file_object = open_file(file_name)
        choice = '1'
        file_process(choice, file_object)
    except FileNotFoundError:
        print('Documents not found\n')
        choice = '3'
        new_file_process()


def file_process(choice, file_object):
    while choice != '3': 
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



def main():

    new_file_process()
    
main()


