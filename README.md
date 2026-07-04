# 🚗 Electric Vehicle Telemetry API

API REST desenvolvida em Python para simular a geração, armazenamento e disponibilização de dados de telemetria de veículos elétricos.

O projeto demonstra conceitos de desenvolvimento de APIs REST, bancos de dados NoSQL, conteinerização com Docker e implantação em ambiente cloud utilizando serviços da Amazon Web Services (AWS).

---

# 📋 Visão Geral

Empresas que operam frotas de veículos elétricos precisam monitorar continuamente informações provenientes dos sensores embarcados para acompanhar o desempenho dos veículos e auxiliar na tomada de decisão.

Esta aplicação simula a geração desses dados de telemetria, armazena as informações em um banco MongoDB e disponibiliza consultas através de uma API REST.

Os dados simulados incluem:

- 🔋 Nível de bateria
- 🚗 Velocidade
- 🌡️ Temperatura
- 📍 Localização GPS
- 🕒 Data e hora da coleta

---

# 🎯 Objetivos

- Simular dados de telemetria de veículos elétricos.
- Armazenar informações em banco NoSQL (MongoDB).
- Disponibilizar os dados através de uma API REST utilizando FastAPI.
- Containerizar toda a aplicação utilizando Docker.
- Implantar a solução utilizando Amazon ECS Fargate.
- Publicar a API através de um Application Load Balancer (ALB).

---

# 🏗 Arquitetura

### Ambiente Local

```text
Cliente
    │
    ▼
FastAPI (Docker)
    │
    ▼
MongoDB (Docker)
```

### Ambiente AWS

```text
Cliente
    │
    ▼
Application Load Balancer
    │
    ▼
Amazon ECS (Fargate)
    │
    ├── Container FastAPI
    │
    └── Container MongoDB
```

---

# ☁️ Arquitetura AWS

A solução foi implantada utilizando os seguintes serviços:

- Amazon ECS Fargate
- Application Load Balancer
- Docker Hub
- Amazon VPC
- Security Groups
- Target Groups
- MongoDB
- Docker

---

# 🛠 Tecnologias Utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- MongoDB
- PyMongo
- Pydantic
- Docker
- Docker Compose
- Amazon ECS (Fargate)
- Application Load Balancer
- Docker Hub

---

# 📂 Estrutura do Projeto

```text
autonomous-api/
│
├── database/
│   └── connection.py
│
├── models/
│   └── telemetry_model.py
│
├── routers/
│   └── telemetry_router.py
│
├── services/
│   ├── telemetry_service.py
│   └── mongo_service.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env
├── main.py
└── README.md
```

---

# 🚀 Executando Localmente

## Clonar o projeto

```bash
git clone https://github.com/SEU-USUARIO/electric-vehicle-api.git

cd electric-vehicle-api
```

---

## Configurar variáveis de ambiente

Criar um arquivo `.env`

```env
MONGO_HOST=mongodb
MONGO_PORT=27017

MONGO_USER=admin
MONGO_PASSWORD=admin123

MONGO_DATABASE=telemetry_db
```

---

## Subir os containers

```bash
docker compose up --build -d
```

Verificar:

```bash
docker ps
```

---

# 📖 Documentação da API

Swagger

```
http://localhost:8000/docs
```

OpenAPI

```
http://localhost:8000/openapi.json
```

---

# 🔌 Endpoints

## Health Check

```http
GET /health
```

Retorno

```json
{
  "status": "healthy"
}
```

---

## Gerar nova telemetria

```http
POST /telemetry/generate
```

Retorno

```json
{
  "message": "Telemetry generated successfully",
  "id": "6876..."
}
```

---

## Listar telemetrias

```http
GET /telemetry
```

---

## Consultar última telemetria

```http
GET /telemetry/latest
```

---

## Buscar telemetria por ID

```http
GET /telemetry/{id}
```

---

# 📊 Exemplo de Telemetria

```json
{
    "battery": 91,
    "speed": 67.8,
    "temperature": 31.2,
    "gps": {
        "latitude": -23.5489,
        "longitude": -46.6388
    },
    "timestamp": "2026-06-27T19:25:40Z"
}
```

---

# 🐳 Containers

| Container | Descrição |
|------------|-----------|
| telemetry_api | API FastAPI |
| telemetry_mongodb | Banco MongoDB |

Verificar execução:

```bash
docker ps
```

Visualizar logs

```bash
docker logs telemetry_api

docker logs telemetry_mongodb
```

---

# ☁️ Implantação na AWS

A aplicação foi implantada utilizando:

- Amazon ECS Fargate
- Application Load Balancer
- Amazon VPC
- Security Groups
- Target Groups
- Docker Hub

Após a implantação, a API ficou disponível através do Load Balancer.

Exemplo:

```
http://<application-load-balancer>/docs
```

---

# 📚 Conceitos Demonstrados

- APIs REST
- FastAPI
- Docker
- Docker Compose
- MongoDB
- Banco NoSQL
- Arquitetura em Containers
- Amazon ECS Fargate
- Application Load Balancer
- VPC
- Security Groups
- Target Groups
- Deploy em Cloud
- Arquitetura Escalável

---

# 🚀 Melhorias Futuras

- Autenticação JWT
- HTTPS com AWS Certificate Manager
- Integração com Amazon ECR
- CI/CD utilizando GitHub Actions
- Monitoramento com Amazon CloudWatch
- Auto Scaling no Amazon ECS
- Integração com sensores IoT reais
- Migração para Amazon DocumentDB

---

# 👨‍💻 Autor

**Lucas Arneiro**

Engenheiro Mecatrônico • Pós-graduado em Engenharia de Software

Python | Cloud | Docker | AWS | APIs REST | Automação | Dados
