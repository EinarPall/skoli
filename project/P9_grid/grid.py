# Project 9 - Grid
# gera klasa sem getur hreyft punkt í hnitakerfi
# ATH.  listakerfið byrjar á 0 en gridið byrjar á 1  


 
class Grid:
    # Fastar
    Y_START = 1
    X_START = 1
    def __init__(self,x_cord = 1,y_cord = 1): # hnit jafnt og einn ef ekkert er sett inní Grid() klasan
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.grid = [] # bý til lista í uppafi með lengdina x_cord, vil hafa lista til þess að gera hreyfingarnar, 
                       # erfitt að gera þeir beint uppúr lögnum streng
        self.cur_pos = [Grid.X_START,Grid.Y_START] # eða [1,1] sem á að vera uphafs punktur 
        self.x_pos = self.cur_pos[0]-1  # -1 til að fara yfir á lista tungumálið
        self.y_pos = self.cur_pos[1]-1 # eða = 0 til að setja á fyrsta stak í listanum
        for i in range(x_cord): # x-listar jafn margir og x_cord 
            temp_list = []
            for u in range(y_cord): # y stök inní x-lista jafn mörg  og y_cord
                if i == self.x_pos and u == self.y_pos:
                    temp_list.append('x')
                else:
                    temp_list.append('o')
            self.grid.append(temp_list)       # lista uppbygging = [['x', 'o', 'o']['o', 'o', 'o']] 

    def __str__(self):
        output_str = '' # loka upbygging á streng = 'xooo\noooo\noooo'
        # self.grid.replace # virkar bara á strengi og ekki hægt að velja stak í strengnum
        for grid_list in self.grid:   
            for cord in grid_list: # setjum öll stök í listanum í einn langan streng
                output_str += cord
            output_str += '\n'
        return output_str #.strip() á ekki að vera strip, á að vera auð lína á eftir þessu

    def current_pos(self):
        return tuple([self.x_pos+1,self.y_pos+1]) # +1 til að breyta yfir í hnitakerfis punkta

    def move_left(self):
        self.grid[self.x_pos][self.y_pos] = 'o' # núlla út x-ið sem var fyrir
        self.y_pos -= 1 
        if self.y_pos < 0 : # ef x fer út af grid vintra megin þá lendir það lengst til hægri eins og grid stærðin leyfir
            self.y_pos = self.y_cord -1  # -1 því listar byrja á núlli
        self.grid[self.x_pos][self.y_pos] = 'x'

    def move_right(self):
        self.grid[self.x_pos][self.y_pos] = 'o'
        self.y_pos += 1
        if self.y_pos == self.y_cord: # ef þú ert búinn að færa þig út af grid-inu 
            self.y_pos = 0
        self.grid[self.x_pos][self.y_pos] = 'x' # nýja xið/punkturinn settur inná gridið

    def move_up(self):
        self.grid[self.x_pos][self.y_pos] = 'o' # taka út fyrra x-ið
        self.x_pos -= 1
        if self.x_pos < 0: # gæti verið == -1 í staðin 
            self.x_pos = self.x_cord -1
        self.grid[self.x_pos][self.y_pos] = 'x'

    def move_down(self):
        self.grid[self.x_pos][self.y_pos] = 'o' # taka út fyrra x-ið
        self.x_pos += 1
        if self.x_pos == self.x_cord:
            self.x_pos = 0
        self.grid[self.x_pos][self.y_pos] = 'x'




# example 1
# a_grid = Grid(3,4)
# print(a_grid)
# print(a_grid.current_pos())

# example 2
# b_grid = Grid(3,3)
# a_grid = Grid(4,4)
# a_grid.move_down()
# print(a_grid)
# a_grid.move_right()
# a_grid.move_right()
# a_grid.move_right()
# print(a_grid)
# b_grid.move_down()
# a_grid.move_up()
# a_grid.move_up()
# a_grid.move_up()

# print(a_grid)
# print(b_grid)
# print(a_grid.current_pos())

# example 3
# a_grid = Grid()
# print(a_grid)