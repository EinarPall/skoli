a_list = []
b_list = list() # listar eru collection og getra geymt hvaða tög sem er
c_list = [1,2,3]
d_list = ['a','b','c'] # listasr eru mutible object 
e_list = [1,2,'a','b']
a_str = 'forritun'
a_str[1] # strengir eru ekki breytan legir
c_list[1] = 9
print(c_list)
nested_list = [[1,2,3],[4,5,6]]
nested_list[1]
nested_list[0:1]
nested_list[1:]
'abc' + 'def'
'a'*3
[1,2,4] + [5,6,7] # = [1,2,4,5,6,7]
len(nested_list) # = 2
len(nested_list[1]) # = 3
nested_list[1][1] # = 5
min(c_list)
max(c_list)
sum(c_list) # bara hægt ef það eru tölur í listnaum

for elem in c_list:
    print(elem)

nested_list[0] = [7,8,9] # eða 
nested_list[0] = 'a'
print(nested_list)

aa_list = [1,2,3,4]
aa_list.append(5)
aa_list.insert(3,9)
last = aa_list.pop() # terkur endastak í burtu 
aa_list.remove(9)

print(aa_list)
print(last)


word_list = 'this is a sentence'.split()
first,second = 'first second'.split()

print(word_list)
print(first,second)

result = ':'.join(['a','b','c'])
print(result)

aa_list = [1,2,3,4]
aa_list.append(5)
print(aa_list[-1])
	




