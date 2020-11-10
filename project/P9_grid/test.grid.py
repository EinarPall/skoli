# Project 9 - Grid
# gera klasa sem getur hreyft punkt í hnitakerfi


# prentar rétt út í upphafi en erfitt að gera hreyfingarnar
class Grid:
    def __init__(self,x_cord,y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.grid = []

    def __str__(self):
        output_str = ''
        for line in self.grid:
            if i == 0:
                output_str += 'x' + 'o' * (self.y_cord-1) + '\n'
            else:
                output_str += 'o' * self.y_cord + '\n'
        return output_str#.strip()


                    # ['oooo', 'oooo'] eða [['o', 'o', 'o']['o', 'o', 'o']] # pottþétt þetta seinna


# self.grid.replace # virkar bara á strengi og ekki hægt að velja stak í strengnum

# a_grid = Grid(3,4)
# print(a_grid)


# u = 'a' + '\n'
# u += 'b' + '\n'
# u.strip()
# print(u.strip())

#u=[]

# l = ' adsfgasdf o sde'
# u = l[11].replace('o','x')
# print(l)
# print(u)

# ná í stak í túplu

#t = [1,1]
#print(t[1])
# útfærslan ín move föllunum
grid = [['x', 'o', 'o'], ['o', 'o', 'o']]
x_cord = 2
y_cord = 3
y_pos = 0
x_pos = 0
grid[x_pos][y_pos] = "o"
y_pos += 1
grid[x_pos][y_pos] = "x"

#t[1] += 1
print(grid)

# u= [1,1]
# print(u[0]-1)

#def make_grid(self): # fall sem gerir grid út frá current position
 #   pass


# from grid import Grid

# # example 1
# a_grid = Grid(3,4)
# print(a_grid)
# print(a_grid.current_pos())