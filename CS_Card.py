class Card(object):
    Suits = ["♠","♥","♦","♣"]
    Faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(total, suit, face):
        total.suitList = suit
        total.faceList = face

    def __str__(total):
        face = Card.Faces[total.faceList]
        suit = Card.Suits[total.suitList]
        cardValue = face + suit

        return cardValue
