from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

player_balances = {}
transactions = {}

class Bet(BaseModel):
    player: int
    value: float


class Win(BaseModel):
    player: int
    value: float


class Rollback(BaseModel):
    player: int
    txn: int
    value: float

##########################-REQUISIÇÕES-##############################################

@app.get("/balance")
def get_balance(player: int):
    balance = player_balances.get(player, 1000)
    return {"player": player, "balance": balance}