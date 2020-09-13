
 # úr vídjó úr tíma

string = 'Forr itun'
string[0]
string[1]
string[3:6] # sjött stafur ekki með
ord('a')
chr(97)

for ch in string:
    print(ch)


string2 = 'skemtilegt'

string + ' ' + string2
'a' * 3 # enduartekning
string2 = 'K' + string[1:-1]
print(string2)
string2 = 'K' + string[1:]
print(string2)

print(string.upper())
print(string.split()) # splittar í lista því það er bil í strengnum
# print(string.) alskonar eftir punkt til

test_str = 'this is the first item {}, this is the second {}'.format('hello',2) 
print(test_str)


#  hér byrjar quizið 

# message = 'Beautiful weather!'
# print(message[7])

# message = 'Beautiful weather!'
# print(message[:-2])

# "programming"[4:]

# my_str = "A test string"
# #my_str[-1] = "G"

# print('hello'*2)

# u = chr(ord('P'))
# print(u)


# my_str = input("Input a string: ")
# index = 0
# result = 'a' 

# while index < len(my_str)-1:
#     if my_str[index] < my_str[index+1]:
#         result = result * 2
#     else:
#         result = result + my_str[index]
#     index += 1
# print(result)


# message = 'Beautiful weather!'
# print(message[7])


















