import random
#u = random.randint(0, 9)
# for i in range(99):
#     u = random.randint(0, 9)
#     print(u)

offset = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
offset_shuffled = random.shuffle(offset)
print(offset[random.randint(0,len(offset))])
print(offset_shuffled)             #offset_shuffled:



