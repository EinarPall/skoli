# Þrír eiginleikar hlutbundinnar forritunar (Object-Oriented Programming)
# Hjúpun (Encapsulation)
    # hjúpum ákveðin gögn og aðgerðir inní klasa 
    # upplýsinga huld
    # interface = þær aðgerðir sem klasinn býður manni uppá á nota

# Erfðir (Inheritance)
    # gera okkur kleift að erfa  gögn og aðgerðir frá einum klasa í einhverjum nýjum klasa sem við erum að búa til
    # code reuseability


# Fjölbinding (Polymorphism)
    # erum að beita operator overloading

# 3 + 4 , hér eru 3 og fjórir þolendur, verið að beita integer samlagningu, 
# (+) hagar sér öðruvísi eftri því hverjir þolendur hans eru.     



class Person(object): # erfir frá object, en það er sjálgefið  ### Parent class, Super class
    def __init__(self, first, last):
        self._first_name = first #  _first_name is protected
        self._last_name = last   # _last_name is protected, aðgengileg í erfðum
    	
    def __str__(self):          # erumn að fjölbinda hér
        return '{} {}'.format(self._first_name,self._last_name)

class Student(Person): # Child class, sub class
    def __init__(self, first, last, uni):
        # self.__first_name = first ### ekki duplicate-a kóða
        # self.__last_name = last
        # frekar svona:  
        Person.__init__(self, first, last) # self hér er tilvik á student, erfum first name og last name frá Person klasanum
        self.__university = uni

    def __str__(self): # væri betra að nota bara str fallið í Person
        return Person.__str__(self) + ' ' + self.__university # náum að endurnýta kóða út Person
        #  return '{} {}'.format(Person.__str__(self),self.__university) LÍKA HÆGT SVONA; líklega betra
        # hægt að breyta first og last í protected breytu en þá er hún með einu undirstriki
        # return '{} {} {}'.format(self._first_name,self._last_name, self.__university) # self.__first_name er privat breyta í Person

# person er ekki student en student er person

# Main program starts here

person1 = Person('Bobby', 'Jones')
print(person1)

student1 = Student('John', 'Smith', 'RU') # Student() virkar ekki því Person byður um 2 arguments, first and last

print(student1)


