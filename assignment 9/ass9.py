# # assignment 


# ############# dæmi 1

# def open_file(filename):
#     file_object = open(filename, "r")
#     return file_object

# def read_file(file_object):
#     for line in file_object:
#         line = line.strip()
#         line = line.replace(' ','')
#         print(line, end=(''))

# # main program
# def main():
#     filename = input('Enter filename: ')
#     file_object = open_file(filename)
#     read_file(file_object)
# main()

# ################ dæmi 2

# def is_float(s):
#     try: 
#         float(s)
#         return True
#     except ValueError:
#         return False


# print(is_float('3.45'))
# print(is_float('abc'))


################ dæmi 3

# def divide_safe(num1_str,num2_str):
#     try:
#         result = round(float(num1_str)/float(num2_str),5)
#         return result
#     except ValueError:
#         return None
#     except ZeroDivisionError:
#         return None

# num1_str = input('Input first number: ')
# num2_str = input('Input second number: ')

# result = divide_safe(num1_str, num2_str)
# print(result)

########### dæmi 4

def open_file(filename):
    try: 
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return False

def find_longest(file_object):
    longest = ''
    for line in file_object:
        if len(line) > len(longest):
            longest = line
        else:
            pass
    return longest


# Main program starts here
def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object:
        longest_word = find_longest(file_object)
        print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
        file_object.close()
    else:
        print("File not found")
main()

# ############## eysteinn dæmi 4
# def open_file(filename):
#     try:
#         return open(filename,'r')
#     except FileNotFoundError:
#         return False

# def find_longest(file_object):
#     longest_word = ''
#     words = ''
#     for line in file_object:
#         words += line
#     words = words.split()
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#         else:
#             pass
#     return longest_word

# # Main program starts here
# filename = input("Enter filename: ")
# file_object = open_file(filename)

# if file_object:
#     longest_word = find_longest(file_object)
#     print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
#     file_object.close()
# else:
#   print("File not found")



# ########### dæmi 5

# filename = input("Enter filename: ")
# with open(filename, 'r') as file_object:
#     contents = file_object.read()

# print(contents.replace(" ","\n"))

