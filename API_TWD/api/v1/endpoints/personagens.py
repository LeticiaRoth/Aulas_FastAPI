#Criamos a estrutura da primeira versão dentro de uma pasta para os endpoints e dentro dela os itens que temos que criar

#Dentro dos endpoints, eu coloco os métodos que irei usar dentro da API

#Vou enviar PersonagensSchema(JSON) e também receber um PersonagensSchema
#A API envia JSON e espera receber um JSON

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
#Independente de chamar ou não, a função assíncrona roda
async def post_personagens(personagem: PersonagensSchema, db: AsyncSession = Depends(get_session)):
    #Cria um novo personagem com dados recebidos do PersonagensSchema, do corpo da requisição em JSON
    novo_personagem = PersonagensModel(
        nome=personagem.nome, 
        idade=personagem.idade, 
        grupo=personagem.grupo
    )
    
    db.add(novo_personagem)
    #Salva no banco
    await db.commit()
    await db.refresh(novo_personagem)
    return novo_personagem


#MÉTODO GET (todos os personagens) COM CONEXÃO COM O BANCO
#Retorna uma lista com todos os personagens
@router.get("/", response_model=List[PersonagensSchema])
async def get_personagens(db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel)
    result = await db.execute(query)
    #Retorna uma lista
    personagens: List[PersonagensModel] = result.scalars().all()
    return personagens

#MÉTODO GET (pegando pelo ID do personagem) COM CONEXÃO COM O BANCO
@router.get("/{personagem_id}", response_model=PersonagensSchema, status_code=status.HTTP_200_OK)
async def get_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem = result.scalar_one_or_none()

    #Verificação se existe aquele personagem
    if personagem:
        return personagem
    else:
        raise HTTPException(
            detail="Personagem de TWD não encontrado.",
            status_code=status.HTTP_404_NOT_FOUND
        )
        
#MÉTODO PUT - CONEXÃO COM O BANCO
#Definição da URL dentro do parênteses;
#Determino a forma que será retornado
@router.put("/{personagem_id}", response_model=PersonagensSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensSchema, db: AsyncSession = Depends(get_session)):
    #Requisição de busca do personagem dentro do banco
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    #Variável que armazenará o resultado se for encontrado
    personagem_up = result.scalar_one_or_none()

    #Se for encontrado é atualizado
    if personagem_up:
        #Atualiza os dados do personagem que foi encontrado no banco
        personagem_up.nome = personagem.nome
        personagem_up.idade = personagem.idade
        personagem_up.grupo = personagem.grupo

        #Salva a alteração feita
        await db.commit()
        #Atualiza a instância
        await db.refresh(personagem_up)
        return personagem_up
    
    #Se não for encontrado retorna o Exception
    else:
        raise HTTPException(
            detail="Personagem não foi encontrado dentro do banco.",
            status_code=status.HTTP_404_NOT_FOUND
        )
        
#MÉTODO DELETE - CONEXÃO COM O BANCO
@router.delete("/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
#Depends função para fazer injeção, que executa o get_session para conectar com o banco
async def delete_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    personagem_del = result.scalar_one_or_none()

    if personagem_del:
        await db.delete(personagem_del)
        await db.commit()
        #Requisição processada, entretanto não há conteúdo (resposta)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            detail="Personagem não encontrado.",
            status_code=status.HTTP_404_NOT_FOUND
        )