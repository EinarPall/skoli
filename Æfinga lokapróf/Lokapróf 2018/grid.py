# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def show_board(board,DIM):
    for i in range(DIM):
        for j in range(DIM):
            print('{}'.format(board[i][j], end=''))


#def find_move(move, board):
  #  if move == RIGHT:

    

def main():
    move = ''
    board = initialize_grid()
    print_board = show_board(board, DIM)
    while move != 'q':
        move = get_move()



main()


#fá lista
