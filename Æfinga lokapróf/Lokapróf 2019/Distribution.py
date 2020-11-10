# lokapróf 2019
# dæmi 3

class Distribution:
    __MAX_NUM =  6 # það er ekkert max í þessu 
    FILE_STREAM = 0
    def __init__(self, instance = 0):
        self.__distribution = dict()
        self.__average = 0 
        # Thedict = {}
        #fo = open('distribution_nums.txt', 'r')
        if instance != Distribution.FILE_STREAM and isinstance(instance, dict) == False:
            for line in instance:
                for num in line.split(' '):
                    num = int(num.strip('.').strip())
                    if(num in self.__distribution):
                        self.__distribution[num] += 1
                    else:
                        self.__distribution[num] = 1   
            sorted_dict = dict(sorted(self.__distribution.items())) # items er í bókinni
            # print(sorted_dict)
            self.__distribution = sorted_dict # eftir þetta er key orðið að streng
        if isinstance(instance, dict):
            self.__distribution = instance
        # if not isinstance(self.__distribution, dict):
        #     self.__distribution = dict()


    def __str__(self): # þetta prent fall virkar
        outcome = ''
        for key in self.__distribution.keys():
            outcome += f'{key}: {self.__distribution[key]}' + '\n' 
        return outcome #.strip() þarf ekki

    def __ge__(self,other):
        if self.average() >= other.average(): # kalla á average fallið en ekki self.__average því það er núll ef ekki er búið að kalla á það fall áður í main 
            return True
        else:
            return False 

    def __add__(self,other):
        if len(self.__distribution) > len(other.__distribution): # þetta er notað til þess að athuga hvort föllin sé jafn löng, annars kom error
            longer_dict = self.__distribution
            shorter_dict = other.__distribution
        else:
            longer_dict = other.__distribution
            shorter_dict = self.__distribution
        for key in longer_dict:
            try:
                longer_dict[key] += shorter_dict[key]
            except:
                pass
        new_dist = longer_dict        #set_distribution
        return Distribution(new_dist)

    def set_distribution(self, distribution): # fall sem tekur inn túplu sem segir hversu 1 uppí 6 kom oft fyrir. 
        self.__distribution = distribution

    def average(self): # reiknar meðaltalið úr dict;   virkar
        try:
            under_line = 0
            on_the_line = 0
            for key in self.__distribution:
                on_the_line += key * self.__distribution[key] # int ef key er str
                under_line += self.__distribution[key]
            self.__average = on_the_line/under_line
            return self.__average
        except ZeroDivisionError: # ef the dict er tóm
            return 0
    	


### main input case #####

# def open_file(filename):
#         ''' Returns a file stream if filename found, otherwise None '''
#         try:
#             file_stream = open(filename, "r")
#             return file_stream
#         except FileNotFoundError:
#             return None

# dist1 = Distribution()
# dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4}) # 1 appears 5 times, 2 appears 3 times, etc.
# print("Dist1: ")
# print(dist1)
# print(dist1.average())

# filename = 'distribution_nums.txt' #input("Enter filename: ")
# file_stream = open_file(filename)

# dist2 = Distribution(file_stream)
# print("\nDist2: ")
# print(dist2)
# print(dist2.average())

# if not dist2 >= dist1:
#     print("Dist2 >= Dist2")
# else:
#     print("Dist1 > Dist2")

# dist3 = dist1 + dist2
# print("\nDist3: ")
# print(dist3)
# print(dist3.average())
# print(str(dist3))

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

### textcase 6  
dist1 = Distribution()
dist1.set_distribution({1:4, 2:5, 3:3, 4:5, 5:7, 6:2})
dist2 = Distribution()
dist2.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4, 7:2})
print(dist2 >= dist1)
print(not dist1 >= dist2)



# # testcase 8
# dist1 = Distribution()
# dist1.set_distribution({1:4, 2:5, 3:3, 4:5, 5:7, 6:2})
# dist2 = Distribution()
# dist2.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4, 7:2})
# dist3 = dist1 + dist2
# print(str(dist3))            #== "1: 9\n2: 8\n3: 10\n4: 9\n5: 13\n6: 6\n7: 2\n"
# print('1: 9\n2: 8\n3: 10\n4: 9\n5: 13\n6: 6\n7: 2\n')


