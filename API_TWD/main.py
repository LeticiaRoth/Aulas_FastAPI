from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.configs import settings
from api.v1.api import api_router

origins = ["http://localhost", "http://localhost:8080", "http://localhost:5500", "http://127.0.0.1:5500"]

app = FastAPI(title="API DE PERSONAGENS DO TWD")

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
#Puxa o prefixo setado no meu API
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

    
