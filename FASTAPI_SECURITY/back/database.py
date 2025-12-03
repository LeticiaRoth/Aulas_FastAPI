from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL=  "sqlite:///./test.bd" #Permanecer na pasta de back

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Configurações do banco, como autocommit
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Usado para ser chamada em outros arquivos
Base = declarative_base()