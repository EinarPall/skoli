# um klasa, Kaflar 11 og 12 í kennslubók
# vektor klasi
import math

class Vector():
    def __init__(self, a_list):
        self.__elements = a_list # __ þýðir að breytan er private, þýðir að breytan er ekki aðgengileg utan klasans 
                                 # ef punktur, þá puplic breyta
    
    def __str__(self):
        return str(self.__elements)

    def __len__(self): # to overload a function, erum að fjölbinda þetta fall; fjölbinding á len fallinu í klasanum
        return len(self.__elements) # gæti t.d. breytt því að len skili alltaf  5, er að breyta þvi sem innbygða len fallið á að gera

    def scaling(self, scalar):
        for i in range(0,len(self)): # hér er kallað á __len__ fallið.. þarf ekki að skrifa núllið
            self.__elements[i] = self.__elements[i] * scalar

    def length(self): # reikna lengd vektors í n víðu rúmi
        square_sum = 0
        for i in range(len(self)):
            square_sum += self.__elements[i]**2   # summan af öllum stökum sett í anaðveldi
        return math.sqrt(square_sum) # hér er notað úr import math

    def __add__(self, other): # er að overload-a (+)
        ''' return a new vector wich is the result of adding self and other '''
 

# main program starts here
vec1 = Vector([3,4])
# print(vec1.__elements) # ekki hægt __ gerði breytuna óaðgengilega (private), upplýsinga huld
# print(vec1.elements) # virkar ef puplic breyta
print(vec1)
vec1.scaling(3)
print(vec1)
print(len(vec1))
print(vec1.length())


vec2 = Vector([1,2,3])
print(vec2)
print(len(vec2))
print(vec2.length())

vec3 = vec1 + vec2
# vec3 = vec1.__add__(vec2)
print(vec3)
