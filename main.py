from flask import Flask, render_template
from random import randint
from utils import format_balance

app = Flask(__name__)

PLAYER = {"username": "programadorpython", "balance": 1000}

GAMES = [
    {
        "id": 1,
        "name": "Iniciante",
        "buy_in": 50,
    },
    {
        "id": 2,
        "name": "Intermediário",
        "buy_in": 250,
    },
    {
        "id": 3,
        "name": "Avançado",
        "buy_in": 1000,
    },
    {
        "id": 4,
        "name": "Lendário",
        "buy_in": 10000,
    },
]


@app.route("/")
def index():
    return render_template("home.html", list_games=GAMES)


@app.route("/game/<int:game_id>")
def game(game_id):
    game = list(filter(lambda x: x["id"] == game_id, GAMES))[0]
    return render_template("game.html", game=game)


@app.route("/game/<int:game_id>/run")
def run_game(game_id):
    game = list(filter(lambda x: x["id"] == game_id, GAMES))[0]

    # validations

    if game["buy_in"] > PLAYER["balance"]:
        return {"error": "Você não tem dinheiro para apostar!"}

    # start coin
    result = {}
    selected = randint(0, 1)
    winner = True if selected == 0 else False
    if winner:
        PLAYER["balance"] += game["buy_in"] * 2
    else:
        PLAYER["balance"] -= game["buy_in"]

    return {
        "result_game": f"Você {'GANHOU' if winner else 'PERDEU'}.",
        "balance": format_balance(PLAYER["balance"]),
    }


@app.route("/player-info")
def get_player_info():
    return {
        "username": f"@{PLAYER['username']}",
        "balance": format_balance(PLAYER["balance"]),
    }


app.run(debug=True)
