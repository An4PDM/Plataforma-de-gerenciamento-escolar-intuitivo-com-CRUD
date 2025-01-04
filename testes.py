import mysql.connector
from sis_acad import registro_aluno,registro_curso,registro_nota,registro_professor

# Conexão com o banco de dados
bd = mysql.connector.connect(
    host = 'localhost',
    user = 'usuario',
    password = 'senha_exemplo',
    database = 'sistema_academico'
)
cursor = bd.cursor()
# Teste das funções
registro_professor('Josué','Vicentino','m','1981-11-06')
registro_professor('Laura','Augusta','f','1981-04-15')
registro_professor('Rosi','K.','f','1979-08-16')

registro_curso('Biologia Marinha',1200)
registro_curso('Engenharia de Dados',1400)
registro_curso('Educação Física',1200)

cursor.execute('SELECT * FROM professor;')
result = cursor.fetchall()
for x in result:
        print(x)
