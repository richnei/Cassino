from fastapi import FastAPI, HTTPException
from Base_Model import Bet, Win, Rollback

app = FastAPI()

player_balances = {}
transactions = {}

##########################-REQUISIÇÕES-##############################################

@app.get("/balance")
def get_balance(player: int):
    balance = player_balances.get(player, 1000)
    return {"player": player, "balance": balance}


@app.post("/bet")
def place_bet(bet: Bet):
    if bet.player not in player_balances:
        player_balances[bet.player] = 1000 

    player_balances[bet.player] -= bet.value

    txn_id = len(transactions) + 1
    transactions[txn_id] = {"player": bet.player, "value": -bet.value}
    
    return {"player": bet.player, "balance": player_balances[bet.player], "txn": txn_id}


@app.post("/win")
def win_game(win: Win):
    if win.player not in player_balances:
        raise HTTPException(status_code=400, detail="Player não existe")
    
    txn_id = len(transactions) + 1
    transactions[txn_id] = {"player": win.player, "value": win.value}

    player_balances[win.player] += win.value

    return {"player": win.player, "balance": player_balances[win.player], "txn": txn_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

