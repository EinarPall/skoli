#ASCII













import string
def upper_lower(some_string):
    new_string=''
    for char in some_string:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            pass
    return new_string

def main():
    letter = input('Input letter: ')
    if letter.islower():
        print(letter.upper())
    elif letter.upper():
        print(letter.lower())
    else:
        print('Not a letter')

    a_string = input('Input string: ')
    a_string = upper_lower(a_string)
    
    print(a_string)
        



main()