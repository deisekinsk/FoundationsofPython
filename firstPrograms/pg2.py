import psycopg2

# Connect to your postgres DB
try: #Tratamento de exceção
    con = psycopg2.connect(
        "host=localhost dbname=projeto2 user=admin password=Dkr@2016")
    print("1.Conectou com banco de dados.")
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    exit()

# cur.execute("insert into produtos(nome, quantidade, preco) values ('banana', 30, 4.99);")
# cur.execute("update produtos $set preco=1.00 where id=2;")
# cur.execute("delete from produtos where id=1;")
# con.commit()
cur.execute("select * from produtos")
# print(cur.fetchone()) #Imprime um registros
print(cur.fetchall()) #Impreime todos os registros
print("2.Realizou execução no banco de dados.")

print("3.Finalizando conexãoo com o banco de dados.")
cur.close()
con.close()
