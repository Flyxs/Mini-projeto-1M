from time import sleep
from os import system
import sqlite3

def limpar(a):
    sleep(a)
    return system('clear')

limpar(0)

def validar_cpf(cpf):
    cpf = ''.join([char for char in cpf if char.isdigit()])
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf_parcial, peso_inicial):
        soma = sum(int(cpf_parcial[i]) * (peso_inicial - i) for i in range(len(cpf_parcial)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito = calcular_digito(cpf[:9], 10)
    segundo_digito = calcular_digito(cpf[:10], 11)

    if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
        return True
    else:
        print('Esse CPF não existe! ')
        return False

def verifica_ext_geral(entrada):
    conexao = sqlite3.connect("Banco_Geral.db")
    cursor = conexao.cursor()
    try:
        cursor.execute(f'SELECT 1 FROM Alunos WHERE Matricula = ? OR CPF = ?;',(entrada, entrada))
        resultado = cursor.fetchone()
        return bool(resultado)
    except sqlite3.Error as e:
        print(f'Erro: {e} ')
        return False
        
def verifica_ext_mat(entrada,banco):
    conexao = sqlite3.connect("Banco_Geral.db")
    cursor = conexao.cursor()
    try:
        cursor.execute(f'SELECT 1 FROM {banco} WHERE Matricula = ?;',(entrada,))
        resultado = cursor.fetchone()
        return bool(resultado)
    except sqlite3.Error as e:
        print(f'Erro: {e} ')
        return False
        
def fmt_nome(a):
    nome = str(a)
    nome = nome.split(' ')
    nome = [i.capitalize() for i in nome]
    nome = ' '.join(nome)
    return nome

def calcular_media(a,b,c):
    try:
        a, b, c = map(float, (a,b,c))
        media = (a+b+c)/3
        media = round(media, 2)
        return media
    except ValueError:
        print('Erro: todos os parametros devem ser numeros inteiros. ')
        return None