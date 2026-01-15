from pydantic import BaseModel

class Threat(BaseModel):
    name: str
    location: str
    danger_rate: int