# abundant forlykkjan
n = int(input('Input the max number to check: '))

sum_proper_divisors = 0  
for i in range(1, n+1):  
    for j in range(1, int(i)):  
        if (i % j == 0):   
            sum_proper_divisors = sum_proper_divisors + j  
    if (sum_proper_divisors > i):  
        print( i)  
    sum_proper_divisors = 0 


