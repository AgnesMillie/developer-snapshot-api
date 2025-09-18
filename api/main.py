from fastapi import FastAPI
# 1. Importamos o CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from src.v1.endpoints import health, user

# Adicionamos metadados para a documentação automática da API
app = FastAPI(
    title="Developer Snapshot API",
    version="0.1.0",
    description="An intelligent API that analyzes a developer's GitHub profile to provide qualitative insights.",
)

# 2. Definimos as "origens" (endereços) que podem acessar nossa API.
#    No nosso caso, é o endereço do nosso servidor de desenvolvimento Vite.
origins = [
    "http://localhost:5173",
]

# 3. Adicionamos a configuração de CORS à nossa aplicação.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)

# Incluímos os roteadores na nossa aplicação principal
app.include_router(health.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the Developer Snapshot API"}