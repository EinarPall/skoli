# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n'
#coins = 0
Tiles_with_coins = [(1,2), (2,2), (2,3), (3,2)]


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def coins_for_player(col,row):
    '''Reitir þar sem spilari fær pening (1,2), (2,2), (2,3) og (3,2)'''
    if tuple([col,row]) in Tiles_with_coins:
        lever = random.choice([YES, NO])
        print("Pull a lever (y/n): ",lever)
        if lever == 'y':
            global coins
            coins += 1
            print("You received 1 coin, your total is now {}.".format(coins))
        else:
            pass


def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    direction = direction.lower()
    print('Direction:',direction)
    global moves
    if not direction in valid_directions:
        print("Not a valid direction!")
        moves += 1
    else:
        col, row = move(direction, col, row)
        coins_for_player(col,row) #####
        victory = is_victory(col, row)
        moves += 1
    return victory, col, row

# The main program starts here
import random
keep_on_going = 'y'
seed = input('Input seed: ')
random.seed(int(seed))
while keep_on_going == 'y':
    victory = False
    row = 1
    col = 1
    coins = 0
    moves = 0
    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row = play_one_move(col, row, valid_directions)
    print("Victory! Total coins {}. Moves {}.".format(coins,moves))
    keep_on_going = input('Play again (y/n):').lower()
