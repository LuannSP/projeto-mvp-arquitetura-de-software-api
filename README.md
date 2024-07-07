# API QuickContact

Este projeto é parte do material didático da disciplina **Arquitetura de Software** e apresenta uma API implementada no estilo REST.

### Tecnologias Principais:
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) - Framework web em Python.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Ferramenta de ORM para Python.
- [OpenAPI3](https://swagger.io/specification/) - Especificação para documentação de APIs.
- [SQLite](https://www.sqlite.org/index.html) - Banco de dados embutido.

## API ViaCEP

### Descrição
A API VIACEP é uma ferramenta gratuita para consulta de CEPs (Códigos de Endereçamento Postal) do Brasil. Através dela, é possível obter informações detalhadas sobre endereços a partir de um CEP fornecido.

### Licença de Uso
A API VIACEP é de uso gratuito e não requer licença específica. Ela está disponível para uso público sem necessidade de pagamento ou registro, conforme indicado no site oficial.

### Rotas Utilizadas

No projeto é usado a rota de consulta de CEP.

**Descrição:** Retorna informações de endereço a partir de um CEP.

**Método HTTP:** GET

**URL:** https://viacep.com.br/ws/{cep}/json/

**Parâmetros:**
{cep}: O CEP desejado (somente números, sem hífen ou espaço).

Exemplo de Uso:
```
https://viacep.com.br/ws/01001000/json/
```

---
### Instalação

Para instalar as dependências, certifique-se de ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas. 
> Recomenda-se o uso de ambientes virtuais como [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env) pip install -r requirements.txt
```

---
### Executando o servidor

Para iniciar o servidor da API:

```
(env) flask run --host 0.0.0.0 --port 5000
```

Em ambiente de desenvolvimento, utilize o parâmetro --reload para reiniciar automaticamente o servidor após alterações no código fonte:

```
(env) flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no Navegador

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para acessar a API em execução.

---
## Executando via Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução.

Vá até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute o seguinte comando para construir a imagem Docker **(certifique-se de ter permissões adequadas)**:

```
docker build -t quickcontact-rest-api .
```

Uma vez que a imagem esteja criada, para iniciar o container, execute o seguinte comando **(certifique-se de ter permissões adequadas)**:

```
docker run -p 5000:5000 quickcontact-rest-api
```

Após o container estar em execução, você pode acessar a API abrindo [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.

### Mais informações sobre Docker

Para mais detalhes e comandos adicionais, consulte a [documentação oficial do Docker](https://docs.docker.com/engine/reference/run/).
