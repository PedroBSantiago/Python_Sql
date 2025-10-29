import mysql.connector
# conexão com o banco de dados db_nota
conexao = mysql.connector.connect(host = 'localhost', database = 'db_nota', user = 'root', password = 'root')

#criar a instrução que será executada no banco

nr_cnpj = input('Digite o CNPJ: ')
nm_razao_social = input('Digite o nome da razão: ')
nm_pais = input('Digite o País: ')
nm_email = input('Digite seu email: ')

insert_cliente = f"insert into tb_cliente values ('{nr_cnpj}','{nm_razao_social}','{nm_pais}','{nm_email}');"

# comandos para executar dentro do banco de dados no banco db_nota
cursor = conexao.cursor()
cursor.execute(insert_cliente)
conexao.commit()
print('Inserido com sucesso!')