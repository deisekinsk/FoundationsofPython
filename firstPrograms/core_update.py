from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'Thomas')

commit = atualizar.values(nome='Joseph Thomas')
result = con.execute(commit)

print(result.rowcount)