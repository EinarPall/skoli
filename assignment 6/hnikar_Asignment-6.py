# # Dæmi 1
# a_str = input("Input a string: ")
# print(a_str[0]+' '+a_str[-1])
# # Dæmi 2
# a_str = input("Input a string: ")
# print(a_str[-2:]+a_str[0:-2])
# # Dæmi 3
# a_str = input("Input a string: ")
# lower = sum(1 for c in a_str if c.islower())
# upper = sum(1 for c in a_str if c.isupper())
# num = sum(1 for c in a_str if c.isdigit())
# print('count of lowercase letters',lower)
# print('count of uppercase letters',upper)
# print('count of numers',num)
# # Dæmi 4
# a_str = input("Input a float: ")
# a_float=float(a_str)
# print('{:>12.2f}'.format(a_float))
# # Dæmi 5
a_str = input("Input a string: ")
counter=0
counter2=1
for ch in a_str:
    if ch != '.' and ch != ',' and ch != ' ' and ch != '-':
        counter=counter+1
        print('j')
    if ch==' ':
        counter2=counter2+1
        print('h')
print('No. of letters: {}, no. of words: {}'.format(counter,counter2))
# # Dæmi 6
# name = input("Input a name: ")
# nafn=name.split()
# fornafn=nafn[1]
# forn=fornafn[0].upper()+". "

# eftirnafn=nafn[0]
# eftirn=eftirnafn[0].upper()+eftirnafn[1:-1]

# print(forn+eftirn)
# # Dæmi 7
# my_int = int(input('Give me an int >= 0: '))
# bin_str=''
# my_int2=my_int
# if my_int==0:
#     bin_str='0'
# while my_int2 >= 1:
#     counter=my_int2%2
#     my_int2=my_int2//2
#     bin_str=str(counter) + bin_str
    
# print("The binary of {} is {}".format(my_int,bin_str))
