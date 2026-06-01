CREATE DATABASE clinicaplus;
USE clinicaplus;
 
-- ------------------------------------------------
-- Tabela: pacientes
-- ------------------------------------------------
CREATE TABLE pacientes (
    id        INT           AUTO_INCREMENT PRIMARY KEY,
    nome      VARCHAR(100)  NOT NULL,
    cpf       VARCHAR(14)   NOT NULL UNIQUE,
    telefone  VARCHAR(20),
    data_nasc DATE          NOT NULL
);
 
-- ------------------------------------------------
-- Tabela: medicos
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS medicos (
    id            INT          AUTO_INCREMENT PRIMARY KEY,
    nome          VARCHAR(100) NOT NULL,
    especialidade VARCHAR(80)  NOT NULL,
    crm           VARCHAR(20)  NOT NULL UNIQUE
);
 
-- ------------------------------------------------
-- Tabela: consultas
-- ------------------------------------------------
CREATE TABLE IF NOT EXISTS consultas (
    id          INT       AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT       NOT NULL,
    medico_id   INT       NOT NULL,
    data_hora   DATETIME  NOT NULL,
    status      ENUM('agendada', 'cancelada') NOT NULL DEFAULT 'agendada',
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (medico_id)   REFERENCES medicos(id)
    );