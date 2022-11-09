import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'shikamaru',
    database = 'crud',
)

cursor = conexao.cursor()

# # CREATE
nomeProduto = input("Produto: ")
valor = int(input("Valor: "))
comando = f'INSERT INTO Vendas (nomeProduto, valor) VALUES ("{nomeProduto}", {valor})'
cursor.execute(comando)
conexao.commit()

# READ
# comando = 'select *from Vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() #Comando usado para ler o banco de dados
# print(resultado)

# # UPDATE
# comando = f'UPDATE Vendas SET valor = {valor} WHERE nomeProduto = "{nomeProduto}"'
# cursor.execute(comando)
# conexao.commit() #Comando para editar Banco de dados


# # DELETE
# nomeProduto = input("Produto: ")
# comando = f'DELETE FROM Vendas WHERE nomeProduto = "{nomeProduto}"'
# cursor.execute(comando)
# conexao.commit()

cursor.close()
conexao.close()

