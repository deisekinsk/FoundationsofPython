from pymongo import MongoClient
from pprint import pprint #Imprime de uma forma mais legível.
from bson import ObjectId 

try:
    con = MongoClient()
    db = con['projeto']
    print("Acessou o banco de dados")
except Exception as e:
    print("Erro:{}".format(e))
    exit()

# db.produtos.insert({'_id':4, 'nome':'jaca', 'quantidade': 8 , 'preco': 1.50})
# db.produtos.insert_one({'_id':5, 'nome':'melão', 'quantidade': 5 , 'preco': 3.99})
# print("Realizou a modificação/consulta no bando de dados.")
# print(db.produtos.find_one()) #Retorna um valor da base.?
# db.produtos.delete_one({'_id':4})
# db.produtos.remove({'_id': ObjectId('5fa5ad118428dbe83a8a4e3c')})

# db.produtos.update(
#     {'_id': ObjectId('5fa5acab8428dbe83a8a4e3a')},
#     {'$set': {'quantidade':8.0}}) #remove tudo

#Usar PUSH para inserir. E PULL para remover.

db.produtos.update(
    {'_id': 4},
    {'$unset': {'projetos':''}}) #remove uma coluna


for x in db.produtos.find():#loop para trazer todos os dados do banco.
    print(x)
    
# print([x for x in db.produtos.find()]) #para trazer os dados em formato de lista.