## assigmnet 15

# dæmi 3

def open_file(filename):
    ''' fall sem opnar skrá sem notandi velur '''
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError: 
        return print('Documents not found')
    

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


def pair_all_words(word_list):
    #bigrams = [b for l in word_list for b in zip(l.split(",")[:-1], l.split(",")[1:])]
    #return bigrams
    tuple_list = []
    for word_nr in range(len(word_list[0])*2): # lengdin þarf að vera fjöldi orða í word_list
        tuple_list.append(tuple([word_list[word_nr-1], word_list[word_nr]]))
        tuple_list.append(tuple([word_list[word_nr], word_list [word_nr+1] ]))
    return tuple_list

def dict_tuples(tuple_list):
    the_dicht = dict()
    count = 1
    for tup in tuple_list:
        if tup not in the_dicht:
    	    the_dicht[tup] = count
        else:
            the_dicht[tup] += 1
    return the_dicht





def main():
    file_name = 'D3_ass15.txt'         #input('Enter name of file: ')
    file_object = open_file(file_name)
    no_punc_list = get_word_list(file_object)
    print(no_punc_list)
    paired_tuples = pair_all_words(no_punc_list)
    print(paired_tuples)
    dicht_tup = dict_tuples(paired_tuples)
    print(dicht_tup)
main()


[(('a', 'short'), 2), (('here', 'is'), 2), (('file', 'only'), 1), (('is', 'a'), 1), (('line', 'here'), 1), (('only', 'a'), 1), (('short', 'file'), 1), (('short', 'line'), 1)]



# text = ["this is a sentence", "so is this one"]
# bigrams = [b for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
# print(bigrams)
#[('this', 'is'), ('is', 'a'), ('a', 'sentence'), ('so', 'is'), ('is', 'this'), ('this', 'one')]












