# =========================================================
# 🏗️  Aurion BIM ALL-IN-ONE v5.0 — Backend (FastAPI)
# 📦  Dockerfile otimizado para Render + Python 3.12
# =========================================================

# Etapa base: imagem leve do Python
FROM python:3.12-slim

# Diretório de trabalho no container
WORKDIR /app

# Variáveis de ambiente para melhor desempenho
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala dependências do sistema + Python libs
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libffi-dev libssl-dev curl && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copia todo o restante do código
COPY . .

# Define a porta de execução
ENV PORT=10000

# Comando padrão de inicialização do backend (FastAPI com Uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
