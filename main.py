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
    id_txn: int
    value: float