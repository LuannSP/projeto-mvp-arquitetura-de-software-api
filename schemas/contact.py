from pydantic import BaseModel
from typing import List
from models.contact import Contact


class ContactSchema(BaseModel):
    """ Define como um novo contato a ser inserido deve ser representado """
    nome: str = "Nome Contato"
    telefone: str = "00112233445"
    email: str = "email@example.com"
    cep: str = "12345678"
    rua: str = "Rua Exemplo"
    bairro: str = "Bairro Exemplo"
    cidade: str = "Cidade Exemplo"
    uf: str = "UF"


class ContactViewSchema(BaseModel):
    """ Define como um contato será retornado """
    id_contato: int = 1
    nome: str = "Nome Contato"
    telefone: str = "00112233445"
    email: str = "email@example.com"
    cep: str = "12345678"
    rua: str = "Rua Exemplo"
    bairro: str = "Bairro Exemplo"
    cidade: str = "Cidade Exemplo"
    uf: str = "UF"


class ContactSearchByNameSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por nome """
    nome: str = "Nome Contato"


class ContactByID(BaseModel):
    """ Define como deve ser a estrutura que representa a exclusão por ID """
    id_contato: int = 1


class ContactListSchema(BaseModel):
    """ Define como uma listagem de contatos será retornada """
    contatos: List[ContactViewSchema]


class ContactDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção """
    message: str
    id_contato: int


def present_contacts(contatos: List[Contact]):
    """ Retorna uma representação dos contatos seguindo o schema definido em ContactListSchema """
    result = []
    for contato in contatos:
        result.append({
            "id_contato": contato.id_contato,
            "nome": contato.nome,
            "telefone": contato.telefone,
            "email": contato.email,
            "cep": contato.cep,
            "rua": contato.rua,
            "bairro": contato.bairro,
            "cidade": contato.cidade,
            "uf": contato.uf
        })

    return {"contatos": result}


def present_contact(contato: Contact):
    """ Retorna uma representação do contato seguindo o schema definido em ContactViewSchema """
    return {
        "id_contato": contato.id_contato,
        "nome": contato.nome,
        "telefone": contato.telefone,
        "email": contato.email,
        "cep": contato.cep,
        "rua": contato.rua,
        "bairro": contato.bairro,
        "cidade": contato.cidade,
        "uf": contato.uf
    }
