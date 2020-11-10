# lokapróf 2019
# dæmi 1
# bókstafir ekki leyfðir

 
STRING_FORMAT = 'X-XXX-XXXXX-X' # x eru tölur
STRING_SPLIT = '-'
STRING_PART = [1,3,5,1]
# STRING_PART1 = 1
# STRING_PART2 = 3
# STRING_PART3 = 5
# STRING_PART4 = 1

def isbn_valid_or_not(isbn_str):
    ''' fall sem athugar hvort strengur sé rétt upp byggður'''
    split_list = isbn_str.split(STRING_SPLIT)
    #print(split_list)
    len_list = []
    for i in range(len(split_list)): 
        if split_list[i].isnumeric():
            len_list.append(len(split_list[i]))
        else:
            return print('Invalid format!')

    #print(len_list)
    if len_list == STRING_PART: # ef lengdar listinn er alveg eins og hann að ver    # [STRING_PART1,STRING_PART2,STRING_PART3,STRING_PART4]:
        return print('Valid format!')
    else:
        return print('Invalid format!')



def main():
    isbn_str = ' just for starting'
    while isbn_str != 'q':
        isbn_str = input('Enter an ISBN: ')
        if isbn_str != 'q':
            isbn_valid_or_not(isbn_str)
    
main()

# allt grænt í testcase 

