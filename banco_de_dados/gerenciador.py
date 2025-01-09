import sqlite3
from banco_de_dados.diversos import validar_cpf, verifica_ext_geral, verifica_ext_mat, fmt_nome, calcular_media


class EXE:
    def __init__(self, banco='Banco_Geral.db'):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()
        
    def add_aluno(self, nome, cpf, email):
        try:
            self.cursor.execute('INSERT INTO Alunos (Nome, CPF, Email) VALUES (?, ?, ?)',(nome, cpf, email))
            self.conexao.commit()
            print('Aluno Adicionado com sucesso! ')
        except sqlite3.Error as e:
            print(f'Erro: {e}')
            
    def r_aluno(self, tipo, entrada, tabela):
        try:
            if verifica_ext_mat(entrada, tabela):
                if tipo != 'q':
                    bancos = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                    if tipo == '1':
                        tabela = int(tabela)
                        self.cursor.execute(f'DELETE FROM {bancos[tabela]} WHERE Matricula = ?;', (entrada,))
                        print('Aluno removido com sucesso! ')
                        
                    elif tipo == '2':
                            for i in bancos:
                                if verifica_ext_mat(entrada, i):
                                    self.cursor.execute(f'DELETE FROM {i} WHERE Matricula = ?;', (entrada))
                            print(f'Aluno removido de: {bancos}')
                                                           
                    elif tipo == '3':
                        aviso = str(input('ATENÇÃO! Essa ação irá remover esse aluno e todos seus dados do nosso sistema\n[c]Continuar\n[q]Voltar\n')).lower()
                        if aviso == 'c':
                            bancos = ['Alunos', 'Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                            for i in bancos:
                                if verifica_ext_mat(entrada, i):
                                    self.cursor.execute(f'DELETE FROM {i} WHERE Matricula = ?;', (entrada,))
                            print('Aluno removido do sistema com sucesso!')
                        elif aviso == 'q':
                            pass
                        else:
                            print('Escolha uma das opções acima! ')
                        
                elif tipo == 'q':
                    pass
                else:
                    print('Por favor escolha uma das opções acima.')
                self.conexao.commit()
            else:
                print('Esse aluno não está cadastrado em nosso sistema. ')
                    
        except sqlite3.Error as e:
            print(f'Erro ao remover o aluno: {e}')
       
    def editar_aluno(self,matricula,escolha):
        try:
            if escolha == '1':
                novo_nome = str(input('Digite o nome completo do aluno: '))
                novo_nome = fmt_nome(novo_nome)
                self.cursor.execute(f'UPDATE Alunos SET Nome = ? WHERE Matricula = ?;', (novo_nome, matricula,))
                print('Nome atualizado com sucesso! ')
            elif escolha == '2':
                novo_cpf = str(input('Digite o novo CPF do aluno: '))
                if validar_cpf(novo_cpf):
                    self.cursor.execute(f'UPDATE Alunos SET CPF = ? WHERE Matricula = ?;', (novo_cpf, matricula,))
                    print('CPF atualizado com sucesso!')
            elif escolha == '3':
                novo_email = str(input('Digite o novo email do aluno: '))
                self.cursor.execute(f'UPDATE Alunos SET Email = ? WHERE Matricula = ?;', (novo_email, matricula,))
                print('Email atualizado com sucesso! ')
            self.conexao.commit()
        except sqlite3.Error as e:
            print(f'Erro: {e}')
        
    def mostrar_aluno(self, tipo, matricula, tabela):
        try:
            if tipo == '1':
                self.cursor.execute(f"SELECT * FROM {tabela};")
                linhas = self.cursor.fetchall()
                colunas = [desc[0] for desc in self.cursor.description]
                if linhas:
                    print(f"{' | '.join(colunas)}")
                    print("-" * 50)
                    for linha in linhas:
                        print(" | ".join(str(campo) for campo in linha))
                    print()
                    print()
                else:
                    print(f"A tabela '{tabela}' está vazia.")
                    
            elif tipo == '2':
                self.cursor.execute(f"SELECT * FROM {tabela} WHERE Matricula = ?;", (matricula,))
                colunas = [desc[0] for desc in self.cursor.description]
                linha = self.cursor.fetchone()
                if linha:
                    print(f"{' | '.join(colunas)}")
                    print("-" * 50)
                    print(" | ".join(str(campo) for campo in linha))
                    print()
                    print()
                else:
                    print(f"Aluno não encontrado")
            else:
                print('Escolha uma opção valida! ')
                       
        except sqlite3.Error as e:
            print(f'Erro: {e}')
        
    def add_materia(self, tipo, entrada, materia):
        try:
            if verifica_ext_geral(entrada):
                if tipo == '1':
                    self.cursor.execute(f'INSERT INTO {materia} (Matricula, Nome) SELECT Matricula, Nome FROM Alunos WHERE Matricula = ?;', (entrada,))
                    print(f'Aluno matriculado em {materia}.')
                elif tipo == '2':
                    tabelas = ['Biologia', 'Física', 'Geografia', 'História', 'Matemática', 'Português', 'Química']
                    for tabela in tabelas:
                        if not verifica_ext_mat(entrada, tabela):
                            self.cursor.execute(f"INSERT INTO {tabela} (Matricula, Nome) SELECT Matricula, Nome FROM Alunos WHERE Matricula = ?;", (entrada,))
                    print(f'Aluno matriculado em todas as matérias. ') 
                
                elif tipo == 'q':
                    pass
                else:
                    print('Escolha uma das opções válidas.')
                self.conexao.commit()
            else:
                print('Esse aluno não está cadastrado em nosso sistema.')
        except sqlite3.Error as e:
            print(f'Erro ao adicionar matéria: {e}')

    def add_nota(self, matricula, materia, posicao, nota):
        try:
            if verifica_ext_mat(matricula, materia):
                self.cursor.execute(f"UPDATE {materia} SET {posicao} = ? WHERE Matricula = ?;", (nota, matricula))
                self.conexao.commit()
                print('Nota Modificada com Sucesso! ')
            else:
                print(f'Esse aluno não está cadastrado nessa turma. ')
            self.conexao.commit()
        except sqlite3.Error as e:
            print(f'Erro: {e}')

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            
    def lançar_media(self, matricula, materia):
        try:
            self.cursor.execute(f'SELECT Nota_1 FROM {materia} WHERE Matricula = ?;', (matricula,))
            nota1 = self.cursor.fetchone()
            nota1 = nota1[0]
            self.cursor.execute(f'SELECT Nota_2 FROM {materia} WHERE Matricula = ?;', (matricula,))
            nota2 = self.cursor.fetchone()
            nota2 = nota2[0]
            self.cursor.execute(f'SELECT Nota_3 FROM {materia} WHERE Matricula = ?;', (matricula,))
            nota3 = self.cursor.fetchone()
            nota3 = nota3[0]
            
            media = calcular_media(nota1,nota2,nota3)
            self.cursor.execute(f'UPDATE {materia} SET Media = ? WHERE Matricula = ?;', (media, matricula))
            self.conexao.commit()
        except sqlite3.Error as e:
            print(f'Erro: {e}')