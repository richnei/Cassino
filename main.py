from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


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