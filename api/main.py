from fastapi import FastAPI
from src.v1.endpoints import health, user  # Importamos o novo módulo 'user'

# Adicionamos metadados para a documentação automática da API
app = FastAPI(
    title="Developer Snapshot API",
    version="0.1.0",
    description="An intelligent API that analyzes a developer's GitHub profile to provide qualitative insights.",
)

# Incluímos os roteadores na nossa aplicação principal
app.include_router(health.router, prefix="/v1")
# Adicionamos o roteador do usuário
app.include_router(user.router, prefix="/v1")


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the Developer Snapshot API"}
