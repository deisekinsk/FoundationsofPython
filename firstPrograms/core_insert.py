from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

# new = ins.values(idade=24, nome='Deise', senha='Dkr@2000')
# con.execute(new)

con.execute(ins, [
    {'idade':4, 'nome': 'Iara', 'senha' :'Dkr@2001'},
    {'idade':37, 'nome':'Thomas', 'senha':'Dkr@2002'},

])
print('Executou.')