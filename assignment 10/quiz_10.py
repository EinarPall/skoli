a_list = [ ['a', 'b', 'c'], [1, 2, 3], [1.1, 2.2] ]
#a_list[2] = 1
#a_list[3:] = [6, 8, 6]
#a_list.append(a_list.pop())
u = a_list.count('a')



print(a_list[1])
print(a_list)
print(u)

# sp 6
a_list = [1, 2, 3, 4, 5]

for element in a_list:
    if element*2 in a_list:
        print(element, end=' ')


# sp 5
a_list = [3, 4, 5] + [6]
b_list = [3, 9]*2
result_list = []

for i, value in enumerate(a_list):
   value_to_append = value
   if b_list[i] > value:
       value_to_append = b_list[i]
   result_list.append(value_to_append)

print(result_list)


# sp 9

a_list = [4, 2, 4, 4, 2, 4]
u = a_list[1:3]

print(u)

# sp 10

a = [4, 7, 1]
b = a.sort()

print(b)


