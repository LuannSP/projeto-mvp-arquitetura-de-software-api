from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from models.contact import Contact
from models import Session
from flask_cors import CORS
from schemas import *

info = Info(title="API QuickContact", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Tags
contact_tag = Tag(name="Contatos", description="Inserção, visualização, atualização e remoção de contatos na base de dados.")
documentation_tag = Tag(name="Documentação", description="Favor selecionar o estilo de documentação desejado dentre as seguintes opções: Swagger, Redoc ou RapiDoc.")


@app.get('/', tags=[documentation_tag])
def home():
    """Redireciona para /openapi, página que permite escolher o estilo de documentação."""
    return redirect('/openapi')


@app.post('/contato', tags=[contact_tag], responses={"200": ContactViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_contact(form: ContactSchema):
    """Adiciona um novo contato à base de dados e retorna uma representação do contato."""
    contact = Contact(
        nome=form.nome,
        telefone=form.telefone,
        email=form.email,
        cep=form.cep,
        rua=form.rua,
        bairro=form.bairro,
        cidade=form.cidade,
        uf=form.uf)
    try:
        session = Session()
        session.add(contact)
        session.commit()

        return present_contact(contact), 200

    except IntegrityError as e:
        error_msg = "Um contato com o mesmo telefone ou email já existe na base de dados."
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível adicionar o novo contato."
        return {"message": error_msg}, 400


@app.get('/contatos', tags=[contact_tag], responses={"200": ContactListSchema, "404": ErrorSchema})
def get_contacts():
    """Realiza a busca por todos os contatos cadastrados e retorna uma representação da listagem de contatos."""
    session = Session()
    contacts = session.query(Contact).all()

    if not contacts:
        return {"contatos": []}, 200
    else:
        return present_contacts(contacts), 200


@app.get('/contato', tags=[contact_tag], responses={"200": ContactViewSchema, "404": ErrorSchema})
def get_contact(query: ContactSearchByNameSchema):
    """Efetua uma pesquisa de todos os contatos registrados no banco de dados pelo nome."""
    contact_id = query.nome
    session = Session()
    contact = session.query(Contact).filter(Contact.nome == contact_id).first()

    if contact:
        return present_contact(contact), 200
    else:
        error_msg = "O contato não foi encontrado na base de dados."
        return {"message": error_msg}, 404


@app.delete('/contato', tags=[contact_tag], responses={"200": ContactDeleteSchema, "404": ErrorSchema})
def del_contact(query: ContactByID):
    """Remove um contato específico do banco de dados com base no ID fornecido."""
    id_contact = request.args.get('id_contato')

    try:
        id_contact = int(id_contact)
    except ValueError:
        return {"message": "ID do contato inválido."}, 400

    session = Session()
    count = session.query(Contact).filter(
        Contact.id_contato == id_contact).delete()
    session.commit()

    if count:
        return {"id_contato": id_contact, "message": "Contato removido."}
    else:
        error_msg = "Contato não encontrado na base de dados."
        return {"message": error_msg}, 404


@app.put('/contato', tags=[contact_tag], responses={"200": ContactViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def update_contact(query: ContactByID, form: ContactSchema):
    """Atualiza um contato específico na base de dados pelo ID e retorna uma representação atualizada do contato."""
    id_contact = request.args.get('id_contato')
    session = Session()
    try:
        contact = session.query(Contact).filter(
            Contact.id_contato == id_contact).first()
        if contact:
            contact.nome = form.nome
            contact.telefone = form.telefone
            contact.email = form.email
            contact.cep = form.cep
            contact.rua = form.rua
            contact.bairro = form.bairro
            contact.cidade = form.cidade
            contact.uf = form.uf
            session.commit()

            return present_contact(contact), 200
        else:
            error_msg = "O contato não foi encontrado na base de dados."
            return {"message": error_msg}, 404

    except Exception as e:
        error_msg = "Não foi possível atualizar o contato."
        return {"message": error_msg}, 400
