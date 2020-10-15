### Password ###

# Lykilorð amk 6 stafir og max 20 stafir, ef satt, þá fer það í næstu skilyrði.
# Amk. einn lágstafur, einn Hástafur og einn tölustaf.
# q stoppar og lætur notanda hafa yfirlit yfir fjölda tilraun, heppnaðra og misheppnaðra.
 
pass_word = input('Enter a new password: ')
total_pw = 0
valid = 0
invalid = 0

while pass_word != 'q':
    if 6 <= len(pass_word) <= 20: 
        pw_valid = True #Til að núllstilla hvort passwordið sé valid eða invalid. Byrjum á true ef ske kynni að fyrsta tilraun notanda sé fullkomin.
        if not any(char.islower() for char in pass_word): #Ef engir lágstafir.
            print('At least one lower case letter needed')
            pw_valid = False ##Til þess að telja þessa tilraun sem invalid.
        if not any(char.isupper() for char in pass_word): #Ef engir hástafir.
            print('At least one upper case letter needed')
            pw_valid = False
        if not any(char.isdigit() for char in pass_word): #Ef engir tölustafir.
            print('At least one number needed')
            pw_valid = False
        if pw_valid: #Ef true (tilraun stendst skilyrði).
            print('Valid password of length',len(pass_word))
            valid += 1
        else: #Teljari á lykilorð sem stendst ekki skilyrði (False).
            invalid += 1
    else: #Ef lengd lykilorðs stendst ekki skilyrði.
        invalid += 1
        print('Invalid length')
    pass_word = input('Enter a new password: ') #Til að byrjar lykkjuna upp á nýtt.
    total_pw = valid + invalid

print('You tried {} passwords, {} valid, {} invalid'.format(total_pw,valid,invalid)) #Ef pass_word = q.
