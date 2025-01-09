import sqlite3


def criar_tabela():
    
    conexao = sqlite3.connect("Banco_Geral.db")
    cursor = conexao.cursor()

    print("Conexão estabelecida com sucesso!")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Alunos (
        Matricula INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        CPF TEXT UNIQUE NOT NULL,
        Email TEXT UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Português (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Matemática (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS História (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Geografia (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Física (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Biologia (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0,
        Nota_3 REAL DEFAULT 0.0,
        Media REAL DEFAULT 0.0,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Química (
        Matricula INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Nota_1 REAL DEFAULT 0.0,
        Nota_2 REAL DEFAULT 0.0 ,
        Nota_3 REAL DEFAULT 0.0 ,
        Media REAL DEFAULT 0.0 ,
        Situação TEXT DEFAULT 'Não confirmado'
    );
    """)

    print("Tabelas criadas com sucesso!")

    conexao.close()