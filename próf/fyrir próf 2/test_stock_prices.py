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



'''
def get_monthly_averages (data_list):
    date_list = []
    monthly_average_list = []
    current_date = ''
    nums = []
    count = 0
    total = 0
    average = 0
    for index, row in enumerate(data_list[1:]):
        print(row)
        data_list[index] = row #.split(",")
    for index, row in enumerate(data_list[1:]):
        if index > 0:
            date_list.append(row[0])
            data_list[index] = [float(i) for i in row if row.index(i) > 0]
    for index, row in enumerate(data_list):
        if index == 1:
            current_date = str(date_list[index-1])
            current_date = current_date[:-3]
            count += 1
            nums = row[5:6]

        elif index > 1 and current_date in date_list[index - 1]:
            nums = row[5:6]




            monthly_average_list.append(average)

        elif index > 1 and current_date not in date_list[index - 1]:
            current_date = str(date_list[index-1])
            current_date = current_date[:-3]
            nums = row[5:6]
            total = 0




    print(monthly_average_list[0])
    print(current_date)
    print(date_list[0])
    print(data_list[1])    

    return monthly_average_list
'''

from collections import defaultdict

def get_col_avg_by_month(data, colnumber):
    result = defaultdict(lambda: [])
    for row in (row for row in data):
        date = year, month = row[0].split('-')[:2]
        result[tuple(date)].append(float(row[colnumber]))
    return {date: avg(data) for date, data in result.items()}



def main():
    filename = input('Enter file name: ')
    file_object = open_file(filename)
    data_list = get_data_list(file_object)
    test = get_col_avg_by_month(data_list,5)

main()


