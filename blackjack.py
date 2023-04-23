import random

games = {

}
    
def new_deck():
    deck = []
    for suit in "SDCH":
        for face in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            deck.append(face+'_'+suit)
    
    random.shuffle(deck)
    return deck 

def value(hand):
    total = 0
    for i in hand:
        card = i.split("_")[0]
        print(card)
        if card in "JQK":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: 
                total+= 11
        else:
            total += int(card)
    return total
    

def new_game():
    game = {
        "deck" : new_deck(),
        "playerTurn": "True",
        "playerHand": None,
        "dealerHand": None,
        "gameOver" : False,
        "result" : -1
    }

    game["playerHand"] = []
    game["dealerHand"] = []

    return game


def deal(game_id, hand):
    games[game_id][hand].append(games[game_id]["deck"].pop(0))

def start_game(game_id):
    if game_id in games.keys():
        for i in range(2):
            # games[game_id]["playerHand"].append(games[game_id]["deck"].pop(0))
            # games[game_id]["dealerHand"].append(games[game_id]["deck"].pop(0))
            deal(game_id, "playerHand")
            deal(game_id, "dealerHand")

def create_new_game():
    game_id = random.randint(0,10000)
    while game_id in games.keys():
        game_id = random.randint(0,10000)
    games[game_id] = new_game()
    return game_id

def update(game_id, action):
    if not games[game_id]["gameOver"]:
        #1 - Hit
        if action == 1:
            deal(game_id, "playerHand")
            if (value(games[game_id]["playerHand"]) > 21):
                games[game_id]["gameOver"] = True
                games[game_id]["result"] = 0
                

        #0 - Stand
        if action == 2:
            while value(games[game_id]["dealerHand"]) < 17:
                deal(game_id, "dealerHand")

            if (value(games[game_id]["dealerHand"]) > 21):
                games[game_id]["gameOver"] = True
                games[game_id]["result"] = 1

            elif value(games[game_id]["dealerHand"]) == value(games[game_id]["playerHand"]):
                games[game_id]["gameOver"] = True
                games[game_id]["result"] = 2
            elif value(games[game_id]["dealerHand"]) > value(games[game_id]["playerHand"]):
                games[game_id]["gameOver"] = True
                games[game_id]["result"] = 0

            elif value(games[game_id]["dealerHand"]) < value(games[game_id]["playerHand"]):
                games[game_id]["gameOver"] = True
                games[game_id]["result"] = 1

            return game_id
