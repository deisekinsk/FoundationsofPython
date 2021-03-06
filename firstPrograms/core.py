#Estrutura de criação de tabela por meio do Python e SqlAlchemy
from sqlalchemy import (create_engine, MetaData, Table,
                        Column, Integer, String, DateTime)

from datetime import datetime

engine = create_engine ('sqlite:///projeto.db', echo=True)
metadata = MetaData(bind=engine)

user_table = Table ('usuarios',
                    metadata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True),
                    Column('idade', Integer, nullable=False),
                    Column('senha', String),
                    Column('Criado_em ', DateTime, default=datetime.now),
                    Column('Atualizado_em', DateTime, default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)