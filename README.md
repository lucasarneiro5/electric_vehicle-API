# electric_vehicle-API

# 🚗 Autonomous Vehicle Telemetry API

API desenvolvida em Python para simular a geração e disponibilização de dados de telemetria de veículos elétricos/autônomos.

O projeto tem como objetivo demonstrar conceitos de desenvolvimento de APIs REST, bancos de dados NoSQL, containers Docker e computação em nuvem utilizando serviços da AWS.

---

# 📋 Visão Geral

Empresas que operam frotas de veículos elétricos e autônomos precisam monitorar continuamente informações como:

* Nível de bateria
* Velocidade do veículo
* Localização GPS
* Data e hora da coleta

Esta aplicação simula a geração desses dados e os disponibiliza através de uma API REST para consulta e análise.

---

# 🎯 Objetivos do Projeto

* Simular dados de telemetria de veículos autônomos.
* Armazenar informações em banco NoSQL (MongoDB).
* Disponibilizar os dados através de uma API REST.
* Containerizar a aplicação utilizando Docker.
* Preparar a solução para implantação na AWS utilizando Amazon ECS.

---

# 🏗 Arquitetura da Solução

```text
┌─────────────────────┐
│      Cliente        │
│ Swagger / Browser   │
└──────────┬──────────┘
           │ HTTP
           ▼
┌─────────────────────┐
│      FastAPI        │
│  Container Docker   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      MongoDB        │
│  Container Docker   │
└─────────────────────┘
```

Arquitetura futura na AWS:

```text
Amazon ECS
│
├── Container FastAPI
│
└── Container MongoDB
```

---

# 🛠 Tecnologias Utilizadas

* Python 3.13
* FastAPI
* MongoDB
* PyMongo
* Docker
* Docker Compose
* AWS ECS (planejado)
* Amazon ECR (planejado)

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
├── .env
├── .dockerignore
├── main.py
│
└── README.md
```

---

# 🚀 Executando Localmente

## Clonar o projeto

```bash
git clone https://github.com/seu-usuario/autonomous-api.git

cd autonomous-api
```

---

## Configurar variáveis de ambiente

Criar arquivo `.env`

```env
MONGO_HOST=mongodb
MONGO_PORT=27017

MONGO_USER=admin
MONGO_PASSWORD=admin123

MONGO_DATABASE=telemetry_db
```

---

## Subir a aplicação

```bash
docker compose up --build -d
```

Verificar containers:

```bash
docker ps
```

---

# 📖 Documentação da API

Após iniciar a aplicação:

Swagger:

```text
http://localhost:8000/docs
```

OpenAPI:

```text
http://localhost:8000/openapi.json
```

---

# 🔌 Endpoints

## Health Check

```http
GET /health
```

Retorno:

```json
{
  "status": "healthy"
}
```

---

## Gerar Telemetria

```http
POST /telemetria
```

Retorno:

```json
{
  "mensagem": "Telemetria salva",
  "id": "687123abc456"
}
```

---

## Listar Telemetrias

```http
GET /telemetria
```

Retorno:

```json
[
  {
    "_id": "687123abc456",
    "bateria": 92,
    "velocidade": 64.5,
    "gps": {
      "latitude": -21.764,
      "longitude": -43.350
    },
    "data_hora": "2026-06-21T14:00:00"
  }
]
```

---

## Buscar Telemetria por ID

```http
GET /telemetria/{id}
```

---

# 🧪 Exemplo de Dados Gerados

```json
{
  "bateria": 87,
  "velocidade": 58.3,
  "gps": {
    "latitude": -21.764321,
    "longitude": -43.352187
  },
  "data_hora": "2026-06-21T14:30:00"
}
```

---

# 🐳 Containers Docker

A aplicação utiliza dois containers:

| Container         | Função        |
| ----------------- | ------------- |
| telemetry_api     | API FastAPI   |
| telemetry_mongodb | Banco MongoDB |

Verificar:

```bash
docker ps
```

Logs:

```bash
docker logs telemetry_api

docker logs telemetry_mongodb
```

---

# ☁️ Evolução para AWS

Próximas etapas previstas:

* Publicação da imagem no Amazon ECR.
* Implantação dos containers no Amazon ECS.
* Configuração de CI/CD.
* Health Checks avançados.
* Monitoramento com CloudWatch.
* Auto Scaling.

---

# 📚 Conceitos Demonstrados

* APIs REST
* Arquitetura em Microsserviços
* Banco NoSQL
* Docker
* Containerização
* Computação em Nuvem
* AWS ECS
* Amazon ECR
* Observabilidade
* Boas práticas de desenvolvimento

---

# 👨‍💻 Autor

Lucas Arneiro

Engenheiro Mecatrônico | Pós-graduado em Engenharia de Software | Desenvolvedor Python, Automação e Dados.
