#Dentro do colocamos as configurações do banco

from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base


#Crio a classe que herda de BaseSettings
class Settings(BaseSettings):
    #Configurações gerais usadas na aplicação, caminho da API

    #Variavel de versionamento
    API_V1_STR : str = '/api/v1'

    #Depende do banco, nesse caso usamos o MYSQL, trocar a porta se necessário
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/personagenstwd'

    #Padronização para que todos os models herdem os recursos do SQLalchemy
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = False
        env_file = ".env"


#Aqui estamo setando a variável que herda a classe Settings que herda BaseSettings
settings = Settings()