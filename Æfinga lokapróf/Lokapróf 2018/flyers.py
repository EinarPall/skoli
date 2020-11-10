#prentar út nöfn allra ferðalanganna í stafrófsræð
#fyrir hvern ferðalang prentar út þau lönd sem hann hefur ferðast til í stafrófsröð
#Prentar út nafn þess ferðalangs sem hefur ferðast til flestra landa og hversu margra landa
# Prenta fyrsta af þeim sem hefur komið til jafnmargra landa

#gera dictionary til að telja orð
import operator
def get_flight_list(a_file):
    flight_list = []
    flight_dict = {}
    nr_of_flights = {}
    for line in a_file:
        line_list = line.strip().split()
        name = line_list[0]
        country = line_list[1]
        if name not in flight_dict:
            flight_dict[name] = country
            nr_of_flights[name] = 1
        else:
            flight_dict[name] += country
            nr_of_flights[name] += 1
    return flight_dict, nr_of_flights



#def get_nr_of_countries(flight_dict):
 #   for key,value in flight_dict:


def print_flights(flights_dict):
    for key,value in flights_dict.items():
        print('\t{]:'.format(key))

        
        


def main():
    a_file = open('flights.txt')
    flight_dict, flights = get_flight_list(a_file)
    print(flight_dict)
    print(flights)
    #print(flight_dict)
 
    sorted_flights = sorted(flights.items(), key=operator.itemgetter(1,0), reverse=True)
    top_flyer = [sorted_flights[i] for i in range(1)]
    print(top_flyer)

    #flights = get_flights(data)





main()
