from CS_Deck import CS_Deck
class CS_Casino(object):
        def __init__(total):
                total.cShuffle()
        def cShuffle(total):
                total.Casino = []
                deckValue = int(input("How Many Decks Do You Have?"))
                for i in range(deckValue):
                        total.Casino.append(CS_Deck())
                        
        def massMix(total):
                x = len(total.cards)
                for i in range(x-1,0,-1): 
                        j = random.randint(0,i+1) 
                        total.cards[i],total.cards[j] = total.cards[j],total.cards[i]


        def print(total):
                for i in range(len(total.Casino)):
                        print(total.Casino[i])
                        
                
                
                               
                
