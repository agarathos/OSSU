# http://www.codeskulptor.org/#user47_4K8QYG5NLD_3.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTRE = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
total_games = 0
wins = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):         
        return "Hand has value " + str(self.get_value()) + " and contains " + ' '.join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        has_ace = False
        value = 0
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        
        if has_ace and value + 10 <= 21:
            value += 10
                                           
        return value
                                           
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas,
                               [CARD_SIZE[0] * i + pos[0],
                               pos[1]])
         
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        return "Deck contains " + ' '.join([str(card) for card in self.cards])

#helper deal cards function
def deal_cards(obj, count):
    global deck
    for i in range(1, count + 1):
        obj.add_card(deck.deal_card())

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, total_games
    
    # if you were in play when requesting a deal, you lose
    if in_play:
        total_games += 1
    
    # your code goes here
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    in_play = True
    deal_cards(player, 2)
    deal_cards(dealer, 2)
    
    outcome = "Hit or stand?"

def hit():
    global player, in_play, outcome, total_games
    
    if in_play:
        deal_cards(player, 1)
        
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        in_play = False
        total_games += 1
        outcome = "You have busted, select Deal to play again"
       
def stand():
    global player, dealer, in_play, outcome, wins, total_games
    
    if player.get_value() > 21 or not in_play:
        outcome = "You have busted!"
        total_games += 1
        in_play = False
        return
    
    while dealer.get_value() < 17:
        deal_cards(dealer, 1)
        
    if dealer.get_value() >= 21:
        in_play = False
        outcome =  "Dealer busted, you win! Select Deal to play again"
        wins += 1
        total_games += 1
        return
        
    # Check who won
    outcome = "Dealer stands on " + str(dealer.get_value())
    if dealer.get_value() >= player.get_value():
        outcome =  "Dealer won!"
    else:
        outcome = "You win!"
        wins += 1
    total_games += 1
    in_play = False
    
    outcome += " Select Deal to play again"
    

# draw handler    
def draw(canvas):
    
    #Draw hands
    player.draw(canvas, [50, 400])
    dealer.draw(canvas, [50, 200])
    
    #draw over the first card
    if in_play:
        canvas.draw_image(card_back, 
                          CARD_BACK_CENTRE,
                          CARD_BACK_SIZE, 
                          [50 + CARD_BACK_CENTRE[0], 
                           200 + CARD_BACK_CENTRE[1]], 
                          CARD_BACK_SIZE)
        


    #TEXT
    canvas.draw_text("BlackJack", [50, 50], 30, "White")
    canvas.draw_text(outcome, [50, 75], 20, "Black")
    canvas.draw_text("Dealer", [50, 180], 15, "White")
    canvas.draw_text("Player", [50, 380], 15, "White")
    score = str(wins)
    score += (" Win " if wins == 1 else " Wins ") + " / "
    score += str(total_games - wins)
    score += " Loss " if total_games - wins == 1 else " Losses "
    canvas.draw_text("Score: " + score, [380, 50], 20, "White")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric