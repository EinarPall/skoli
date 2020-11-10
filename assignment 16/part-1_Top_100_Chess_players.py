# part 1 og 2 
# fastar
RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3

def open_file(filename):
    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError: 
        return None


def create_players(file_stream):
    the_dict = {}
    for line in file_stream:
        # might considder splitting on ;  and space?
        rank, name, country, rating, byear = line.split(';')
        lastname, firstname = name.split(',')
        firstname = firstname.strip()
        lastname = lastname.strip()
        country = country.strip()
        rating = rating.strip()
        byear = byear.strip()

        key = f"{firstname} {lastname}"
        value_tuple = (int(rank), country, int(rating), int(byear))

        the_dict[key] = value_tuple

    return the_dict

def create_countries_dict(dict_players):
    countries_dict = {}
    for chess_player, chess_player_value in dict_players.items():
        country = chess_player_value[COUNTRY]
        if country in countries_dict:
           name_list =  countries_dict[country]
           name_list.append(chess_player)
        else:
            countries_dict[country] = [chess_player]
    return countries_dict

def create_year_dict(dict_players):
    year_dict = {}
    for chess_player, chess_player_value in dict_players.items():
        year = chess_player_value[BYEAR]
        if year in year_dict:
           name_list =  year_dict[year]
           name_list.append(chess_player)
        else:
            year_dict[year] = [chess_player]
    return year_dict

def print_header(header):
    print(header)
    dashes = '-' * len(header)
    print(dashes)

def print_sorted_country(dict_countries,dict_players):
    sorted_dict = sorted(dict_countries.items())
    for country, players_list in sorted_dict:
        average_rating = get_averages_rating(players_list,dict_players) # avg fyrir hvert country
        print('{} ({}) ({:.1f}):'.format(country,len(players_list),average_rating))
        for player in players_list:
            rating = dict_players[player][RATING]
            print('{:>40}{:>10d}'.format(player,rating))

def print_sorted_year(year_dict,dict_players):
    sorted_dict = sorted(year_dict.items())
    for year, players_list in sorted_dict:
        average_rating = get_averages_rating(players_list,dict_players) # avg fyrir hvert country
        print('{} ({}) ({:.1f}):'.format(year,len(players_list),average_rating))
        for player in players_list:
            rating = dict_players[player][RATING]
            print('{:>40}{:>10d}'.format(player,rating))



def get_averages_rating(players_list, dict_players):
    ratings = [dict_players[player][RATING] for player in players_list]
    average_rating = sum(ratings)/len(ratings)
    return average_rating



# main program starts here
# read file
filename = input('Enter filename: ')
file_stream = open_file(filename)
if file_stream:
    # dict-players
    dict_players = create_players(file_stream)
    dict_countries = create_countries_dict(dict_players)
    print_header('Players by country:')
    print_sorted_country(dict_countries,dict_players)
    print()
    dict_year = create_year_dict(dict_players)
    print_header('Players by birth year:')
    print_sorted_year(dict_year,dict_players)
    file_stream.close()