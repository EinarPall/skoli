age = int(input("Input age: ")) # Do not change this line

price=float(40)

if age >= 65:
    price=0.6*price
elif age >=20:
    pass
elif age>5: 
    price = 0.8*price
else:
    price=0.0
print(price)

