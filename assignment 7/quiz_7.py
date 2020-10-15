#### úr tíma 15-09-2020

# def inc(num,alli): # fallið inc með num parameter
#     result = num + alli
#     return result # fjöll eiga að hafa skýr hlutverk

# number = int(input('Enter a number: '))
# alli = 5 
# number_incremented = inc(number,alli) # number = argument 
# print(number_incremented)




### quiz 7 #####

# def make_odd(n):
#     return 2*n - 1

# print(1 + make_odd(3))



# def func(x):
#     total = 0
#     for i in range(x)
#         total += i * (i-1)
#     return total

# print(func(4))


# string ='hallo'
# u = string[::-1]
# print(u)

# ekki ég dæmi 5

def palindrome(input_str):
    import string
    modified_str = input_str.lower()
    bad_chars = string.whitespace + string.punctuation
    for char in modified_str:
        if char in bad_chars:
            modified_str = modified_str.replace(char,'')
    if modified_str == modified_str[::-1]:
        print('"{}" is a palindrome.'.format(input_str))
    else:
        print('"{}" is not a palindrome.'.format(input_str))
    return

in_str = input("Enter a string: ")
palindrome(in_str)



