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

# Registro de materias
def registro_materia (n,c):
    query = '''INSERT INTO materia (nome,carga_horaria)
                            VALUES (%s,%s);'''
    cursor.execute(query,(n,c))
    bd.commit()
    print('Materia registrada com sucesso.')

# Registro de notas
def registro_nota (ra,id_c,n):
    query = '''INSERT INTO nota (ra,id_c,nota)
                            VALUES (%s,%s,%s)'''
    cursor.execute(query,(ra,id_c,n))
    bd.commit()
    print('Nota registrada com sucesso!')


# Opção de registrar, apagar ou atualizar dados
escolha = int(input('''Digite 1, caso queira gerenciar os dados de alunos; 
Digite 2, caso queira gerenciar os dados de professores;
Digite 3, caso queira gerenciar os dados de materias;
Digite 4, caso queira gerenciar as notas: '''))

# Gerenciamento de alunos
if escolha == 1:
    acao = int(input('''1: Para inserir aluno; 
2: Para deletar aluno; 
3: Para atualizar dados do aluno;
4: Para exibir os dados de todos os alunos: '''))
    

    ra = int(input('ra: '))
    n =input('Nome: ')
    s = input('Sobrenome: ')
    sx = input('Sexo (f,m,o): ')
    d = input('Data de nascimento: ')

    if acao == 1:
        query = '''INSERT INTO aluno 
                            VALUES (%s,%s,%s,%s,%s);'''
        cursor.execute(query,(ra,n,s,sx,d))
        bd.commit()
        print('Aluno registrado com sucesso.')

    elif acao == 2:
        query = '''DELETE FROM aluno WHERE ra = %s;'''
        cursor.execute(query,(ra,))
        bd.commit()
        print('Aluno deletado com sucesso.')

    elif acao == 3:
        query = '''UPDATE aluno SET nome = %s,
                                    sobrenome = %s,
                                    sexo = %s,
                                    data_nascimento = %s
                                    WHERE ra = %s;'''
        cursor.execute(query,(n,s,sx,d,ra))
        bd.commit()
        print('Dados atualizados com sucesso.')

    elif acao == 4:
        query = '''SELECT * FROM aluno;'''
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x)

# Gerenciamento de professores            
if escolha == 2:
    acao = int(input('''1: Para inserir professor; 
2: Para deletar professor; 
3: Para atualizar dados do professor;
4: Para exibir os dados de todos os professores: '''))

    id = int(input('id: '))
    cpf =input('cpf: ')
    n =input('Nome: ')
    s = input('Sobrenome: ')
    sx = input('Sexo (f,m,o): ')
    d = input('Data de nascimento: ')

    if acao == 1:
        query = '''INSERT INTO professor 
                            VALUES (%s,%s,%s,%s,%s,%s);'''
        cursor.execute(query,(id,cpf,n,s,sx,d))
        bd.commit()
        print('Professor registrado com sucesso.')

    elif acao == 2:
        query = '''DELETE FROM professor WHERE id_p = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        print('Professor deletado com sucesso.')

    elif acao == 3:
        query = '''UPDATE professor SET cpf = %s,
                                    nome = %s,
                                    sobrenome = %s,
                                    sexo = %s,
                                    data_nascimento = %s
                                    WHERE id_p = %s;'''
        cursor.execute(query,(cpf,n,s,sx,d,id))
        bd.commit()
        print('Dados atualizados com sucesso.')

    elif acao == 4:
        query = '''SELECT * FROM professor;'''
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x)

