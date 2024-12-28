CREATE DATABASE sistema_academico;
USE sistema_academico;
SHOW TABLES;
CREATE TABLE aluno (
	ra INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45),
    sobrenome VARCHAR(45),
    sexo ENUM ('f','m','o'),
    data_nascimento DATE
);
DROP TABLE aluno;
CREATE TABLE professor (
	id_p INT PRIMARY KEY AUTO_INCREMENT,
    cpf CHAR(11) UNIQUE,
    nome VARCHAR(45),
    sobrenome VARCHAR(45),
    sexo ENUM ('f','m','o'),
    data_nascimento DATE
);
DROP TABLE professor;
CREATE TABLE curso (
	id_c INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45) UNIQUE,
    carga_horaria FLOAT
);
CREATE TABLE nota (
	id_n INT PRIMARY KEY AUTO_INCREMENT,
    ra INT,
    id_c INT,
    nota DECIMAL(10,2),
    FOREIGN KEY (ra) REFERENCES aluno(ra),
    FOREIGN KEY (id_c) REFERENCES curso (id_c)
);
DROP TABLE nota;
-- Inserção de dados
INSERT INTO aluno (nome, sobrenome, sexo, data_nascimento) 
VALUES ('Noah','Silveira','m','1999-10-28'),
('Bianca','Costa','f','2000-12-24'),
('Lana','Torres','o','2001-03-14'),
('José','Cunha','m','1998-04-20'),
('Maria','Nascimento','f','2000-09-30');
SELECT * FROM aluno;