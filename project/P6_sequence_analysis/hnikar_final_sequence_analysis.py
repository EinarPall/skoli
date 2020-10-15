#fall sem opnar textaskrá

def opna_skra(filename):
    try:
        hlutur_i_skra=open(filename, "r")
        return hlutur_i_skra
    except:
        return print('\nFile {} not found'.format(filename))


#fall sem breytir lista í floated lista

def floated_listi(skra_listi):
    skra_listi_floated=[]
    for num in skra_listi:
        try:
            skra_listi_floated.append(float(num))
            skra_listi_floated.append(round(num,4))
        except:
            pass
    return skra_listi_floated

#fall sem prentar út listann

def sequence(hlutur_i_skra):
    for num in hlutur_i_skra:
        print(num, end=' ')
    return

#fall sem prentar summu listans

def summa(hlutur_i_skra):
    try:
        summa1=0; summa_listi=[]
        for num in hlutur_i_skra:
            summa1+=num
            summa1=round(summa1,4)
            print(summa1, end=' ')
        return
    except:
        return print('')

#fall sem raðar tölunum í stærðarröð

def rada_runu(hlutur_i_skra):
    try:
        hlutur_i_skra.sort()
        for num in hlutur_i_skra:
            print(num, end=' ')
        return
    except:
        return print('')

#fall sem finnur miðgildið

def midgildi_i_lista(hlutur_i_skra):
    try:
        if len(hlutur_i_skra)%2==1:
            stak=len(hlutur_i_skra)//2
            midgildi=hlutur_i_skra[stak]
            midgildi_namundad=round(midgildi,4)
            return print(midgildi_namundad)
        elif len(hlutur_i_skra)%2==0:
            stak1=len(hlutur_i_skra)//2
            stak2=stak1-1
            midgildi1=hlutur_i_skra[stak1]
            midgildi2=hlutur_i_skra[stak2]
            midgildi=(midgildi1+midgildi2)/2
            midgildi_namundad=round(midgildi,4)
            return print(midgildi_namundad)
    except:
        return print('')

# Main program starts here

def main():
    filename_list = input("Enter filenames: ").split()
    for i in filename_list:
        try:
            hlutur_i_skra=opna_skra(i)
            listi_float=floated_listi(hlutur_i_skra)
            print('\nFile',i)
            print('\tSequence:')
            print('\t\t', end='')
            listi_sequence=sequence(listi_float)
            print('')
            print('\tCumulative sum:') 
            print('\t\t', end='')
            listi_summa=summa(listi_float)
            print('')
            print('\tSorted sequence:')
            print('\t\t', end='')
            listi_radad=rada_runu(listi_float)
            print('')
            print('\tMedian:')
            print('\t\t', end='')
            midgildi=midgildi_i_lista(listi_float)
        except:
            pass

main()