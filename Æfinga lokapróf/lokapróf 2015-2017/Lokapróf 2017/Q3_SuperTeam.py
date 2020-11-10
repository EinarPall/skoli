#name, age superpower
class Superhero(object):
    def __init__(self, name='', age=0, power='n'):
        self.name = name
        self.age = age
        self.power = power
    def setName(self,string):
        self.name = string
    
    def setAge(self, integer):
        self.age = integer
    
    def setPower(self, char):
        self.power = char
    
    def findpower(self):
        if self.power == 'f':
            self.power = 'Flying'
        elif self.power =='g':
            self.power = 'Giant'
        elif self.power == 'h':
            self.power = 'Hacker'
        elif self.power == 'n':
            self.power = 'None'
        else:
            self.power = 'Weakling'
        return self.power

    
    def __str__(self):
        return '{} ({}) : {}'.format(self.name, self.age, self.findpower())
        # Hvernig nota ég set.name í format



# def createSomeHeroes():
# fá hetju og skila inputi

def hero_amount():
    heroes = int(input('Input number of of heroes: '))
    return heroes
def CreateGroupOfHeroes(nr_of_heroes):
    
    for hero in range(0, nr_of_heroes):
        name = input('Input hero name: ')
        age = input('Input hero age: ')
        power = input('Input power: ')
        return name, age, power

def main():
    a_hero = Superhero('Dave', 12, 'g')
    print(a_hero)
    nr_of_heroes = hero_amount()#hvernig fæ ég nr. of heroes?
    for i in range(0, nr_of_heroes):
        name, age, power = CreateGroupOfHeroes(nr_of_heroes) #cannot unpack non-iterable
        hero = Superhero(name, age, power)
        print(hero)







main()