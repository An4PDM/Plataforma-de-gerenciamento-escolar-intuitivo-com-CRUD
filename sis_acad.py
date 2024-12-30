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

# Gerenciamento de materias
if escolha == 3:
    acao = int(input('''1: Para inserir uma matéria; 
2: Para deletar matéria; 
3: Para atualizar dados da matéria;
4: Para exibir os dados de todos as matérias: '''))
    

    id = int(input('id: '))
    n =input('Nome: ')
    c = input('Carga horária: ')


    if acao == 1:
        query = '''INSERT INTO materia 
                            VALUES (%s,%s,%s);'''
        cursor.execute(query,(id,n,c))
        bd.commit()
        print('Matéria registrada com sucesso.')

    elif acao == 2:
        query = '''DELETE FROM materia WHERE id_m = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        print('Matéria deletada com sucesso.')

    elif acao == 3:
        query = '''UPDATE materia SET nome = %s,
                                    carga_horaria = %s
                                    WHERE id_m = %s;'''
        cursor.execute(query,(n,c,id))
        bd.commit()
        print('Dados atualizados com sucesso.')

    elif acao == 4:
        query = '''SELECT * FROM materia;'''
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x)

# Gerenciamento de notas
if escolha == 4:
    acao = int(input('''1: Para inserir uma nota; 
2: Para deletar nota; 
3: Para atualizar a nota;
4: Para exibir as notas do aluno: '''))
    
    id = input('ID para a nota: ')
    ra =input('ra do aluno: ')
    id_materia = input('ID da matéria: ')
    n = input('Nota: ')


    if acao == 1:
        query = '''INSERT INTO nota 
                            VALUES (%s,%s,%s,%s);'''
        cursor.execute(query,(id,ra,id_materia,n))
        bd.commit()
        print('Nota registrada com sucesso.')

    elif acao == 2:
        query = '''DELETE FROM nota WHERE id_n = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        print('Nota deletada com sucesso.')

    elif acao == 3:
        query = '''UPDATE nota SET ra = %s,
                                    id_m = %s,
                                    nota = %s
                                    WHERE id_n = %s;'''
        cursor.execute(query,(ra,id_materia,n,id))
        bd.commit()
        print('Dados atualizados com sucesso.')

    elif acao == 4:
        query = '''SELECT a.nome AS 'Aluno', m.nome AS 'Matéria', n.nota 
                                    FROM nota n
                                    INNER JOIN aluno a ON a.ra = n.ra
                                    INNER JOIN materia m ON m.id_m = n.id_m;'''
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x)

