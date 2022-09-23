import pyodbc

dados = (
    "Driver={SQL Server};"
    "Server=LAPTOP-0TVV2ATR;" #PODE SER OBTIDO ABRINDO O PROMPT DE COMANDO E DIGITANDO "hostname"
    "Database=EXEMPLO_PYTHON;"
)

conexao = pyodbc.connect(dados)
print("Conexão realizada!")

cursor = conexao.cursor()

atualizar = """UPDATE TB_FUNCIONARIO
                SET SALARIO = 5000
                WHERE MATRICULA = 2"""

cursor.execute(atualizar)
cursor.commit()
print("Atualização realizada na tabela")