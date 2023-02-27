from pydantic import BaseModel


class MoteurCreate(BaseModel):
    moteur: str
    description: str 

class MoteurUpdate(BaseModel):
    description: str 

class MarqueCreate(BaseModel):
    marque: str
    description: str 

class MarqueUpdate(BaseModel):
    description: str 


class CategorieCreate(BaseModel):
    marque: str
    description: str 

class CategorieUpdate(BaseModel):
    description: str 