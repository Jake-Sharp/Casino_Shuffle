from CS_Card import CS_Card
import random
class CS_Deck(object):
    
    def __init__(total):
        total.cDeck()

    def __str__(total):
        return '~' + .join(str(Card) for Card in total.cards) + '~'
    
    def cDeck(total):
        total.cards = []
        for i in range(4):
            for j in range(0,13):
                total.cards.append(Card(i, j))

    def Single_Shuffle(total):
        x = len(total.cards)
        for i in range(x-1,0,-1): 
            j = random.randint(0,i+1) 
            total.cards[i],total.cards[j] = total.cards[j],total.cards[i]
                
