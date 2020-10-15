# # rt
# # lykilorð min 6 stafir og max 20 stafir, ef satt, þá fer það í næstu skilyrði
# # amk einn lágstafur, einn Hástafur og einn tölustaf
 
pass_word = input('Enter a new password: ')
total_pw = 0
valid = 0
invalid = 0

while pass_word != 'q':
    if 6 <= len(pass_word) <= 20:
        pw_valid = True
        if not any(char.islower() for char in pass_word):
            print('At least one lower case letter needed')
            pw_valid = False
        if not any(char.isupper() for char in pass_word):
            print('At least one upper case letter needed')
            pw_valid = False
        if not any(char.isdigit() for char in pass_word):
            print('At least one number needed')
            pw_valid = False
        if pw_valid:
            print('Valid password of length',len(pass_word))
            valid += 1
        else:
            invalid += 1
    else:
        invalid += 1
        print('Invalid length')
    pass_word = input('Enter a new password: ')
    total_pw = valid + invalid

print('You tried {} passwords, {} valid, {} invalid'.format(total_pw,valid,invalid))
















