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

ALTER TABLE curso RENAME TO materia;
ALTER TABLE materia RENAME COLUMN id_c TO id_m;

CREATE TABLE nota (
	id_n INT PRIMARY KEY AUTO_INCREMENT,
    ra INT,
    id_m INT,
    nota DECIMAL(10,2),
    FOREIGN KEY (ra) REFERENCES aluno(ra),
    FOREIGN KEY (id_m) REFERENCES materia (id_m)
);

-- Inserção de dados
INSERT INTO aluno (nome, sobrenome, sexo, data_nascimento) 
VALUES ('Noah','Silveira','m','1999-10-28'),
('Bianca','Costa','f','2000-12-24'),
('Lana','Torres','o','2001-03-14'),
('José','Cunha','m','1998-04-20'),
('Maria','Nascimento','f','2000-09-30');

SELECT * FROM aluno;
SELECT * FROM professor;
SELECT * FROM nota;
SELECT * FROM materia;

-- Cálculo da média por matéria
SELECT m.nome AS Materia, round(AVG(n.nota),1) AS 'Média'
FROM nota n 
INNER JOIN aluno a ON a.ra = n.ra
INNER JOIN materia m ON m.id_m = n.id_m
WHERE a.ra = 1
GROUP BY m.nome;
