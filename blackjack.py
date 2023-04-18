import random

games = {

}
    
def new_deck():
    deck = []
    for suit in "SDCH":
        for face in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            deck.append(face+'_'+suit)
    return deck

def new_game():
    return {
        "deck" : new_deck(),
        "playerTurn": "True",
        "playerHand": [],
        "dealerHand": []
    }

def create_new_game():
    game_id = random.randint(0,10000)
    while game_id in games.keys():
        game_id = random.randint(0,10000)
    games[game_id] = new_game()
    return game_id



def start_game(game_id):
    if game_id in games.keys():
        for i in range(2):
            games[game_id]["playerHand"].append(games[game_id]["deck"].pop(0))
            games[game_id]["dealerHand"].append(games[game_id]["deck"].pop(0))