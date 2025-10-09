#Converte para JSON para fazer a comunicação com o banco
from typing import Optional
#Como o SQLAlchemy tem o BaseModel dele, não podemos confundir então uso o as para determinar o SCBaseModel
from pydantic import BaseModel as SCBaseModel

#Garante que a requisição tenha os campos iguais aos definidos no Model
class PersonagensSchema(SCBaseModel):
    #Pode estar ausente ou ser None
    id : Optional[int] = None 
    nome : str
    idade : int
    grupo : str

    class Config:
        #Esse chemas vai ser no formato JSON que ferá a comunicação com o Banco
        from_attributes = True