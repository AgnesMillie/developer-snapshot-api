# Alteramos a versão do Node.js de 18 para 20
FROM node:20-alpine

# Definimos o diretório de trabalho dentro do container.
WORKDIR /app

# Copiamos os arquivos de gerenciamento de dependências primeiro.
COPY package*.json ./

# Instalamos as dependências do projeto.
RUN npm install

# Copiamos todo o resto do código da nossa aplicação para o container.
COPY . .

# O Vite, por padrão, roda na porta 5173. Nós a expomos.
EXPOSE 5173

# O comando para iniciar o servidor de desenvolvimento do Vite.
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]