# Gerenciador de Produtos de Padaria

##  Descrição

Este projeto é um **gerenciador de produtos** desenvolvido para uma padaria utilizando **Python, Django e Django REST Framework (DRF)**.
O objetivo é permitir o controle dos produtos de forma simples e eficiente, implementando as operações básicas de um sistema de gestão.

---

## Funcionalidades

O sistema oferece um **CRUD completo** para os produtos:

* **Criar (Create):** adicionar novos produtos ao sistema.
* **Ler (Read):** listar todos os produtos e visualizar detalhes individuais.
* **Atualizar (Update):** editar as informações de um produto já cadastrado.
* **Excluir (Delete):** remover produtos que não estão mais disponíveis.

---

## Funcionalidades do Site/App

* Interface para gerenciamento de produtos.
* API REST para consumo em outras aplicações.
* Organização em **apps Django**, facilitando escalabilidade.

---

##  Tecnologias Utilizadas

* **Python**
* **Django**
* **Django REST Framework (DRF)**
* **SQLite3** (banco de dados padrão do Django)

---

## Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/cauedev30/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar um ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar as migrações

```bash
python manage.py migrate
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

O projeto estará disponível em: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**


autor: Cauê Franco


