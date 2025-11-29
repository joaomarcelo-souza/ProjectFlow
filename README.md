# ProjectFlow 📋

Sistema de gerenciamento de tarefas e projetos com API RESTful e arquitetura containerizada.

## 🚀 Tecnologias

- **Backend**: Python/FastAPI
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker & Docker Compose

## 📋 Funcionalidades

- Criação e organização de tarefas em projetos
- Status de acompanhamento de tarefas
- Consulta unificada de tarefas com detalhes do projeto
- Validações de negócio e tratamento de erros

## 🗄 Estrutura do Banco

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
