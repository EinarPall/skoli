## assignment 17

# dæmi 1

class Score: # hjúpun á ákveðnum gögnum og virki
    num_instances = 0 # num_instances is a class variable

    def __init__(self, value = 0):  # upphafsstillir. self er tilvik af counter
        Score.num_instances += 1
        self.value = value  # self.valuer is an instance variable, tilvikabreyta

    def __str__(self): # skilar af sér streng
        return str(self.value)             #'counter value: {}'.format(self.value)

    def add(self, value = 1): # hækka score-ið  # method í klasa er í rauninni bara fall
        self.value += value 

    def decrease(self, value = 1):
        self.value -= value

# dæmi 2 

class Sentence:
    def __init__(self, text):
        self.text = text
        self.word_list = self.text.split()

    def get_first_word(self):
        return self.word_list[0]
    
    def get_all_words(self):
        return self.word_list

    def replace(self, word_num, new_word):
        try:
            self.word_list[word_num] = new_word
            return self.word_list
        except IndexError:
            pass

# testcase 2    
# sent = Sentence('Here we have a longer sentence')
# sent.replace(2, "find")
# sent.replace(10,"bla")
# assert str(sent.get_all_words()) == "['Here', 'we', 'find', 'a', 'longer', 'sentence']"
# Example use of class:
# sent = Sentence('This is a test')
# print(sent.get_first_word())
# print(sent.get_all_words())
# sent.replace(3, "must")
# print(sent.get_all_words())

## dæmi 3

class Stock:
    def __init__(self,stock_name, stock_shares):
        self.stock_name = stock_name
        self.stock_shares = stock_shares
        #self.stock_str = f'{self.stock_name}: {self.stock_shares}'

    def __str__(self):
        return f'{self.stock_name}: {self.stock_shares}'


 
class Portfolio:
    def __init__(self):

        #self.stock_str = stock_str
        self.portfolio_list = []

    def add(self,stock_str):
        self.portfolio_list.append(stock_str)

    def __str__(self): # þetta fall þarf alltaf að returna strengi
        output_str = '' # bý til streng út frá listanum til þess að returna honum
        for index in self.portfolio_list:
            if index != None:
                output_str += str(index) + '\n'
            else: 
                pass
        return output_str.strip() # strip til að taka þetta auka newline í byrjun


# from portfolio import *   # Stock # virkar ef select folder á ass 17

stock1 = Stock('IBM', 100)
print(stock1)
stock2 = Stock('GOOG', 200)
stock3 = Stock('AMZN', 500)

portfolio = Portfolio()  #Portfolio
# print(portfolio)
portfolio.add(stock1)
portfolio.add(stock2)
portfolio.add(stock3)
print()
print(portfolio)