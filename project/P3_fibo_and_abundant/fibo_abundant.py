# 1. forrit sem skrifar út fyrstu n1 >= 2 tölurnar í Fibonacci runu ( ein tala í hverri línu)
# 2. skrifa út allar "abundant" tölur á bilinu 1 uppí n2 (ein tala í hverri línu) 
# 0 1 1 2 3 5 8 13 21 34 - fyrstu 10 í fibonacci

choose = input('Input f|a|b (fibonacci, abundant or both): ') # Do not change this line

# Fibonacci runa
if choose == 'f' or choose == 'b':
    n = int(input('Input the length of the sequence: '))
    n1=0
    n2=1
    print('Fibonacci Sequence:')
    print('-------------------')
    print(n1)
    print(n2)
    for i in range(2,n): # Range byrjar í tveim til þess að uppfylla n1>=2
        n3=n1+n2 # Leggur saman 2 fibo tölur á undan til að fá næstu fibo tölu út 
        print(n3)
        n1=n2
        n2=n3

# Notum tvær ótengdar if skipanir til þess að "b" inputið virki. 

if choose == 'a' or choose == 'b':
# Abundant forlykkjan
    n2 = int(input('Input the max number to check: '))
    print('Abundant numbers:')
    print('-----------------')
    sum_proper_divisors = 0  
    for i in range(1, n2+1):  
        for j in range(1, int(i)):  # prófar alla eiginlega deila sem passa við hvert i þangað til i=j-1 
            if (i % j == 0):   
                sum_proper_divisors = sum_proper_divisors + j  # summar alla deilana saman 
        if (sum_proper_divisors > i):  
            print(i)  
        sum_proper_divisors = 0 

