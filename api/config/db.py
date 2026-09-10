from sqlmodel import SQLModel, create_engine
from api.models.user_model import User
import os

def get_database_url() -> str:
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", 5432)
    database = os.getenv("DB_NAME")
    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"    

URL = get_database_url()

engine = create_engine(URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":  
    create_db_and_tables()