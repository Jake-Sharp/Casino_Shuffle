class CS_Card(object):
    Suits = ["♠","♥","♦","♣"]
    Faces = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    
    def __init__(total, suit, face):
        total.faceList = face
        total.suitList = suit

    def __str__(total):
        face = CS_Card.Faces[total.faceList]
        suit = CS_Card.Suits[total.suitList]
        cardValue = face + suit

        return cardValue
