class Card:
    suitlist = ["Clubs", 'Diamonds', 'Hearts', 'Spades']
    rankList = ['none', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rankList[self.rank] + ' of ' + self.suitlist[self.suit])

    def __eq__(self, other):
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank:
            return 1
        if self.rank > other.rank:
            return -1
        return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # return type of __Str__ is always a string
    # it will always return single object and not list of objects
    def __str__(self):
        collection = ""
        count = 1
        for card in self.cards:
            collection = collection + " " * count + str(card) + '\n'
            count = count + 1
        return collection

    # list is manipulated so no need of return
    def shuffle(self):  # any return cannot be pprinted and list is changed
        from random import randint
        nCards = len(self.cards)  # number of times to shuffle
        for i in range(0, nCards):
            # j = random.randrange(i, nCards)
            rand = randint(0, len(self.cards) - 1)  # pick any card from all 52 cards
            self.cards[rand], self.cards[i] = self.cards[i], self.cards[rand]

    def removecard(self, card):
        self.cards.remove(card)

    def isEmpty(self):
        self.cards.clear()  # the cards  get cleard and returnss true
        length = len(self.cards)
        return length == 0


card2 = Deck()
# card2.shuffle()
# print(card2)
card1 = Card(0, 0)
print(card1)
card2.removecard(card1)
print(card2)
# mistake in indexex due to none
