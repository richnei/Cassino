from fastapi import FastAPI, HTTPException
from Base_Model import Bet, Win
from typing import Dict

app = FastAPI()

player_balances = {}
transactions = {}


class GameState:
    def __init__(self):
        self.player_balances: Dict[int, float] = {}
        self.transactions: Dict[int, Dict] = {}

    def get_balance(self, player: int):
        return self.player_balances.get(player, 1000)

    def place_bet(self, bet: Bet):
        if bet.player not in self.player_balances:
            self.player_balances[bet.player] = 1000 

        if self.player_balances[bet.player] < bet.value:
            raise HTTPException(status_code=400, detail="Sem fundos para fazer a aposta")

        self.player_balances[bet.player] -= bet.value

        txn_id = len(self.transactions) + 1
        self.transactions[txn_id] = {"player": bet.player, "value": -bet.value}
        
        return {"player": bet.player, "balance": self.player_balances[bet.player], "txn": txn_id}

    def win_game(self, win: Win):
        if win.player not in self.player_balances:
            raise HTTPException(status_code=400, detail="Player não existe")
        
        txn_id = len(self.transactions) + 1
        self.transactions[txn_id] = {"player": win.player, "value": win.value}

        self.player_balances[win.player] += win.value

        return {"player": win.player, "balance": self.player_balances[win.player], "txn": txn_id}

game_state = GameState()

##########################-REQUISIÇÕES-##############################################

@app.get("/balance")
def get_balance(player: int):
    return {"player": player, "balance": game_state.get_balance(player)}

@app.post("/bet")
def place_bet(bet: Bet):
    return game_state.place_bet(bet)

@app.post("/win")
def win_game(win: Win):
    return game_state.win_game(win)