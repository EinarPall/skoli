a = [1, 2, 3]
b = a
x = a == b
y = a is b


a_list = [1, 2, 3]
b_list = [5, 6, 7]

a_list.append(b_list)
b_list[0] = 4

print(a_list)


something = [ i for i in range(1,6) if i + 1 >=  3]
something = [ (i, j+1) for i in range(1,3) for j in range (1, 2)]
print(something)

an_int = 5
a_tuple = (an_int,)
a_list = [an_int]
an_int = 6
print(a_tuple, a_list)

# a_list = [3, 1, 6, 5]
# a_tuple = tuple(a_list)
# print(a_tuple.sort())


a_list = [1, 2]
b_list = [3, 4]
c_list = a_list
d_list = b_list[:]

a_list[0] = 9
b_list[0] = 8

print(a_list, b_list, c_list, d_list)
