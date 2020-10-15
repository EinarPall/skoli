dæmi 1 name and number

more_data = 'y'
the_dict = {}

while more_data != 'n':
    name = input('Name: ')
    number = (input('Number: ')
    the_dict[name] = number
    more_data = input('More data (y/n)? ')
    items = []
for item in the_dict.items():
    items.append(item)
sorted_items = sorted(items) 
    # more_data = more_data.lower #.lower

print(sorted_items)





