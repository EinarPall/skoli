# dæmi 1

# sentence = input('Input a sentence: ')

# sentence_list = list(sentence)
# print(sentence_list)
# sentence_list.sort()
# print(sentence_list)


# dæmi 2
import string

# Implement a function here
def no_punctuation(sentence):
    no_punc =''
    #u = ''.join(set(sentence))
    for char in sentence:
        if char not in string.punctuation:
            # sentence.remove(char)
            no_punc = no_punc + char
    return no_punc

# def no_whitespace(sentence):
#     no_whitespace = ''
#     for char in sentence:
#         if char not in string.whitespace:
#             no_whitespace += char 
#     return no_whitespace

# def no_duplicate(sentence):
#     #u = ''.join(set(sentence))
#     sentence = ''.join([j for i,j in enumerate(sentence) if j not in sentence[:i]])
#     return sentence

# def unique_string(sentence):
#     no_punc = no_punctuation(sentence)
#     no_white_punc = no_whitespace(no_punc)
#     no_white_punc_duple = no_duplicate(no_white_punc)
#     unique_list = list(no_white_punc_duple)
#     return unique_list


# def main(): # Main starts here
#     sentence = input("Input a sentence: ")
#     unique_letters = unique_string(sentence)
#     print("Unique letters:", unique_letters)
# main()

### dæmi 3

def input_words(word):
    #word = input('Enter word to be added to list: ')
    word_list = []
    while word != 'x':
        word_list.append(word)
        word = input('Enter word to be added to list: ')
    return word_list

# def print_list(word_list):
#     for word in word_list:
#         print(word)

def sort_out(word_list):
    for i in word_list:
        if i[0] == i[-1] and len(i) > 1:
            print(i)
    return i

def main():
    word = input('Enter word to be added to list: ')
    word_list = input_words(word)
    print(word_list)
    final_list = sort_out(word_list)
    #print_list(word_list)
main()



##### dæmi 4




























