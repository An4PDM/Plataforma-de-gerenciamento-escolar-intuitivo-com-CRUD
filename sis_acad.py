import mysql.connector
import PySimpleGUI as sg

# Conexão com o banco de dados
bd = mysql.connector.connect(
    host = 'localhost',
    user = 'usuario',
    password = 'senha_exemplo',
    database = 'sistema_academico'
)
cursor = bd.cursor()

# Gerenciamento de dados de alunos
def gerenciar_aluno(acao, ra, n, s, sx, d):
    if acao == 1:
        query = '''INSERT INTO aluno 
                            VALUES (%s,%s,%s,%s,%s);'''
        cursor.execute(query,(ra,n,s,sx,d))
        bd.commit()
        return 'Aluno registrado com sucesso.'

    elif acao == 2:
        query = '''DELETE FROM aluno WHERE ra = %s;'''
        cursor.execute(query,(ra,))
        bd.commit()
        return 'Aluno deletado com sucesso.'

    elif acao == 3:
        query = '''UPDATE aluno SET nome = %s,
                                    sobrenome = %s,
                                    sexo = %s,
                                    data_nascimento = %s
                                    WHERE ra = %s;'''
        cursor.execute(query,(n,s,sx,d,ra))
        bd.commit()
        return 'Dados atualizados com sucesso.'

    elif acao == 4:
        query = '''SELECT * FROM aluno;'''
        cursor.execute(query)
        result = cursor.fetchall()
        result_str = ''
        for x in result:
            result_str += f'{x}\n'
        return result_str

# Gerenciamento de professores            
def gerenciar_professores (acao, id, cpf, n, s, sx, d):
    if acao == 1:
        query = '''INSERT INTO professor 
                            VALUES (%s,%s,%s,%s,%s,%s);'''
        cursor.execute(query,(id,cpf,n,s,sx,d))
        bd.commit()
        return 'Professor registrado com sucesso.'

    elif acao == 2:
        query = '''DELETE FROM professor WHERE id_p = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        return 'Professor deletado com sucesso.'

    elif acao == 3:
        query = '''UPDATE professor SET cpf = %s,
                                    nome = %s,
                                    sobrenome = %s,
                                    sexo = %s,
                                    data_nascimento = %s
                                    WHERE id_p = %s;'''
        cursor.execute(query,(cpf,n,s,sx,d,id))
        bd.commit()
        return 'Dados atualizados com sucesso.'

    elif acao == 4:
        query = '''SELECT * FROM professor;'''
        cursor.execute(query)
        result = cursor.fetchall()
        result_str = ''
        for x in result:
            result_str += f'{x}\n'
        return result_str

# Gerenciamento de materias
def gerenciar_materias(acao, id, n, c):
    if acao == 1:
        query = '''INSERT INTO materia 
                            VALUES (%s,%s,%s);'''
        cursor.execute(query,(id,n,c))
        bd.commit()
        return 'Matéria registrada com sucesso.'

    elif acao == 2:
        query = '''DELETE FROM materia WHERE id_m = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        return 'Matéria deletada com sucesso.'

    elif acao == 3:
        query = '''UPDATE materia SET nome = %s,
                                    carga_horaria = %s
                                    WHERE id_m = %s;'''
        cursor.execute(query,(n,c,id))
        bd.commit()
        return 'Dados atualizados com sucesso.'

    elif acao == 4:
        query = '''SELECT * FROM materia;'''
        cursor.execute(query)
        result = cursor.fetchall()
        result_str = ''
        for x in result:
            result_str += f'{x}\n'
        return result_str

# Gerenciamento de notas
def gerenciar_notas(acao, id, ra, id_materia, n):  
    if acao == 1:
        query = '''INSERT INTO nota 
                            VALUES (%s,%s,%s,%s);'''
        cursor.execute(query,(id,ra,id_materia,n))
        bd.commit()
        return 'Nota registrada com sucesso.'

    elif acao == 2:
        query = '''DELETE FROM nota WHERE id_n = %s;'''
        cursor.execute(query,(id,))
        bd.commit()
        return 'Nota deletada com sucesso.'

    elif acao == 3:
        query = '''UPDATE nota SET ra = %s,
                                    id_m = %s,
                                    nota = %s
                                    WHERE id_n = %s;'''
        cursor.execute(query,(ra,id_materia,n,id))
        bd.commit()
        return 'Dados atualizados com sucesso.'

    elif acao == 4:
        query = '''SELECT a.nome AS 'Aluno', m.nome AS 'Matéria', n.nota 
                                    FROM nota n
                                    INNER JOIN aluno a ON a.ra = n.ra
                                    INNER JOIN materia m ON m.id_m = n.id_m;'''
        cursor.execute(query)
        result = cursor.fetchall()
        result_str = ''
        for x in result:
            result_str += f'{x}\n'
        return result_str

    # Calculo da média por materia
    elif acao == 5:
        ra = input('Insira o ra do aluno: ')
        query = '''SELECT m.nome AS Materia, round(AVG(n.nota),1) AS 'Média'
                                    FROM nota n 
                                    INNER JOIN aluno a ON a.ra = n.ra
                                    INNER JOIN materia m ON m.id_m = n.id_m
                                    WHERE a.ra = %s
                                    GROUP BY m.nome;'''
        cursor.execute(query,(ra,))
        result = cursor.fetchall()
        result_str = ''
        for x in result:
            result_str += f'{x}\n'
        return result_str

# Criação do layout
layout = [
    [sg.Text('Escolha uma opção:')],
    [sg.Combo(['Gerenciar alunos','Gerenciar professores','Gerenciar matérias','Gerenciar notas'],key='-MENU-',readonly=True)],

    [sg.Text('RA ou ID (se aplicável): '), sg.Input(key='-RA-ID-')],
    [sg.Text('Nome: '), sg.Input(key='-NOME-')],
    [sg.Text('Sobrenome: '), sg.Input(key='-SOBRENOME-')],
    [sg.Text('CPF (apenas para professor): '), sg.Input(key='-CPF-')],
    [sg.Text('Sexo: (f/m/o)'), sg.Combo(['f','m','o'],key='-SEXO-')],
    [sg.Text('Data de Nacimento: '), sg.Input(key='-DATA-')],
    [sg.Text('ID da Matéria (se aplicável): '), sg.Input(key='-ID-MATERIA-')],
    [sg.Text('Carga Horária (se aplicável): '), sg.Input(key='-CARGA-')],
    [sg.Text('Nota (se aplicável): '),sg.Input(key='-NOTA-')],
    

    [sg.Text('Ação:')],
    [sg.Combo(['1 - Inserir','2 - Deletar','3 - Atualizar','4 - Exibir','5 - Exibir médias'], key='-ACAO-',readonly=True)],

    [sg.Button('Executar'), sg.Button('Sair')],

    [sg.Text('Resultado:',size=(40,1))],
    [sg.Multiline('',size=(50,10),key='-RESULT-')]
]

# Criação da janela
window = sg.Window('Sistema Acadêmico', layout)

# Interações do user
while True:
    event,values = window.read() # Espera por interações

    if event == sg.WINDOW_CLOSED or event == 'Sair': #Saida do sistema
        break

    # Obtenção dos dados
    acao = int(values['-ACAO-'][0]) if values['-ACAO-'] else 0
    menu = values['-MENU-']
    id = values['-RA-ID-']
    n = values['-NOME-']
    s = values['-SOBRENOME-']
    cpf = values['-CPF-']
    sx = values['-SEXO-']
    d = values['-DATA-']
    id_materia = values['-ID-MATERIA-']
    c = values['-CARGA-']
    nota = values['-NOTA-']

    # Seleção da função correspondente ao menu
    if 'Gerenciar alunos' in menu:
        result = gerenciar_aluno(acao,id,n,s,sx,d)
    
    elif 'Gerenciar professores' in menu:
        result = gerenciar_professores(acao,id,cpf,n,s,sx,d)

    elif 'Gerenciar matérias' in menu:
        result = gerenciar_materias(acao,id,n,c)

    elif 'Gerenciar notas' in menu:
        result = gerenciar_notas(acao,id,id,id_materia,nota)

    # Exibição dos resultados
    window['-RESULT-'].update(result)

window.close()
