# Game of three-nought-four

# cards
import random as rd
suits = ('Club', 'Heart', 'Spade', 'Diamond')
faces = ('Ace', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
deck = [(s, f) for s in suits for f in faces] # define card deck
deck = rd.shuffle(deck) # shuffle deck
    
#players
players = [person, opp1, partner, opp2]
# first deal    
def initial_deal():
    global person, opp1, partner, opp2
    person.append(deck[:4])
    opp1.append(deck[4:8])
    partner.append(deck[8:12])
    opp2.append(deck[12:16])
    return player1, player2, player3, player4

# second deal
def second_deal():
    global player1, player2, player3, player4
    player1.append(deck[16:20])
    player2.append(deck[20:24])
    player3.append(deck[24:28])
    player4.append(deck[28:])
    return player1, player2, player3, player4

# bidding loop
def bid(player):
    if player is person:
        bid_person = int(input('Enter bid (0 = pass, 5 = 50, 6 = 60, 7 = 70, 8 = 80, 9 = 90, 10 = 100, 11 = 110, 12 = 120, 13 = all caps :'))
    else:
        bid
        
# main game loop
initial_deal()

while bid < 13:
    
    
# bidding loop
while trump_points < win_bid and non_trump_points < (304 - win_bid + 100):
    for player in players:
        bid(player)
        
    
