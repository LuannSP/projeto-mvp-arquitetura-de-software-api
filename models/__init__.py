import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from models.base import Base
from models.contact import Contact

db_path = "database/"
db_filename = "db_quickcontact.sqlite3"
db_url = f'sqlite:///{os.path.join(db_path, db_filename)}'

os.makedirs(db_path, exist_ok=True)

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
