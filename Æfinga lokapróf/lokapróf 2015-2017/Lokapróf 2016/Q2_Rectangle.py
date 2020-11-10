class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return self.width *2 + self.height * 2
    def __str__(self):
        return 'Width: {}, Height: {}'.format(self.height, self.width)

    def __eq__(self, other):##
        if self.area() == other.area():
            return 'The two rectangles are equal'
        else:
            return 'The two rectangles are not equal'

def main():
    rec1 = Rectangle(10,20)
    print(rec1.area())
    print(rec1.circumference())

    rec2 = Rectangle(10,21)
    print(rec2.area())
    print(rec2.circumference())
    # print(rec2)
    print(rec1)
    print(rec2)
    print(rec1 == rec2)



main()
