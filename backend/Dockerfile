FROM python:3.11-slim

WORKDIR /usr/src/app/backend

COPY /requirements.txt ./

# 必要なパッケージのインストールと依存関係のインストール
RUN apt-get update && apt-get install -y \
    python3-dev \
    pkg-config \
    gcc \
    build-essential \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
