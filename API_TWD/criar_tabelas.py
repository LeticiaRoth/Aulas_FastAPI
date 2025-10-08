#Código simples para comunicação se a tabela foi criada

from core.configs import settings
from core.database import engine
from models import all_models

async def create_table() -> None:
    print("Criando as tabelas no banco da API TWD")

    async with engine.begin() as conn:
        #Criar um bloco de contexto assíncrono
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        #Excluir caso já exista
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    
    print("Tabelas criadas com sucesso!")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_table())