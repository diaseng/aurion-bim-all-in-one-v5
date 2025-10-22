
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libffi-dev libssl-dev curl \    && pip install --upgrade pip \    && pip install --no-cache-dir -r requirements.txt \    && apt-get purge -y build-essential \    && apt-get autoremove -y \    && rm -rf /var/lib/apt/lists/*
COPY . .
ENV PORT=10000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","10000"]
