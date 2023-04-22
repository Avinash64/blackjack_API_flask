from markupsafe import escape
from flask import Flask, request
from blackjack import *

app = Flask(__name__)

a = create_new_game()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return f'Hello, World {start_game(a)} {games}'


@app.route('/create_game')
def create_game():
    game_id = create_new_game()
    start_game(game_id)
    return {"gameId" : game_id, "game": games[game_id]}



# @app.route('/create_game')
# def create_game():
#     game_id = create_new_game()
#     start_game(game_id)
#     return {"gameId" : game_id, "game": games[game_id]}

@app.route('/play',methods = ['POST'])
def play():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        update(json["game_id"], json["action"])
    return games[json["game_id"]]
