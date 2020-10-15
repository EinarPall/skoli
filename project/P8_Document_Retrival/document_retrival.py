# Project 8
# Document Retrival
# 1 biður notnendann um document collection 



def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError: 
        return print('Documents not found')


def get_word_list(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    finale = []
    doc_list = []
    for line in file_object:
        doc_list.append(line.strip('\n'))
    for line in doc_list:
        finale.append(line.split('<NEW DOCUMENT>'))
    return doc_list


def get_word_list2(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    finale = []
    doc_list = []
    doc_list.append(file_object.strip('<NEW DOCUMENT>'))
        #doc_list.append(line.strip('<NEW DOCUMENT>').strip())
    return doc_list

def get_word_list3(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    finale = []
    doc_list = []
    doc_list.append(file_object.split('<NEW DOCUMENT>'))
        #doc_list.append(line.strip('<NEW DOCUMENT>').strip())
    return doc_list




def get_word_list_OG(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    list_of_words = []
    for line in file_object:
        stripped_line = line.strip('<NEW DOCUMENT>').strip('\n').split(' ') 
        for word in stripped_line:
            list_of_words.append(word.lower())
    import string
    no_punc_list = []
    for list_str in list_of_words:
        no_punc_list.append(list_str.strip(string.punctuation))
    
    #new_list = []
    #new_list.append(no_punc_list.split('document'))
    # for a in no_punc_list:
    #     new_list.append(a.split('document'))
    return no_punc_list #new_list #no_punc_list





def main():
    file_name = 'P8-1.txt'         #input('Document collection: ')
    file_object = open_file(file_name)
    doc_in_lists = get_word_list3(file_object)
    print(doc_in_lists)
main()


