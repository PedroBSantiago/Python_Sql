# importar o módulo de mysql
import mysql.connector

conexao = mysql.connector.connect(host = 'localhost', database = 'db_nota', user = 'root', password = 'root')
# if connection.is_connected():
#     db_info = connection.get_server_info()
#     print('Conectado no servidor MySQL', db_info)
#     # cursor = ferramenta de manipulação (neste caso é o banco de dados)
#     cursor = connection.cursor()
#     cursor.execute('select database();')
#     line = cursor.fetchone()
#     print('Conectado ao banco de dados', line)

create_table = """create table tb_cliente(
                    nr_cnpj char(14) primary key,
                    nm_razao_social varchar(35) not null,
                    nm_pais varchar(20),
                    nm_email varchar(40) not null
                    );
                    
                    create table tb_produto(
	                    cd_produto int auto_increment primary key,
                        nm_produto varchar(25) not null,
                        vl_unitario decimal(5,2) not null
                        );

                    create table tb_nota(
	                    cd_nota int auto_increment primary key,
                        dt_emissao date not null,
                        dt_envio date not null,
                        vl_total decimal(6,2),
                        fk_nr_cnpj char(14),
                        foreign key (fk_nr_cnpj) references tb_cliente (nr_cnpj)
                        );

                    create table tb_produto_nota(
	                    cd_item int auto_increment primary key,
                        qt_produto int not null,
                        vl_total_item decimal(5,2),
                        fk_cd_produto int,
                        fk_cd_nota int,
                        foreign key (fk_cd_produto) references tb_produto (cd_produto),
                        foreign key (fk_cd_nota) references tb_nota (cd_nota)
                        );"""

cursor = conexao.cursor()
cursor.execute(create_table)
print('Tabela criada com sucesso!')