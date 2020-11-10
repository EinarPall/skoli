# klasar fyrir assignment 17
# dæmi 3

class Stock:
    def __init__(self,stock_name, stock_shares):
        self.stock_name = stock_name
        self.stock_shares = stock_shares
        #self.stock_str = f'{self.stock_name}: {self.stock_shares}'

    def __str__(self):
        return f'{self.stock_name}: {self.stock_shares}'



class Portfolio:
    def __init__(self):

        #self.stock_str = stock_str
        self.portfolio_list = []

    def add(self,stock_str):
        self.portfolio_list.append(stock_str)

    def __str__(self):
        output_str = ''
        for index in self.portfolio_list:
            if index != None:
                output_str += str(index) + '\n'
            else: 
                pass
        return output_str.strip()
