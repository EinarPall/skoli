# # rt
# # lykilorð min 6 stafir og max 20 stafir, ef satt, þá fer það í næstu skilyrði
# # amk einn lágstafur, einn Hástafur og einn tölustaf

# pass_word = input('Enter a new password: ')
# pass_length = len(pass_word)
# #print(pass_length)
# valid = 0
# invalid = 0
# if 6 <= pass_length <= 20:
#     LOWER = sum(1 for c in pass_word if c.islower())
#     UPPER = sum(1 for c in pass_word if c.isupper())
#     NUMBER = sum(1 for c in pass_word if c.isdigit())
#     if UPPER < 1:
#         print('At least one upper case letter needed')
#     if LOWER < 1:
#         print('At least one lower case letter needed')
#     if NUMBER < 1:
#         print('At least one number needed')
#     if 
#         print('Valid password of length',pass_length)
#         valid += 1
# elif pass_word == 'q':
#     print('You tried {} passwords, {} valid, {} invalid'.format(valid+invalid,valid,invalid))  
# else: 
#     print('Invalid length')
#     invalid += 1

# pass_word = input('Enter a new password: ')

## pice of shit 
#         else:
#             print('Valid password of length',pass_length)
#             valid += 1
#     pass_word = input('Enter a new password: ')
#     else: 
#         print('Invalid length')
#     invalid += 1
#     pass_word = input('Enter a new password: ')  
# print('You tried {} passwords, {} valid, {} invalid'.format(valid+invalid,valid,invalid)) 

 
###### nýtt

pass_word = input('Enter a new password: ')
#pass_length = len(pass_word)
total_pw = 0
valid = 0
invalid = 0
#T_F = True
while pass_word != 'q':
    if 6 <= len(pass_word) <= 20:
        pw_valid = True
        if not any(char.isdigit() for char in pass_word):
            print('At least one number needed')
            pw_valid = False
        if not any(char.islower() for char in pass_word):
            print('At least one lower case letter needed')
            pw_valid = False
        if not any(char.isupper() for char in pass_word):
            print('At least one upper case letter needed')
            #invalid += 1
            pw_valid = False
        if pw_valid:
            print('Valid password of length',len(pass_word))
            valid += 1
        else:
            invalid += 1
    else:
        invalid += 1
        print('Invalid length')
    # total_pw += 1
    pass_word = input('Enter a new password: ')
    total_pw = valid + invalid
#print(f)
#print("You tried " + str(total_pw) + " passwords, " + str(valid) + " valid, " + str(invalid) +  " invalid")
#print(f'You tried {total_pw} passwords, {valid} valid, {invalid} invalid')
#invalid = total_pw - valid
print('You tried {} passwords, {} valid, {} invalid'.format(total_pw,valid,invalid))
















