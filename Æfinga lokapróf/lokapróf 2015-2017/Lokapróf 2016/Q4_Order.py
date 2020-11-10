#manages an order in a shop
#each order can contain multiple order lines
#Each line specifies the man of a product,price,quantity bought and possible discount

class Order():
    def __init__(self, name, product, price, quantity,discount=0,total=0):
        self.name = name
        self.product = product
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.total = self.price*self.quantity-self.discount


    def OrderLine(self):

        #print line in an order
        #total = self.price*self.quantity-self.discount

        return '{}\t{}\t{}\t{}\t{}'.format(self.product, self.price, self.quantity, self.discount, self.total)

    def addLine(self):
        #addline creates instance of orderline and stores in a list


    def getTotal(self):
       Total_order =0
       Total_order+= self.total 
       return 'Total:\t\t\t\t{}'.format(Total_order)


    






def main():
    print('Product\tPrice\tDiscount\tTotal')
    print('========================================')
        
    Order.addLine('eggs', 60, 12, 2, 5)
    Order.addLine('bread', 200, 1, 10, 5)
    Order.addLine('milk', 120, 2, 5)



    print('========================================')

    order.getTotal

main()
