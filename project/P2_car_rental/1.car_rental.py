print('Welcome to car rentals!')
# skref1 = "y"

skref1 = input('Would you like to continue (y/n)? ')
while skref1 == "y":
    cc = input('Customer code (b or d): ')
    if cc == 'b':
        num_days = int(input('Number of days: '))
        odo_start = int(input('Odometer reading at the start: '))
        odo_end = int(input('Odometer reading at the end: '))
        miles_driven = int(odo_end - odo_start)
        print('Miles driven:',miles_driven)
        am_due =  float(40*num_days + 0.25 * miles_driven)
        print('Amount due:',round(am_due,1))
    elif cc == 'd':
        num_days = int(input('Number of days: '))
        odo_start = int(input('Odometer reading at the start: '))
        odo_end = int(input('Odometer reading at the end: '))
        miles_driven = int(odo_end - odo_start)
        print('Miles driven:',miles_driven)
        am_due = float(0.25 * (miles_driven -(100*num_days))) # 
        if am_due < 0:
            print('Amount due:',60*num_days)
        else:
            print('Amount due:',round(am_due+60*num_days,1))   
    skref1 = input('Would you like to continue (y/n)? ')











