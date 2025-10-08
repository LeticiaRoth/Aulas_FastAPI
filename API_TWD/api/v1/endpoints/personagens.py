#Criamos a estrutura da primeira versão dentro uma pasta para os endpoints e dentro dela os itens que temos que criar

#Dentro do endpoints, eu coloco os métodos que irei usar dentro da api

#Vou enviar PersonagensSchema(JSON) e também receber um PersonagensSchema
#API envia JSON e espera receber um JSON

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

#Configuração do sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

#Configuração da rota da models
from models.personagens_model import PersonagensModel
from schemas.personagens_schema import PersonagensSchema

from core.deps import get_session

router = APIRouter()

#MÉTODO POST
#O ID já é criado pelo banco

#decorator usado para lidar com requisições HTTP_POST no caminho /
#O response_model, a resposta deve seguir o modelo de dados do PersonagensSchema
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonagensSchema)
#Independente de chamar ou não, a função assincrona roda
async def post_personagens(personagem: PersonagensSchema, db: AsyncSession = Depends (get_session)):
    #Cria um novo personage com dados recebidos do PersonagenSchemas, body JSON
    novo_personagem = PersonagensModel(
        nome=personagem.nome, 
        idade=personagem.idade, 
        grupo=personagem.grupo
        )
    
    #Apenas chamo dentro dessa parte db de session
    async with db as session:
        session.add(novo_personagem)
        #Salva no banco
        await session.commit()
        await session.refresh(novo_personagem)
    return novo_personagem


#MÉTODO GET (todas os personagens) COM CONEXÃO COM O BANCO
#Retorna uma lista com todas personagens
@router.get("/",response_class=List[PersonagensSchema])
async def get_personagem(dd: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
        result = await session.execute(query)
        personagem = result.scalar_one_or_one()

        #Verificação se existe aquela banda
        if personagem:
            return personagem
        else:
            raise HTTPException(
                detail="Personagem de TWD não encontrado.",
                status_code=status.HTTP_404_NOT_FOUND
            )

#MÉTODO GET (pegando pelo ID do personagem) COM CONEXÃO COM O BANCO
