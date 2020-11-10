
class Card(object):
    def __init__(self, rank):
        self.rank = str(rank).lower()
        self.set_value(rank)

    def set_value(self,rank):
        if type(rank) == str:
            if rank in 'JjQqKk':
                self.value = 10  # Jack
            elif rank in 'Aa':
                self.value = 11
        elif type(rank) == int:
            if 1 <= rank <= 9:
                self.value = rank
    def get_value(self):
        return self.value

    def is_ace(self):
        return self.rank == 'a'

    def check_total(self, total, ace_count):
        while total> 21:
            if ace_count >0:
                for i in range(0,ace_count):
                    total -= 10
        if total >21:
            print('Busted')
        else:
            return total
            



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
            list_of_cards.append(Card(card))
        for card in list_of_cards:
            total += card.get_value()
            if card.is_ace():
                ace_count += 1
        check_hand = check_total(total, ace_count)
        
        print('The score of the hand is: {}'.format(total))
        
        again = input('Score again? ')
        if again == 'y':
            Done = False
        else:
            Done = True





main()