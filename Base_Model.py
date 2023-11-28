from pydantic import BaseModel

class Bet(BaseModel):
    player: int
    value: float

class Win(BaseModel):
    player: int
    value: float
