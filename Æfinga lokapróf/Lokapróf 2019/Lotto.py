# Lokapróf 2019
# dæmi 2 

WINNING_NUMS_SPLIT = ' '
LOTTO_NUMS_SPLIT = ' '

# gefið fall
def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return False

# strengur sem bætir við stjörnu


def make_lotto_list(file_object):
    ''' fall sem setur lotto línur úr file upp í lista '''
    line_list = []
    for line in file_object:
        line = line.strip()
        line = str(line)
        # print(line)
        line_list.append(line.split(LOTTO_NUMS_SPLIT))
    # print(line_list) 
    return line_list

def mark_winning_nums(line_list,winning_nums):
    ''' fall sem merkir við vinnings tölur '''
    i = 0
    for line in line_list:
        j = 0
        for num in line:
            if int(num) in winning_nums:
                line_list[i][j] = line_list[i][j] + '*'
                j += 1
            else:
                j += 1
                pass
        i += 1
    # print(line_list)
    return line_list

def print_marked_nums(marked_num_list):
    outcome_str = ''
    for line in marked_num_list:
        for num in line:
            outcome_str += num + ' '
        outcome_str += '\n'
    return print(outcome_str.strip())


def winning_nums_valid_or_not(winning_nums):
    #print(winning_nums)
    if len(winning_nums) == 5:
        for i in range(len(winning_nums)):
            try:
                winning_nums[i] = int(winning_nums[i])
            except ValueError:
                return False
        for num in winning_nums:
            if not (num >= 1 and num <= 40 ):
                return False           # print(True)
        return True
    else:
        return False    # print(False)





def main():
    filename = input('Enter file name: ')
    file_object = open_file(filename)
    if file_object:
        winning_nums = input('Enter winning numbers: ').split(WINNING_NUMS_SPLIT)
        valid_or_not = winning_nums_valid_or_not(winning_nums)
        if valid_or_not:
            lotto_list = make_lotto_list(file_object)
            marked_num_list = mark_winning_nums(lotto_list,winning_nums)
            print_marked_nums(marked_num_list)
            #print(marked_num_list)
        else:
            print('Winning numbers are invalid!')
    
    # þetta virkar
    # if int('5') in [3, 4, 5, 6]:
    #     print(True)



main()
