from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint
from datetime import datetime
from typing import Union
from models import Base


class Contact(Base):
    __tablename__ = 'contatos'

    id_contato = Column("pk_contact", Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(11), nullable=False)
    email = Column(String(100), nullable=False)
    cep = Column(String(8), nullable=False)
    rua = Column(String(255), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    uf = Column(String(2), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now)

    __table_args__ = (UniqueConstraint(
        "telefone", name="contact_telefone_unique_id"),)
    __table_args__ = (UniqueConstraint(
        "email", name="contact_email_unique_id"),)

    def __init__(self, nome: str, telefone: str, email: str, cep: str, rua: str, bairro: str, cidade: str, uf: str, data_insercao: Union[datetime, None] = None):
        """
        Sobre a Tabela:
            nome: nome do contato.
            telefone: número do telefone/celular do contato.
            email: e-mail do contato.
            cep: cep do contato.
            rua: rua do contato.
            bairro: bairro do contato.
            cidade: cidade do contato.
            uf: unidade federativa do contato.
            data_insercao: data de quando o contato foi inserido.
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        return {
            "id_contato": self.id_contato,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "cep": self.cep,
            "rua": self.rua,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "data_insercao": self.data_insercao
        }

    def __repr__(self):
        return f"Contact(id_contato={self.id_contato}, nome='{self.nome}', telefone='{self.telefone}', email='{self.email}', cep='{self.cep}', rua='{self.rua}', bairro='{self.bairro}', cidade='{self.cidade}', uf='{self.uf}')"
