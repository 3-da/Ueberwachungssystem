from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import random
import string

# Verbindung zur Datenbank erstellen
engine = create_engine('sqlite:///database.db')
Base = declarative_base()

def generate_rfid():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Tabelle admin
class Admin(Base):
    __tablename__ = 'admin'
    rfid = Column(String, primary_key=True, default=generate_rfid)
    password = Column(String)
    oncall = Column(Boolean)
    img = Column(String)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)

    # Beziehungen zu anderen Tabellen
    entries = relationship("Entrie", back_populates="admin")
    errors = relationship("Error", back_populates="admin")
    breakins = relationship("Breakin", back_populates="admin")

# Tabelle entrie
class Entrie(Base):
    __tablename__ = 'entrie'
    entrie_id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime)
    admin_rfid = Column(String, ForeignKey('admin.rfid'))

    # Beziehung zu admin
    admin = relationship("Admin", back_populates="entries")

# Tabelle breakin
class Breakin(Base):
    __tablename__ = 'breakin'
    breakin_id = Column(Integer, primary_key=True, autoincrement=True)
    movement = Column(String)
    admin_oncall = Column(Boolean)
    admin_email = Column(String, ForeignKey('admin.email'))

    # Beziehung zu admin
    admin = relationship("Admin", back_populates="breakins")

# Tabelle error
class Error(Base):
    __tablename__ = 'error'
    error_id = Column(Integer, primary_key=True, autoincrement=True)
    status_code = Column(Integer)
    datetime = Column(DateTime)
    oncall = Column(Boolean)
    admin_email = Column(String, ForeignKey('admin.email'))

    # Beziehung zu admin
    admin = relationship("Admin", back_populates="errors")


# Tabellen erstellen
Base.metadata.create_all(engine)

# Session erstellen
Session = sessionmaker(bind=engine)
session = Session()

print("Datenbank und Tabellen wurden erfolgreich mit SQLAlchemy erstellt.")