import pyodbc

conexao = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-0TVV2ATR;"
    "Database=EXEMPLO_PYTHON;"
)

print("Conexão realizada!")

cursor = conexao.cursor()

select = """SELECT * FROM TB_FUNCIONARIO"""

cursor.execute(select)

print("Dados presentes na tabela:")
for i in cursor:
    print(i)