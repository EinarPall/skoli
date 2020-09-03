print('Welcome to car rentals!')
while input('Would you like to continue (y/n)? ')=='y':
    cc=input('Customer code (b or d): ')
    days=int(input('Number of days: '))
    odo_start=int(input('Odometer reading at the start: '))
    odo_end=int(input('Odometer reading at the end: '))
    miles=odo_end-odo_start
    print('Miles driven:', miles)
    mpd=miles/days
    if cc=='b':
        price=days*40+0.25*miles
    elif cc=='d':
        if mpd<100:
            price=days*60
        elif mpd>100:
            price=days*60+(mpd-100)*days*0.25
    print('Amount due:', float(round(price,1)))
