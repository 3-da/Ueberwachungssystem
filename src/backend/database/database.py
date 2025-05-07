import os
import random
import string

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Construct the absolute path for the database file
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'database.db')

# Verbindung zur Datenbank erstellen
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()


def generate_rfid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))


# Tabelle admin
class Admin(Base):
    __tablename__ = 'admin'
    rfid = Column(String, primary_key=True, default=generate_rfid)
    password = Column(String)
    name = Column(String)
    email = Column(String, unique=True)


# Tabelle breakin
class Bewegung(Base):
    __tablename__ = 'bewegung'
    breakin_id = Column(Integer, primary_key=True, autoincrement=True)
    bild_name = Column(String)
    date = Column(DateTime)


# Tabellen erstellen
Base.metadata.create_all(engine)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

print("Datenbank und Tabellen wurden erfolgreich mit SQLAlchemy erstellt.")
