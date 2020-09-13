# # Password validation in Python 
# # using naive method 
  
# # Function to validate the password 
# def password_check(passwd): 
      
#     SpecialSym =['$', '@', '#', '%'] 
#     val = True
      
#     if len(passwd) < 6: 
#         print('length should be at least 6') 
#         val = False
          
#     if len(passwd) > 20: 
#         print('length should be not be greater than 8') 
#         val = False
          
#     if not any(char.isdigit() for char in passwd): 
#         print('Password should have at least one numeral') 
#         val = False
          
#     if not any(char.isupper() for char in passwd): 
#         print('Password should have at least one uppercase letter') 
#         val = False
          
#     if not any(char.islower() for char in passwd): 
#         print('Password should have at least one lowercase letter') 
#         val = False
          
#     # if not any(char in SpecialSym for char in passwd): 
#     #     print('Password should have at least one of the symbols $@#') 
#     #     val = False
#     if val: 
#         return val 
  
#   # Main method 
# #def main(): 
# passwd = '4mammahallo'
      
# if (password_check(passwd)): 
#     print("Password is valid") 
# else: 
#     print("Invalid Password !!") 
          


#           ##### annað test drasl


# password= input("Create a password : ")
# x = True #random variable x which is set to TRUE
# while x:  #while x is TRUE,then run the following which is in the loop
#     if (len(password)<6 or len(password)>12): #if password not between 6 and 12 exit loop
#         print("Password length between 6 and 12 please")     
#         #exit the WHILE LOOP
#     elif not re.search("[a-z]",password): #if password doesn't contain one lowercase letter
#         print("You need at least one lower case letter")
#     elif not re.search("[0-9]",password): #if pasword doesn't contain numbers
#         print("You need at least one number")
                  
#     elif not re.search("[A-Z]",password): #if password doesn't contain upper case letter
#         print("You need at least one upper case character")

#     elif not re.search("[$#@]",password): #if password doesn't contain character
#         print("You need at least one special character please")
                  
#     elif re.search("\s",password): #if contains blank space
#         print("You cannot have blank spaces in your password...")
                  
#     else:
#         print("Valid Password")
#         x=False #Valid password has been created, so set x to False and exit the loop
                  

# if x: #note this is outside the while loop (so the code jumps to it, if BREAK is typed inside the loop
#     print("Not a Valid Password")



u = ''
while u:
    print('emty string')


f = 1
while f:
    print("hello")
    break


    