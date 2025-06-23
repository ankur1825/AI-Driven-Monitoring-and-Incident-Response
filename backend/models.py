from pydantic import BaseModel

class AlertModel(BaseModel):
    details: str