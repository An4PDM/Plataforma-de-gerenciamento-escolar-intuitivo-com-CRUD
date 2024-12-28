import mysql.connector
# Conexão com o banco de dados
bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '16092005Dn!',
    database = 'sistema_academico'
)
cursor = bd.cursor()

# Registo de alunos
def registro_aluno (n,s,sx,d):
    query = '''INSERT INTO aluno (nome, sobrenome, sexo, data_nascimento)
                            VALUES (%s,%s,%s,%s);'''
    cursor.execute(query,(n,s,sx,d))
    bd.commit()
    print('Aluno registrado com sucesso.')

# Registro de professores
def registro_professor (n,s,sx,d):
    query = '''INSERT INTO professor (nome, sobrenome, sexo, data_nascimento)
                            VALUES (%s,%s,%s,%s);'''
    cursor.execute(query,(n,s,sx,d))
    bd.commit()
    print('Professor registrado com sucesso.')

# Registro de cursos
def registro_curso (n,c):
    query = '''INSERT INTO curso (nome,carga_horaria)
                            VALUES (%s,%s);'''
    cursor.execute(query,(n,c))
    bd.commit()
    print('Curso registrado com sucesso.')

# Registro de notas
def registro_nota (ra,id_c,n):
    query = '''INSERT INTO nota (ra,id_c,nota)
                            VALUES (%s,%s,%s)'''
    cursor.execute(query,(ra,id_c,n))
    bd.commit()
    print('Nota registrada com sucesso!')
