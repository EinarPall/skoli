# Project 10 
# class 1 of 3



# hugmynd, gera dictionary
# tékka hvort svarið þitt sé sama og value (strengur) fyrir spurnignuna

class Question:
    def __init__(self):
        self.question = ''          # dict()
        self.answer = ''          # dict()
        #self.guess = ''

    def __str__(self):
        return self.question

    def __repr__(self):
        return f'Q: {self.question} A: {self.answer}'

    def set_question(self, question):
        self.question = question
    
    def set_answer(self, answer):
        self.answer = answer
    
    def check_answer(self, guess):
        if guess.lower() == self.answer.lower():
            return True
        else:
            return False 