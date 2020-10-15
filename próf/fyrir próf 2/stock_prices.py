# byggir á verkefni nr. 1 í kafla 8 í kennslubókinni ("Data mining stock prices").  
# Við lausnina megið þið eingöngu notað efni sem fjallað er um í köflum 0-8 í kennslubókinni.

def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except: 
        return print('\nFile {} not found'.format(filename))

# fall sem breytir csv skjali í lista
def get_data_list(file_object):
    data_list = [] # list list sting er uppbyggingin
    for line_str in file_object:
        data_list.append(line_str.strip().split(','))
    return data_list


# fall sem reinkar average fyrir alla heildina
def get_monthly_averages(data_list,list_with_dates):  # adj close er númer 5 í röðinni og volume númer 6
    month_by_month_average_list = []
    
    average_price_on_line = 0
    average_price_divider = 0
    average_price = 0
    months = ['10','11','12','01','02','03','04','05','06','07','08','09']
    for i in range(len(months)):
        while list_with_dates[i][1] == months[i]: 
            for line in data_list[1:]: # sleppa línu 0 það sem yfirheitin eru
                average_price_on_line += float(line[5])*float(line[6])
                average_price_divider += float(line[6])
                average_price_month = average_price_on_line/average_price_divider
                month_by_month_average_list.append(average_price_month)
    return month_by_month_average_list




# fall sem fer í gegn mánuð fyrir mánuð í data listanum skjalinu
def dates_list(data_list):
    date_list = []
    for list_in_data in data_list[1:]:
        date = list_in_data[0].split('-')
        if date[1] == '10': 
            date_list.append(date)
    return  date_list  
# [  [ [10dags1 , tala] [10dags2, tala] ]   [ [11dags1,tala] [11dags2,tala] ]   ]
# 
def month_by_month_average(data_list):
    pass




month_by_month_average_list = []


def main():
    filename = input('Enter file name: ')
    file_object = open_file(filename)
    data_list = get_data_list(file_object)
    #print(data_list) # virkar hingað
    # adj close er númer 5 í röðinni og volume númer 6
    list_with_dates = dates_list(data_list)
    test = get_monthly_averages(data_list,list_with_dates)
    print(test)
main()