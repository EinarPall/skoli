
################# allt sewm við reyndum fyrir fall 2 #########################

def get_word_list(file_object):
    ''' fall sem tekur textaskrá og setur orð uppí list með no punc '''
    finale = []
    doc_list = []
    for line in file_object:
        doc_list.append(line.strip('\n'))
    for line in doc_list:
        finale.append(line.split('<NEW DOCUMENT>'))
    return doc_list.strip

# Python3 code to demonstrate 
# Split list into lists by particular value 
# Using list comprehension + zip() + slicing + enumerate() 

# # initializing list 
# test_list = ['hello','mamma', 'new doc', 'eysteinn', 'er', 'hetjan í hverfinu']

# # printing original list 
# print("The original list : " + str(test_list)) 

# # using list comprehension + zip() + slicing + enumerate() 
# # Split list into lists by particular value 
# size = len(test_list) 
# idx_list = [idx + 1 for idx, val in
# 			enumerate(test_list) if val == 'new doc'] 


# res = [test_list[i: j] for i, j in
# 		zip([0] + idx_list, idx_list +
# 		([size] if idx_list[-1] != size else []))] 

# # print result 
# print("The list after splitting by a value : " + str(res)) 

# res.__delitem__('new doc')
# print(str(res))


    # another_list = []
    # for list_str in some_list:
    #     list_str = list_str.split('<NEW DOCUMENT>')
    #     another_list.append(list_str)
    # shit_list = []
    # for line in file_object:
    #     while line != '<NEW DOCUMENT>':
    #         shit_list.append(line.strip())
    return some_list


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
u = ['a'] + ['b']
print(u)

############################# allt sem við reyndum fyrir fall 3 #####################


u = []
#print(u[0])
print(len(u))
#for i in range(4):
    #print(i)

def set_list_intersection(set_list):
  if not set_list:
    return set()
  result = set_list[0]
  for s in set_list[1:]:
    result &= s
  return result

set_list = [set([1, 2]), set([1, 3]), set([1, 4]), set([1, 4])]
print(set_list_intersection(set_list))
# Output: set([1])


