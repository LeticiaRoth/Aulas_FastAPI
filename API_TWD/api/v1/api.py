from fastapi import APIRouter
from api.v1.endpoints  import personagens

api_router = APIRouter()
api_router.include_router(personagens.router, prefix='/personagens', tags=['Personagens TWD'])