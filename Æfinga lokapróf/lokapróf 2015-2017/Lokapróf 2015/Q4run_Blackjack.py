
class Card(object):
    def __init__(self, rank):
        self.rank = str(rank).lower() #hÃ¶ldum upprunalegu gildi sem notaÃ° er til aÃ° setja rank pÃ¶ssum aÃ° Ã¾aÃ° sÃ© lower case
        self.set_value(rank) # reiknum Ãºt gildi 

    def set_value(self,rank):
        if type(rank) == str:
            if rank in 'JjQqKk':
                self.value = 10 
            elif rank in 'aA': #Ã¡s = 11
                self.value = 11
        elif type(rank) == int:
            if 1 <= rank <= 9:
                self.value = rank
        
    def get_value(self):
        return self.value # skilum gildi

    def is_ace(self):
        return self.rank == 'a'


def main():
    Done = False
    while not Done:
        print('Scoring a blackjack hand')
        print('------------------------')
        nr_of_cards = int(input('Number of cards(min2, max 5): '))
        list_of_cards = []
        total = 0
        ace_count = 0
        
        for i in range(1, nr_of_cards+1):
            card = input('Card no {}: '.format(i))
            # list_of_cards.append(card)
            # hÃ©rna var bara veriÃ° aÃ° byÃ°ja um gildi og bÃ¦ta Ã¾vÃ­ gildi Ã­ lista,
            # Ã­ staÃ°inn fyrir aÃ° nota Ã¾aÃ° gildi til aÃ° bÃºa til instance af Card
            # hÃ©r hefÃ°i veriÃ° betra aÃ° kalla breytuna card eitthvaÃ° annaÃ°, t.d. card_rank
            # Ã¾vÃ­ Ã¾aÃ° er frekar funky aÃ° segja Card(card), hefÃ°i veriÃ° lÃ¦silegra aÃ° vera meÃ° 
            # Card(card_rank) - en no biggie.
            list_of_cards.append(Card(card))
        # print(list_of_cards)
        for card in list_of_cards:
            total += card.get_value()##
            if card.is_ace(): #chekcum Ã¡ hvort um Ã¡s er aÃ° rÃ¦Ã°a
                ace_count += 1
            
        print('The score of the hand is: {}'.format(total))
        
        again = input('Score again? ')
        if again == 'y':
            Done = False
        else:
            Done = True
main()