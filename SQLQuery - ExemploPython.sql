CREATE DATABASE EXEMPLO_PYTHON

USE EXEMPLO_PYTHON

CREATE TABLE TB_FUNCIONARIO (
	MATRICULA INT PRIMARY KEY,
	NOME VARCHAR(50) NOT NULL,
	CARGO VARCHAR(40) NOT NULL,
	SALARIO NUMERIC(10,2) NOT NULL
)

SELECT * FROM TB_FUNCIONARIO

TRUNCATE TABLE TB_FUNCIONARIO -- LIMPAR DADOS DA TABELA