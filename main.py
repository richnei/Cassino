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

@app.post("/rollback")
def rollback_transaction(rollback: Rollback):
    player_id = rollback.player
    txn_id = rollback.txn
    rollback_value = rollback.value
    txn_id = len(transactions) + 1
    transactions[txn_id] = {"player": rollback.player, "value": rollback.value}
    print("transactions:", transactions)
    print("txn_id:", txn_id)


    if txn_id not in transactions:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    transaction_data = transactions[txn_id]
    if transaction_data["player"] != player_id:
        raise HTTPException(status_code=400, detail="ID do jogador não corresponde à transação")

    player_balances[player_id] += rollback_value
    del transactions[txn_id]

    return {"code": "OK", "balance": player_balances[player_id]}
