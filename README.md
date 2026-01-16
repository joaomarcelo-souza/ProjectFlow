# ProjectFlow 📋

Sistema de gerenciamento de tarefas e projetos com API RESTful, arquitetura containerizada e deploy em nuvem.

O foco aqui é simples e sólido. Infra primeiro. Código preparado para crescer.

## 🚀 Tecnologias

- **Backend**: Python com FastAPI
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker e Docker Compose
- **Deploy**: Railway

## 🧱 Arquitetura

- API FastAPI executando em container Docker
- Banco PostgreSQL em container dedicado
- Comunicação via Docker Compose em ambiente local
- Deploy em nuvem com containers isolados

Tudo desacoplado. Tudo pronto para escalar.

## 📋 Funcionalidades (em andamento)

- Estrutura base para projetos e tarefas
- API preparada para operações CRUD
- Validações e regras de negócio planejadas

O sistema nasce simples. Evolui com intenção.

## 🐳 Containerização

O projeto possui:

- `Dockerfile` para build da API
- `docker-compose.yml` para orquestrar API e banco

Isso permite:

- Ambiente local previsível
- Subida rápida do projeto
- Paridade entre desenvolvimento e produção

## ☁️ Deploy

- Deploy realizado na **Railway**
- API e banco executando em containers
- Variáveis de ambiente configuradas na plataforma

Primeiro deploy no ar. Base fincada.

## 🗄 Estrutura do Banco de Dados

```sql
-- Projetos cadastrados
CREATE TABLE projetos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL
);

-- Tarefas dos projetos
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR NOT NULL,
    descricao TEXT,
    status VARCHAR DEFAULT 'pendente',
    projeto_id INT REFERENCES projetos(id)
);
```

## 🛣 Próximos Passos

- Implementação dos endpoints essenciais para projetos e tarefas
- Criação de um frontend simples para consumo da API
- Validação prática da API via interface web
- Migrations com Alembic para versionamento do banco
- Padronização dos status de tarefas
- Healthcheck da API para monitoramento
- Documentação automática com Swagger/OpenAPI
