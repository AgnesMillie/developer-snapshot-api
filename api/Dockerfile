# Estágio Único: Usamos uma imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Define o PYTHONPATH para garantir que as importações de 'src' funcionem
ENV PYTHONPATH="/app"

# Copia e instala as dependências globalmente dentro do container
# (Sem venv, pois o container já é um ambiente isolado)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da nossa aplicação
COPY ./src ./src
COPY main.py .

# Expõe a porta que a aplicação vai usar
EXPOSE 8000

# Comando para iniciar o servidor. O uvicorn estará no PATH do sistema.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]