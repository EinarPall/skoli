# lokapróf 2019
# dæmi 3 prufanir
   	


Thedict = {}
fo = open('distribution_nums.txt', 'r')
for line in fo:
    for word in line.split(' '):
        word = int(word.strip('.').strip())
        if(word in Thedict):
            Thedict[word] += 1
        else:
            Thedict[word] = 1   

sorted_dict = dict(sorted(Thedict.items())) # items er í bókinni
print(sorted_dict)
if isinstance(Thedict, dict):
    print(Thedict)
Thedict[1] += Thedict[6]
print(Thedict[1])
print(len(Thedict))