
rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below

if rating >= 2700 :
    print("Super grandmaster") # Do not change this line
elif rating >= 2500 and rating < 2700 :
    print("Grandmaster") # Do not change this line
elif rating >= 2400 and rating < 2500: 
    print("International") # Do not change this line
elif rating < 2400 and rating > 999 :
    print("Amateur") # Do not change this line
else 999 :
    print("Invalid") # Do not change this line