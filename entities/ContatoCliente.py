from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ContatoCliente(Base):
    __tablename__ = 'contato_cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String(100))
    cpf_cliente = Column(String(14))
    email_cliente = Column(String(250))
    numero_pedido = Column(String(50))
    assunto = Column(String(250))
    mensagem = Column(String(1000))