#Program which reads information about N points and stores in a list
# each point has x, y values
#Range 0-100
#Prints a list of all the points within the upper left rectangle of the are
# Within 0,0 and 50,50
#All inputs are valid
#Use class to manage points and logic which determines if point is in upper left
# ... or not should be in a seperate function

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y


    def upper_left(self):
        upper_left_list = []
        if 0 <= self.x <=50 and 0 <= self.y <=50:
            upper_left_list.append((self.x, self.y))
        return upper_left_list

def main():
    # nr_of_points = input('Input nr. of points: ')
    # for i in range(1, nr_of_points+1):
    #     point = input('Card no {}:'.format(i))
    #     a_point = Point(point)

    point1 = Point(3,27)
    point2 = Point(21,51)
    point3 = Point(55,43)
    point4 = Point(68,99)
    point5 = Point(49,49)

    print('Points in the upper left quadrant are:')
    print(Point.upper_left(point1))#vantar að hafa ekki í tuple og ekki kommur + að lesa allt saman
    print(Point.upper_left(point2))#vantar að hafa ekki í tuple og ekki kommur + að lesa allt saman
    print(Point.upper_left(point3))#vantar að hafa ekki í tuple og ekki kommur + að lesa allt saman
    print(Point.upper_left(point4))#vantar að hafa ekki í tuple og ekki kommur + að lesa allt saman
    print(Point.upper_left(point5))#vantar að hafa ekki í tuple og ekki kommur + að lesa allt saman



    

main()
