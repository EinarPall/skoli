

class StringSet:
    def __init__(self,words):
        words_list = words.split(' ')
        unique_words_list = []
        for word in words_list:
            if word not in unique_words_list:
                unique_words_list.append(word)
        
        self.__words = unique_words_list

    def __str__(self):
        return self.make_string(self.__words)

    def make_string(self,some_list):
        outcome = ''
        for word in some_list:
            outcome += word + ' ' 
        return outcome.strip() # taka seinasta bilið í burtu

    def size(self):
        return len(self.__words)

    def __add__(self, other):
        union_words_list = []
        for word in self.__words:
            if word not in union_words_list:
                union_words_list.append(word)
        for word in other.__words:
            if word not in union_words_list:
                union_words_list.append(word)
        print(union_words_list)
        return StringSet(self.make_string(union_words_list))

    def find(self, word):
        if word in self.__words:
            return True
        else:
            return False

    def at(self, num):
        return self.__words[num]




#### testcase 5
set1 = StringSet('word1 word2 word3 word2 word1 word4')
print(set1.find('word2'))   # == True
print(set1.find('word5'))   # == False


## main testcase 

def main():
    str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
    set1 = StringSet(str1)
    str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
    set2 = StringSet(str2)
    print("Set1:", set1)
    print("Set2:", set2)
    print("Set1 size:", set1.size())
    print("Set2 size:", set2.size())
    the_union = set1 + set2
    print("Union:", the_union)
    print("Union size:", the_union.size())

    query = StringSet('chocolate cream fish good rubbish')
    print("Query:", query)
    count = 0
    for i in range(query.size()): # size er 5 
        if the_union.find(query.at(i)):
            count += 1
    
    print("Query size:", query.size())
    print("Found in union:", count)

main()