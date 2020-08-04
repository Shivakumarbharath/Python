import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        total_deck = ''
        for card in self.deck:
            total_deck += '\n' + card.__str__()
        return "This deck has : " + total_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # card passed in will be from the deck.deal -->single card object that is Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips you want to bet"))
        except:
            print("Sorry Please provide an integer")

        else:
            if chips.bet > chips.total:
                print("You dont have enough chips :{}".format(chips.total))

            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    print("\n\nSelect\n\n1.Hit\n2.Stand")
    while True:
        opt = int(input())

        if opt == 1:
            hit(deck, hand)
        elif opt == 2:
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry I did not understand")
            continue
        break


def show_some(player, dealer):
    print("Player Cards : ")

    for card in player.cards:
        print(card)
    print(" The value is ", player.value, '\n\n')

    print("dealer cards : ")
    show = dealer.cards[0]
    print(show)
    print(" The Value is ", values[show.rank])


def show_all(player, dealer):
    print("Showing ALL")
    print("\n\nPlayer Cards : ")
    for card in player.cards:
        print(card)
    print(" The value is ", player.value, '\n\n')

    print("Dealer Cards : ")

    for card in dealer.cards:
        print(card)
    print(" The value is ", dealer.value)


def player_busts(player, dealer, chips):
    print("Bust Player")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player Wins Dealer Busted!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(" Dealer Wins")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player Tie \n PUSH!")


def MainPlay(chips):
    global playing

    while True:
        # Print an opening statement
        print("Welcome to The Black Jack\n ")

        # Create & shuffle the deck, deal two cards to each player
        main_deck = Deck()
        main_deck.shuffle()

        player = Hand()
        dealer = Hand()
        player.add_card(main_deck.deal())
        player.add_card(main_deck.deal())

        dealer.add_card(main_deck.deal())
        dealer.add_card(main_deck.deal())

        # Set up the Player's chips
        chips = Chips(chips)

        # Prompt the Player for their bet
        take_bet(chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(main_deck, player)

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(player, dealer, chips)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player.value <= 21:
                while dealer.value < 17:
                    hit(main_deck, dealer)

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios
        if player.value > 21:
            player_busts(player, dealer, chips)
        elif dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif player.value > dealer.value:
            player_wins(player, dealer, chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, chips)

        else:
            push(player, dealer)

        # Inform Player of their chips total

        print("Your chips Availibale is", chips.total)

        # Ask to play again
        k = input("Do you want to play again(Y/N)").capitalize()
        print('\n\n\n\n\n\n\n')
        if k == 'Y':
            playing = True
            MainPlay(chips.total)
        else:
            exit()


MainPlay(100)
