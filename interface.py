from banco_de_dados.gerenciador import EXE
from banco_de_dados.diversos import limpar, fmt_nome, verifica_ext_geral, verifica_ext_mat, validar_cpf
from banco_de_dados.criador import criar_tabela


exe = EXE()
limpar(0)

def start():
    criar_tabela()
    limpar(1)     
    print(f'Bem Vindo(a)')
    
    while True:
        limpar(0)
        escolha = str(input('''O que gostaria de fazer?\n
[1]Adicionar, Remover ou Editar um aluno.
[2]Matricular aluno em uma matéria.
[3]Modificar a nota de um aluno.
[4]Exibir alunos matriculados
[q]Sair
'''))
        
        limpar(0)
        
        if escolha == '1':
            while True:
                limpar(1)
                subescolha = str(input('O que gostaria de fazer?\n[1]Adicionar um aluno.\n[2]Remover um aluno.\n[3]Editar dados de um aluno\n[q]Voltar\n'))
                if subescolha == '1':
                    limpar(0)
                    nome = str(input(f'Qual o nome do aluno? '))
                    nome = str(fmt_nome(nome))
                    cpf = str(input(f'Qual o CPF do aluno? '))
                    if not verifica_ext_geral(cpf):
                        if validar_cpf(cpf):
                            email = str(input(f'Qual o email do aluno? '))
                            exe.add_aluno(nome,cpf,email)
                        else:
                            print('Esse CPF não existe. ')
                    else:
                        print('Esse Aluno já está cadastrado em nosso sistema! ')
                          
                elif subescolha == '2':
                    limpar(0)
                    mat = str(input('Qual a matricula do aluno: '))
                    if verifica_ext_geral(mat):
                        subescolha_2 = str(input('O que gostaria de fazer?\n[1]Remover de uma materia especifica\n[2]Remover de todas as matérias\n[3]Excluir aluno do sistema\n'))
                        limpar(0)
                        if subescolha_2 == '1':
                            banco = str(input('Gostaria de remover o aluno de qual matéria?\n[0]Biologia\n[1]Fisica\n[2]Geografia\n[3]História\n[4]Matematica\n[5]Portugues\n[6]Quimica\n'))
                            exe.r_aluno(subescolha_2,mat,banco)
                        elif subescolha_2 == '2':
                            exe.r_aluno(subescolha_2,mat,'Alunos')
                        elif subescolha_2 == '3':
                            exe.r_aluno(subescolha_2,mat,'Alunos')
                        else:
                            print('Escolha uma opção valida! ')

                elif subescolha == '3':
                    mat = str(input('Qual a matricula do aluno que gostaria de modificar? '))
                    if verifica_ext_geral(mat):
                        while True:
                            subescolha_2 = str(input('O que gostaria de fazer?\n[1]Alterar o nome do aluno.\n[2]Alterar o CPF do aluno\n[3]Alterar o email do aluno\n[q]Voltar\n'))
                            if subescolha_2 == '1':
                                exe.editar_aluno(mat,subescolha_2)
                            elif subescolha_2 == '2':
                                exe.editar_aluno(mat,subescolha_2)
                            elif subescolha_2 == '3':
                                exe.editar_aluno(mat,subescolha_2)
                            elif subescolha_2 == 'q':
                                break
                            else:
                                print('Escolha uma das opções acima! ')
                    else:
                        print('Escolha uma opção valida! ')
                                             
                elif subescolha == 'q':
                    break
                         
                else:
                    print('Escolha das opções validas! ')
                         
        if escolha == '2':
            mat = str(input('Digite a matricula do aluno: '))
            if verifica_ext_mat(mat,'Alunos'):
                while True:
                    limpar(0)
                    opcao = str(input('Onde gostaria adicionar o aluno?\n[1]Adicionar em uma matéria especifica\n[2]Adicionar em todas as matérias\n[q]Voltar\n'))
                    
                    if opcao == '1':
                        escolher_materia = int(input('Qual materia gostaria de matricular o aluno?\n[0]Biologia\n[1]Fisica\n[2]Geografia\n[3]História\n[4]Matematica\n[5]Portugues\n[6]Quimica\n'))
                        materias = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                        exe.add_materia(opcao,mat,materias[escolher_materia])
                    elif opcao == '2':
                        exe.add_materia(opcao,mat,'tudo')
                    elif opcao == 'q':
                        exe.add_materia(opcao,mat,'Sair')
                        break
                    else:
                        print('Escolha uma opção valida! ')
                        
            else:
                print('Esse usuario não está cadastrado no sistema. ')
                 
        elif escolha == '3':
            mat = str(input('Digite a matricula do aluno: '))
            if verifica_ext_geral(mat):
                    while True: 
                        limpar(0.5)                 
                        escolher_materia = (input('Qual materia gostaria de alterar a nota o aluno?\n[0]Biologia\n[1]Fisica\n[2]Geografia\n[3]História\n[4]Matematica\n[5]Portugues\n[6]Quimica\n[q]Voltar\n'))
                        if escolher_materia != 'q':
                            escolher_materia = int(escolher_materia)
                            materias = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                            while True:
                                prova = str(input('Escolha a prova que gostaria de  modificar:\n[1]Prova 1\n[2]Prova 2\n[3]Prova 3\n '))
                                limpar(0)
                                if prova == '1':
                                    prova = 'Nota_1'
                                    break
                                elif prova == '2':
                                    prova = 'Nota_2'
                                    break
                                elif prova == '3':
                                    prova = 'Nota_3'
                                    break
                                else:
                                    print('Escolha um dos valores acima! ')
                            nota = float(input('Digite a nota: '))
                            exe.add_nota(mat,materias[escolher_materia],prova,nota)
                            exe.lançar_media(mat,materias[escolher_materia])
                            limpar(0.5)
                        elif escolher_materia == 'q':
                            break
            
        elif escolha == '4':
            subescolha = str(input('O que gostaria de fazer?\n[1]Listar todos os alunos matriculados.\n[2]Listar um aluno especifico.\n[q]Voltar.\n'))
            limpar(0)
            if subescolha == '1':
                while True:
                    subescolha_2 = str(input('O que gostaria de ver?\n[1]Listar todos os alunos matriculas na escola.\n[2]Listar todos os alunos matriculados em uma turma especifica.\n[q]Voltar\n'))
                    limpar(0)
                    if subescolha_2 == '1':
                        limpar(0)
                        exe.mostrar_aluno(subescolha,'none','Alunos')
                    elif subescolha_2 == '2':
                        while True:
                            subescolha_3 = str(input('Qual materia gostaria de listar?\n[0]Biologia\n[1]Fisica\n[2]Geografia\n[3]História\n[4]Matematica\n[5]Portugues\n[6]Quimica\n[q]Voltar\n'))
                            limpar(0)
                            if subescolha_3 != 'q':
                                subescolha_3 = int(subescolha_3)
                                materias = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                                limpar(0)
                                print(materias[subescolha_3])
                                exe.mostrar_aluno(subescolha,'none',materias[subescolha_3])
                            elif subescolha_3 == 'q':
                                break
                            else:
                                print('Escolha uma opção valida! ')
                    elif subescolha_2 == 'q':
                        break
                    else:
                        print('Escolha uma opção valida! ')
            elif subescolha == '2':
                mat = str(input('Digite a matricula do aluno: '))
                limpar(0)
                if verifica_ext_geral(mat):
                    while True:
                        subescolha_2 = str(input('O que gostaria de fazer?\n[1]Listar dados do aluno.\n[2]Listar situação em uma matéria especifica.\n[q]Voltar\n'))
                        limpar(0)
                        if subescolha_2 == '1':
                            exe.mostrar_aluno(subescolha,mat,'Alunos')
                        elif subescolha_2 == '2':
                            while True:
                                subescolha_3 = str(input('Qual materia gostaria de listar?\n[0]Biologia\n[1]Fisica\n[2]Geografia\n[3]História\n[4]Matematica\n[5]Portugues\n[6]Quimica\n[q]Voltar\n'))
                                limpar(0)
                                if subescolha_3 != 'q':
                                    subescolha_3 = int(subescolha_3)
                                    materias = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                                    print(materias[subescolha_3])
                                    exe.mostrar_aluno(subescolha,mat,materias[subescolha_3])
                                elif subescolha_3 == 'q':
                                    break
                                else:
                                    print('Escolha uma opção valida! ')
                        elif subescolha_2 == 'q':
                            break
                        else:
                            print('Escolha uma das opções válidas')
                else:
                    print('Essa matricula não está registrada em nosso sistema. ')
            else:
                print('Escolha uma opção valida! ')        
            
        elif escolha == 'q':
            print('Obrigado por usar o nosso sistema!')
            break
        
        else:
            print('Escolha uma das opções acima! ')
        
    exe.conexao.commit()
    exe.fechar_conexao()