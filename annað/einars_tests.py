# n = 1
# while n < 10:
#     print(n)
#     n += 1

def fund_me(age, monthly_salary):
    if int(age) < 24 and monthly_salary < 100000:
        return 20000
    else:
        return "Not applicable for fund"

older_gentleman = fund_me("25", 20000)
younger_gentleman = fund_me(22, 20000)
print(older_gentleman)
print(younger_gentleman)


#####  factorial function loop-a
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

##### styttri útgáfa til að inta stök í lista
listA = ['5', '2','-43', '23']
# Given list
print("Given list with strings : \n",listA)
# using int
res = [int(i) for i in listA]
# Result
print("The converted list with integers : \n",res)

#### skemtilegt dict fall
n=int(input("enter a number of elements in the dict: "))
my_dict = {}
for i in range (n):
    key=input("Enter key :")
    value=input("Enter values :")
    my_dict.update({key: value})
print(my_dict) 

