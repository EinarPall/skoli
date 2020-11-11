# æfingapróf 2020
# dæmi 2



# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0


def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split(' ')
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for i in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def move_choice(choice,puzzle_board,zero_position,offset):
    ''' til að skipta auðareitnum út fyrir nágranna sem er valinn af notenda '''
    #offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x = zero_position[0]
    y = zero_position[1]

    for dx, dy in offset:
        try:
            if choice == puzzle_board[y+dy][x+dx]:
                puzzle_board[y+dy][x+dx] = 0
                puzzle_board[y][x] = choice
                zero_position = (x+dx,y+dy) 
            else:
                pass
        except:
            pass
    return puzzle_board, zero_position


def find_zero_position(puzzle_board):
    ''' til að finn hvar núllið byrjar, út frá input frá notenda '''
    zero_position = None
    for line in range(len(puzzle_board)):
        for num in range(len(puzzle_board)):
            if puzzle_board[line][num] == 0:
                zero_position = (num,line) 
    return zero_position

def choice_offset(zero_position):
    ''' til að finna viðeigandi offset eftir því hvað auði reiturinn er, má bara fær til nágranna á gridinu. '''
    x = zero_position[0]
    y = zero_position[1]
    offset = []
    if x == 4 or x == 0:
        if x == 4:
            offset.append((-1,0))
        if x == 0:
            offset.append((1,0))
    else:
        offset.append((-1, 0))
        offset.append((1, 0))
    if y == 4 or y == 0:
        if y == 4:
            offset.append((0, -1))
        if y == 0:
            offset.append((0, 1))
    else: 
        offset.append((0, 1))
        offset.append((0, -1))
    return offset


def main():
    choice = 4
    puzzle_board = initialize_board()
    #print(puzzle_board)
    display(puzzle_board)
    zero_position = find_zero_position(puzzle_board)
    while  choice != 0:
        offset = choice_offset(zero_position)
        choice = int(input())
        if choice != 0:
            new_puzzle_board, zero_position = move_choice(choice,puzzle_board,zero_position,offset)
            display(new_puzzle_board)

main()











