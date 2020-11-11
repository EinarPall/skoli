
DONE = 'd'
REMOVE_CHOICE = 'r'
NEW_ZERO = 'nz'

#a = [[1,2,3], [4,0,5], [6,7,8]]
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [12, 13, 14, 15]]
print(a[0].index(1))

offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]
x_offset = [(-1, 0), (1, 0)]
y_offset = [(-1, 0), (1, 0)]

# fall til að velja offsett eftir staðsetningu
def choice_offset(zero_position):
    x = zero_position[0]
    y = zero_position[1]
    offset = []
    if x == 4 or x == 0:
        if x == 4:
            offset.append((-1,0))
        if x == 0:
            offset.append((1,0))
    else:
        offset.append((-1, 0))
        offset.append((1, 0))
    if y == 4 or y == 0:
        if y == 4:
            offset.append((0, -1))
        if y == 0:
            offset.append((0, 1))
    else: 
        offset.append((0, 1))
        offset.append((0, -1))
    return offset










##### lausn 3, virkar best en getur ennþá farið út af gridinu, farið hringinn.
# # finn zero position
# for line in range(len(a)):
#     for num in range(len(a)):
#         if a[line][num] == 0:
#             zero_position = (num,line) 

# #zero_position = (3,2)
# x = zero_position[0]
# y = zero_position[1]
# # x=1
# # y=2


# choice = 6


# offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# for dx, dy in offset:
#     try:
#         if choice == a[y+dy][x+dx]:
#             a[y+dy][x+dx] = 0
#             a[y][x] = choice
#         else:
#             pass
#     except:
#         pass

# print(a)

#if a[3][2]






########### þetta virkaði ekki!!
# for i in range(len(a)):
#     try: 
#         num = a[i].index(choice) 
#         a[i][num] = 0
#         REMOVE_CHOICE = DONE
#     except:
#         pass
#     if REMOVE_CHOICE != DONE and NEW_ZERO == DONE :
#         try: 
#             num = a[i].index(0) 
#             a[i][num] = choice
#             NEW_ZERO = DONE
#         except:
#                 pass




# virkar en ekki alveg nógu vel, má bara fara upp,niður,hægri, vinstri
# i = 0
# for line in a:
#     j = 0
#     for num in line:
#         if num == choice:
#             a[i][j] = 0
#         if num == 0:
#             a[i][j] = choice
#         j += 1
#     i += 1

# print(a)





