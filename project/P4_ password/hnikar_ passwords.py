password=input('Enter a new password: ')
tries=0
valid=0
invalid=0
while password!='q':
    if 6<=len(password)<=20:
        if sum(1 for c in password if c.islower())<1:
            print('At least one lower case letter needed')
            if sum(1 for c in password if c.isupper())<1:
                print('At least one upper case letter needed')
            if sum(1 for c in password if c.isdigit())<1:
                print('At least one number needed')
            invalid=invalid+1
        elif sum(1 for c in password if c.isupper())<1:
            print('At least one upper case letter needed')
            if sum(1 for c in password if c.isdigit())<1:
                print('At least one number needed')
            invalid=invalid+1
        elif sum(1 for c in password if c.isdigit())<1:
            print('At least one number needed')
            invalid=invalid+1
        else:
            valid=valid+1
            print('Valid password of length',len(password))
    else:
        print('Invalid length')
        invalid=invalid+1
    tries=tries+1
    password=input('Enter a new password: ')
print('You tried {} passwords, {} valid, {} invalid'.format(tries,valid,invalid))
