# lokapróf 2019
# dæmi 3

class Distribution:
    __MAX_NUM =  6
    def __init__(self,file_stream):
        self.__distribution = dict()




    def __str__(self):
        outcome = ''
        for key in self.__distribution.keys():
            outcome += f'{key}: {self.__distribution[key]}' + '\n' 
        return outcome.strip()
    


    def set_distribution(self, distribution):
        self.__distribution = distribution


### main input case #####

def open_file(filename):
        ''' Returns a file stream if filename found, otherwise None '''
        try:
            file_stream = open(filename, "r")
            return file_stream
        except FileNotFoundError:
            return None

dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4}) # 1 appears 5 times, 2 appears 3 times, etc.
print("Dist1: ")
print(dist1)
print(dist1.average())

# filename = input("Enter filename: ")
# file_stream = open_file(filename)

# dist2 = Distribution(file_stream)
# print("\nDist2: ")
# print(dist2)
# print(dist2.average())

# if dist1 >= dist2:
#     print("Dist1 >= Dist2")
# else:
#     print("Dist2 > Dist1")

# dist3 = dist1 + dist2
# print("\nDist3: ")
# print(dist3)
# print(dist3.average())

# outcome from main test case input
# Dist1: 
# 1: 5
# 2: 3
# 3: 7
# 4: 4
# 5: 6
# 6: 4

# 3.5172413793103448
# Enter filename: data.txt

# Dist2: 
# 1: 6
# 2: 6
# 3: 8
# 4: 4
# 5: 4
# 6: 3

# 3.096774193548387
# Dist1 >= Dist2

# Dist3: 
# 1: 11
# 2: 9
# 3: 15
# 4: 8
# 5: 10
# 6: 7

# 3.3