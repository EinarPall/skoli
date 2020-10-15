#fall sem opnar textaskrá

def opna_skra(filename):
    try:
        hlutur_i_skra=open(filename, "r")
        return hlutur_i_skra
    except:
        return print('\nFile {} not found'.format(filename))

#fall sem breytir textaskrá í lista

def lista_skra(hlutur_i_skra):
    listi=[]
    for line in hlutur_i_skra:
        hreinsud_lina=line.strip()
        listi.append(hreinsud_lina)
    return listi

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
    print('\tSequence:')
    print('\t\t', end='')
    for num in hlutur_i_skra:
        print(num, end=' ')
    return

#fall sem prentar summu listans

def summa(hlutur_i_skra):
    print('\tCumulative sum:'); print('\t\t', end='')
    try:
        summa1=0; summa_listi=[]
        for num in hlutur_i_skra:
            summa1+=num
            summa1=round(summa1,4)
            print(summa1, end='')
        return
    except:
        return print('')

#fall sem raðar tölunum í stærðarröð

def rada_runu(hlutur_i_skra):
    print('\Sorted sequence:')
    print('\t\t', end='')
    try:
        rada=sorted(hlutur_i_skra)
        for num in rada:
            print(num, end=' ')
        return
    except:
        return print('')

#fall sem finnur miðgildið

def midgildi_i_lista(hlutur_i_skra):
    print('\tMedian:')
    print('\t\t', end='')
    import statistics
    try:
        midgildi=statistics.median(hlutur_i_skra)
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
            skra_listi=lista_skra(hlutur_i_skra)
            listi_float=floated_listi(skra_listi)
            print('\nFile',i)
            listi_sequence=sequence(listi_float)
            print('')
            listi_summa=summa(listi_float)
            print('')
            listi_radad=rada_runu(listi_float)
            print('')
            midgildi=midgildi_i_lista(listi_float)
        except:
            print('hér er villan')

main()
