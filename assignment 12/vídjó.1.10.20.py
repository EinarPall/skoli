#v gildissvið (scope)
# stikun færibreytna (parameter passing)
# docstring 


# def func(a_list,a_var):
#     first = a_list[0] # first is a local variable
#     print(first)   # gildissvið breytunnar first er þessar tvær setningar
#     print(some_var) #virkar some_var is a global variable
#     print(a_var)    # a_var is a parameter value




# my_list = [1,2,3]
# some_var = 10 # er hér skilgreind á undan fallinu
# func(my_list,some_var)

# # first = 10 # virkar núna því gildissvið breytunnar er núna þessar tvær setningar
# # print(first) # virkar ekki  



#### dæmi 2

#  my_list  ->  [1,2,3]  <- a_list


# def func(a_list):
#     a_list = [4,5,6]   # nú a_list -> [4,5,6] ný tilvísun
#     a_list.append(4)
#     print(a_list)

# my_list = [1,2,3]
# func(my_list)
# print(my_list) # fjórir kemur hér líka



#### dæmi 3

def func(a_list,b_list = []): # þarf ekki endilega að gefa uppp gildi á b listanum inní functionið
    ''' This function accepts two lists an returns nothing '''
    print(a_list)
    print(b_list)

my_list = [1,2,3]
amother_list = [4,5,6]
func(my_list)
print(func.__doc__)
# importa math í python command promt, þá sést margt sem er hægt að nota




























