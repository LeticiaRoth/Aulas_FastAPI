from core.configs import settings
#Passo o que vou usar dentro do meu banco
from sqlalchemy import Column,Integer,String

#DBBaseModel é uma clare declarativa do SQLAlchemy


#Crio a classe PersonagensModel que herda as settings que passei dentro de configs
class PersonagensModel(settings.DBBaseModel):
    #Determino o nome da tabela dentro do meu banco
    __tablename__ = "personagenstwd"

    #Determino os campos dentro da minha tabela
    id : int = Column(Integer(), primary_key=True, autoincrement=True)
     #Para determinar um campo que não pode ser nulo
    nome : str = Column(String(255), nullable=False)
    idade : int = Column(Integer())
    grupo : str = Column(String(255), nullable=False)