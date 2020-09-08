## dog age to human age

# ég og allt rétt

# dog_age = int(input("Input dog's age: ")) # Do not change this line
# human_age = 15
# if dog_age <= 0 or dog_age > 16:
#     print('Invalid age')
# elif dog_age == 1:
#     print('Human age:',human_age)
# elif dog_age == 2:
#     human_age += 9
#     print('Human age:',human_age)
# for i in range(3,17):
#     if i == dog_age:
#         human_age += 9
#         human_age += 4
#         print('Human age:',human_age)
#     else:
#         human_age += 4

# print('Human age:', human_age)
#while dog_age <= 16 or dog_age >= 3:


####### betri kóði og allt rétt ################ 

dog_age = int(input("Input dog's age: ")) # Do not change this line
human_age = 24

if dog_age <= 0 or dog_age > 16:
    print("Invalid age")
else:
    if dog_age == 1:  
        human_age -= 9 
    elif dog_age == 2:
        human_age=human_age
    else:
        for i in range(3,dog_age+1):
            human_age += 4 
    print("Human age:", human_age)
   




















