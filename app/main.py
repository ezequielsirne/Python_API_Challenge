from fastapi import FastAPI
from app.infrastructure.database import init_db
from app.api.character_router import router as character_router

app = FastAPI()

init_db()  # Creamos las tablas al iniciar
app.include_router(character_router)

@app.get("/")
def root():
    return {
        "message": "Hacé clic en el enlace de abajo o copiá/pegá en tu navegador para ver la documentación de la API.",
        "docs_url": "http://localhost:8000/docs"
    }