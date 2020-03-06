from CS_Card import CS_Card
import random
class CS_Deck(object):
    
    def __init__(total):
        total.cDeck()

    def __str__(total):
        return (str(CS_Card) for CS_Card in total.cards)
    
    def cDeck(total):
        total.cards = []
        for i in range(4):
            for j in range(0,13):
                total.cards.append(CS_Card(i, j))

   
                
