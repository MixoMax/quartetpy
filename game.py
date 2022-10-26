import csv
import keyboard
import random

f = open("./data/data.csv", "r", newline="")
csv_reader = csv.reader(f)
rows = list(csv_reader)

#filtering the data for place holder
valid_types = ['Auto', 'Lok', 'Zug', 'Flugzeug', 'Jet', 'Boot', 'Schiff', 'Traktor', 'Bus', 'Landrakete']#needs to be extended depending on the added data.
cards = [r for r in rows if r[1] in valid_types]
random.shuffle(cards)

#giving each player random cards
player1_cards = cards[:len(cards)//2]
player2_cards = cards[len(cards)//2:]

stechen_cards = []

def play_round(player: int, card_player_none: list, card_player_two: list, last_category: str, stechen: bool, stechen_cards: list):
    print("Player " + str(player) + " please pick a category")

def startUp():
    who_starts = random.randint(1, 2)
    if(who_starts == 1):
        print("Player one starts!")
        play_round(1, player1_cards[0], player2_cards[0], "none", False, stechen_cards)
    else:
        print("Player two starts!")
        play_round(2, player1_cards[0], player2_cards[0], "none", False, stechen_cards)
    
startUp()
