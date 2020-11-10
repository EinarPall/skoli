

class ChoiceQuestion:
    def __init__(self,):
        self.a_question = ''
        #self.a_answers = dict()
        self.key_list = []

    def __str__(self):
        output = ''
        output += self.a_question + '\n'
        for i in range(len(self.key_list)):
            output += str(i+1) +'.' + ' '
            output += self.key_list[i] + '\n' 
        return output.strip() # strip til að losna við seinasta new-line

    def __repr__(self):
        return f'Q: {self.a_question} A: {self.right_anwer_num}'

    def set_question(self, question):
        self.a_question = question 

    def add_choice(self, choice, True_or_False):
        #self.a_answers[choice] = True_or_False
        self.key_list.append(choice)
        if True_or_False == True:  
            self.right_anwer_num = len(self.key_list)

    # útgáfa 2, vil fá númer á réttu svari
    def check_answer(self, choice_num):
        if int(choice_num) == self.right_anwer_num:
            return True
        else:
            return False


    # # útgáfa 1, vil fá lista með öllum svörum til að nota í str fallið
    # def check_answer(self, choice_num):
    #     #self.key_list = list(self.a_answers.keys())
    #     return self.a_answers.get(self.key_list[choice_num])

######## test case 5
# q = ChoiceQuestion()
# q_str = "Who is the president of Iceland?"
# q.set_question(q_str)
# ans1 = "Donald Trump"
# ans2 = "Joe Biden"
# ans3 = "Guðni Th. Jóhannesson"
# q.add_choice(ans1, False)
# q.add_choice(ans2, False)
# q.add_choice(ans3, True)
# print(str(q)) # == "{}\n1. {}\n2. {}\n3. {}".format(q_str, ans1, ans2, ans3)





########### main test
# def answer_question(a_question):
#     print(a_question)
#     response = input("Your answer: ")
#     print(a_question.check_answer(response))

# #Main
# q = ChoiceQuestion()
# q.set_question("In what year was the Python language first released?")
# q.add_choice("1991", True)
# q.add_choice("1995", False)
# q.add_choice("1998", False)
# q.add_choice("2000", False)
# q_str = 'hvað er verst?'
# ans1 = 'fokking'
# ans2 = 'test'
# ans3 = 'case'
# answer_question(q)
# print(str(q))
# u = "{}\n1. {}\n2. {}\n3. {}".format(q_str, ans1, ans2, ans3)
# print(u)

# forlykkja með dict (1: 1991,true)
# hugmynd

# u= {1 : (1991,True)} # dict

# #for i in u: # len(u) virkar ekki
#     #print(i,'.',end=' ')
#     #print(dict.get[i][1])

# #1. 1991
# a = {('1991',1) : True, ('1995',2) : False}

# #print(a.fromkeys('1991'))

# print(len(a))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.get("ford")

# print(x)
