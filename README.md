#  ClinicaPlus — Sistema de Gestão de Clínica Médica

Projeto de estudo desenvolvido para praticar **Python** e **MySQL** em um cenário real de desenvolvimento de software.

> ⚠️ Este projeto tem finalidade exclusivamente educacional e não se destina ao uso em ambientes clínicos reais.

---

## 📋 Descrição do Projeto

O **ClinicaPlus** é um sistema de gerenciamento para clínicas médicas de pequeno porte que roda inteiramente no terminal. Ele simula o fluxo básico de uma clínica: cadastrar pacientes e médicos, agendar consultas e acompanhar o histórico de atendimentos.

O sistema foi construído com foco em boas práticas de organização de código Python e uso correto de banco de dados relacional, aplicando conceitos como separação de responsabilidades, queries parametrizadas e validação de regras de negócio.

- Cadastro de pacientes com validação de CPF único
- Cadastro de médicos com especialidade e CRM
- Agendamento de consultas com controle de conflitos de horário
- Cancelamento lógico de consultas (sem exclusão do banco)
- Relatórios com exportação em `.csv`

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Banco de Dados:** MySQL 8.0+
- **Bibliotecas:** `mysql-connector-python`, `tabulate`
- **Repositório:** Git + GitHub

## 📄 Documentação

- [📥 Escopo e Requisitos do Projeto](./Escopo_ClinicaPlus_v2.docx)

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.10+ instalado
- MySQL 8.0+ instalado e rodando
- Bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/clinicaplus.git
cd clinicaplus
```

**2. Crie o banco de dados:**

Abra o MySQL e execute os scripts:

```bash
mysql -u root -p -e "CREATE DATABASE clinicaplus;"
mysql -u root -p clinicaplus < db/schema.sql
mysql -u root -p clinicaplus < db/seed.sql
```

**3. Configure a conexão:**

Edite o arquivo `config.py` e ajuste suas credenciais do MySQL:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",       # seu usuário
    "password": "",       # sua senha
    "database": "clinicaplus"
}
```

**4. Execute o sistema:**

```bash
python main.py
```
