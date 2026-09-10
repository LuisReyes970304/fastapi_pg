from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from api.config.db import create_db_and_tables
from api.routes.create_user import router as create_user
from api.routes.get_user import router as get_user
from api.routes.update_user import router as update_user
from api.routes.delete_user import router as delete_user
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield   


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5400",
    "https://localhost:5400",
    "http://127.0.0.1:5400",
    "https://127.0.0.1:5400",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(get_user)
# app.include_router(create_user)
# app.include_router(update_user)
# app.include_router(delete_user)



