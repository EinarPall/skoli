year = int(input("Input a year: ")) # Do not change this line
breyta= False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            breyta = True
    else :
        breyta = True
print(breyta)
#true ef hlaupár
