from fastapi import FastAPI
from app.infrastructure.database import init_db
from app.api.character_router import router as character_router

app = FastAPI()

init_db()  # Creamos las tablas al iniciar
app.include_router(character_router)

@app.get("/")
def root():
    return {"message": "API de personajes - en construcción"}