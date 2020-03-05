from CS_Deck import CS_Deck
class Casino(object):
        def __init__(total):
                total.cShuffle()
        def cShuffle(total):
                total.Casino = []
                deckValue = int(input("How Many Decks Do You Have?"))
                for i in range(deckValue):
                        total.Casino.append(CS_Deck())
        def massMix(total):
                for i in range(len(total.Casino)):
                        total.Casino[i].Single_Shuffle()       
        def print(total):
                for i in range(len(total.Casino)):
                        print(total.Casino[i])
                        
                
                
                               
                
