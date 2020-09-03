# Assignment 5
# dæmi 1
# Algorithm that finds the maximum positive interger input by user.
# The user repeatedly inputs numbers until a negative value is entered.

# num_int = int(input("Input a number: "))    # Do not change this line
# # Fill in the missing code

# max_int = 0

# while num_int >= 0:
#     if num_int > max_int:
#         max_int = num_int # max_int verður að num_int ef inputtið hjá user er stærra en inputtin að undan
#         # og max_int helst þá í stærstu tölunni
#     num_int = int(input("Input a number: "))

# print("The maximum is", max_int)    # Do not change this line

# dæmi 2

# summ 3 seinsutu tölur saman til að fá næstu
#  input, hvað þú vilt fá margar tölur 
# u=+3+6+11
# print(u) = 20

n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1=1
n2=2
n3=3
if n == 1:
    print(n1)
elif n == 2:
    print(n1,n2)
elif n == 3:
    print(n1,n2,n3)
else:
    print(n1,n2,n3,end=' ')
    for i in range(4,n+1):
        n4=n1+n2+n3
        print(n4,end=' ')
        n1=n2
        n2=n3
        n3=n4
    







