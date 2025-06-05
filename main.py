# main.py
from fastapi import FastAPI
from routes import router as api_router # Importa tu router

app = FastAPI(title="Agencia de Empleo API")

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de la Agencia de Empleo"}

