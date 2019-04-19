import Card15
import random
class Deck:
    def __init__(self):
        self.deckOfCards = []
    def getlist(self):
        return self.deckOfCards

    def setlist(self):
        for i in range(120):
            self.deckOfCards.append(Card15.Card(i))

    def shuffle(self):
        random.shuffle(self.deckOfCards)

# Draws 30 cards from the top of deck
    def draw(self):
       return self.deckOfCards.pop(1)


