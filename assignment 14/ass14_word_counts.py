# assignment 14 

# dæmi 2

def get_word_list(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    list_of_words = []
    for line in file_object:
        stripped_line = line.strip().split(' ') 
        for word in stripped_line:
            list_of_words.append(word.lower())
    import string
    no_punc_list = []
    for list_str in list_of_words:
        no_punc_list.append(list_str.strip(string.punctuation))
    return no_punc_list

def word_list_to_counts(word_list):
    word_count_dict = {i:word_list.count(i) for i in word_list} # af netinu
    return word_count_dict

def dict_to_tuples(word_count_dict):
    items = []
    for item in word_count_dict.items():
        items.append(item)
    #sorted_items = sorted(items) 
    return items  #sorted_items


def main():
    filename = 'ass14.txt'     #input("Name of file: ")
    file_object = open(filename)
    word_list = get_word_list(file_object)
    #print(word_list) 
    file_object.close()
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list)
    #print(word_count_dict)
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuples(word_count_dict)
    #print(word_count_tuples)
    print(sorted(word_count_tuples))
    
main()
