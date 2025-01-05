# Plataforma de Gerenciamento Escolar intuitivo com CRUD

Este projeto é um sistema de gerenciamento escolar desenvolvido em Python, com integração ao banco de dados MySQL e uma interface gráfica simples, utilizando a biblioteca PySimpleGUI. O sistema permite realizar operações de **CRUD** (Criar, Ler, Atualizar, Deletar) para gerenciar registros de alunos, professores, matérias e notas diretamente através da interface.

## Tecnologias Utilizadas

- **Front-end e Back-end:** Python (versão 3.7 ou superior)
- **Banco de Dados:** MySQL
- **Bibliotecas:** 
  - [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
  - [PySimpleGUI](https://pypi.org/project/PySimpleGUI/)

## Funcionalidades

- **Gerenciamento de alunos:** Inserção, atualização e exclusão de registros de alunos.
- **Gerenciamento de professores:** Cadastro e manutenção de dados de professores.
- **Gerenciamento de matérias:** Cadastro e atualização de matérias oferecidas pela instituição.
- **Gerenciamento de notas:** Registro, alteração e consulta de notas dos alunos.
- **Interface gráfica:** Interface simples para interação com o banco de dados sem necessidade de linha de comando.

## Como Rodar o Projeto

### **Pré-requisitos**

1. Instale o **Python** (versão 3.7 ou superior).
2. Instale o **MySQL** e crie um banco de dados para o sistema.

### **Instalação**

1. Instale as bibliotecas necessárias:

```bash
pip install mysql-connector-python
pip install PySimpleGUI
```

2. Clone o repositório: 

```
git clone https://github.com/An4PDM/Plataforma-de-gerenciamento-escolar-intuitivo-com-CRUD.git
```

3. Navegue até o diretório do projeto:

```
cd Sistema-de-cadastro-escolar-com-CRUD
```

4. Configure as credenciais de acesso ao MySQL. No arquivo sis_acad.py, edite a parte do código que contém as informações do banco de dados (host, user, password, database) para refletir as suas configurações.

5. Criação do Banco de Dados:
Crie um banco de dados no MySQL (caso não tenha um) com o nome sistema_academico. Você pode usar o seguinte script SQL para criar as tabelas necessárias:

```sql
CREATE DATABASE sistema_academico;

USE sistema_academico;

CREATE TABLE aluno (
    ra INT PRIMARY KEY,
    nome VARCHAR(100),
    sobrenome VARCHAR(100),
    sexo ENUM('f', 'm', 'o'),
    data_nascimento DATE
);

CREATE TABLE professor (
    id_p INT PRIMARY KEY,
    cpf VARCHAR(11),
    nome VARCHAR(100),
    sobrenome VARCHAR(100),
    sexo ENUM('f', 'm', 'o'),
    data_nascimento DATE
);

CREATE TABLE materia (
    id_m INT PRIMARY KEY,
    nome VARCHAR(100),
    carga_horaria INT
);

CREATE TABLE nota (
    id_n INT PRIMARY KEY,
    ra INT,
    id_m INT,
    nota DECIMAL(5,2),
    FOREIGN KEY (ra) REFERENCES aluno(ra),
    FOREIGN KEY (id_m) REFERENCES materia(id_m)
);
```

6. Após configurar o banco de dados e as credenciais, execute o script principal para interagir com o sistema:

```bash
python sis_acad.py
```

## Como Contribuir
1. Fork este repositório. 
2. Crie uma branch para suas modificações:

```
git checkout -b feature/nome-da-sua-feature
```

3. Faça suas modificações e adicione os arquivos alterados:

```
git add .
git commit -m "Descrição das suas modificações"
```

5. Envie para o repositório original:

```
git push origin feature/nome-da-sua-feature
```

7. Crie um Pull Request explicando suas alterações.

## Licença
Este projeto está licenciado sob a MIT License.
