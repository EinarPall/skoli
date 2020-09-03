print('Welcome to car rentals!')

skref1 = input('Would you like to continue (y/n)? ') #Athuga hvort notandi vill halda áfram.
while skref1 == "y": #Ef já
    cc = input('Customer code (b or d): ') #Hvora leiðina vill viðskiptavinur velja sér
    if cc == 'b' or cc == 'd': #B leið
        num_days = int(input('Number of days: ')) #Hér fyllir viðskiptavinur út umbeðnar upplýsingar
        odo_start = int(input('Odometer reading at the start: '))
        odo_end = int(input('Odometer reading at the end: '))
        miles_driven = int(odo_end - odo_start) #Fjöldi mílna ekið
        print('Miles driven:',miles_driven)
        if cc == 'b': # b leið
            am_due =  float(40*num_days + 0.25 * miles_driven) #Upphæð sem viðskiptavinur greiðir
            print('Amount due:',round(am_due,1)) #Skrifum ",1" fyrir námundun á einn aukastaf
        elif cc == 'd': #D leið
            am_due = float(0.25 * (miles_driven -(100*num_days))) #Hér er reiknað út verðið. Hér er reiknað verð á mílum sem fara fram yfir 100 mílur á dag.
            if am_due < 0: #Ef það er undir núlli. Viðskiptavinur keyrði undir 100 mílur að meðtali á dag yfir leigutíma.
                print('Amount due:',60*num_days) #Daggjald sinnum dagafjöldi
            else: 
                print('Amount due:',round(am_due+60*num_days,1)) #Viðskiptavinur keyrði yfir 100 mílur að meðaltali á dag yfir leigutíma + daggjaldi sinnum dagafjöldi.
    skref1 = input('Would you like to continue (y/n)? ') #Til að byrja aftur á while lykkju, ef y.