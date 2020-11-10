# klasar og hlutbundin forritun

class Counter: # hjúpun á ákveðnum gögnum og virki
    num_instances = 0 # num_instances is a class variable

    def __init__(self, value = 0):  # upphafsstillir. self er tilvik af counter
        Counter.num_instances += 1
        self.value = value  # self.valuer is an instance variable, tilvikabreyta

    def __str__(self): # skilar af sér streng
        return str(self.value)             #'counter value: {}'.format(self.value)

    def increment(self, value = 1): # hækka teljarann  # method í klasa er í rauninni bara fall
        self.value += value 

    def decrement(self, value = 1):
        self.value -= value
#   interface for class is the set of methods that it defines
# tilvik er hluti af klasa 

# main program starts here
counter1 = Counter()   # calling the constructor (smiður)
print(Counter.num_instances)
print(counter1)
counter1.increment()   # counter1 is self in the call to increment 
counter1.increment(2)
counter1.decrement()
print(counter1)

counter2 = Counter()
print(Counter.num_instances)
for i in range(0,5):
    counter2.increment()
print(counter2)

# list() er innbyggður klasi

#
class GameBoard(object):
    max_score = 200

game1= GameBoard()
game2 = GameBoard

game1.max_score = 100

print(game1.max_score,game2.max_score)
