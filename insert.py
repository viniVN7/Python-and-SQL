import pyodbc

dados = (
    "Driver={SQL Server};"
    "Server=LAPTOP-0TVV2ATR;" #Pode ser obtido abrindo o prompt de comando e digitando "hostname"
    "Database=EXEMPLO_PYTHON;"
)

conexao = pyodbc.connect(dados)
print("Conexão realizada!")

cursor = conexao.cursor()

inserir = """INSERT INTO TB_FUNCIONARIO (MATRICULA, NOME, CARGO, SALARIO)
             VALUES (1, 'JOSÉ', 'ANALISTA', 3500), (2, 'MARIA', 'DBA', 4500)"""

cursor.execute(inserir)
cursor.commit()
print("Inserção realizada na tabela")