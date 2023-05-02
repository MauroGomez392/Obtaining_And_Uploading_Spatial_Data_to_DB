from sqlalchemy import create_engine,Table, Column, MetaData, Integer, Computed, String, DateTime, Text, Sequence, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, mapper, relationship
from datetime import datetime
from .colorsprint.colorsprint import *
from .Credentials.db_psql import *


db_psql = Psql()
log_col = bcolors()
#Parents for the ORM class
Base = declarative_base()

class CapaFuente(Base):
    __tablename__ = 'CapaFuente'

    id = Column(Integer(), Sequence('id', start=1, increment=1), primary_key=True)
    codCapa = Column(String(100),ForeignKey("CapaDescriptor.codCapa"), nullable=False)
    descripcion = Column(String(100), nullable=False)
    urlDescarga = Column(String(350), nullable=False)
    prioridad = Column(Integer(), nullable = False)
    capaNombreWFS = Column(String(150))
    
    def __init__(self, prioridad, url, descripcion, codCapa, capaNombre = " "):
        self.prioridad = prioridad
        self.urlDescarga = url
        self.descripcion = descripcion
        self.codCapa = codCapa
        self.capaNombreWFS = capaNombre
                

    def __repr__(self):
        return f"({self.id} {self.prioridad} {self.urlDescarga} {self.descripcion} || Código de capa => {self.codCapa})"
#-----------------/Method to load the new value in DB/--------------------------
    def load_source(self, session):
        try:
            session.add(self)
            print(log_col.ok + f"Source for layer {self.codCapa} added correctly... commiting")
            session.commit()
            print(log_col.ok + "Source loaded to database correctly.")
        except Exception as ex:
            msjError = log_col.fail + str(ex)            
            print(msjError + log_col.reset)

    def delete_entry(self, session):
        try:
            layer_to_delete = session.query.filter_by(codCapa=self.codCapa).first()
            session.delete(layer_to_delete)
            session.commit()
            print(log_col.ok + "Layer deleted correctly from the table!" + log_col.reset)
        except Exception as ex:
            print(log_col.fail + str(ex) + log_col.reset)

""" #Sólo correr cuando necesitamos crear nuvas tablas con clases ORM

try:
    engine = create_engine(db_psql.get_url_connect())
    print(log_col.ok + "Conexión con Postgres establecida" + log_col.reset)
except Exception as ex:
    print(log_col.fail + str(ex) + log_col.reset)

try:
    Base.metadata.create_all(bind = engine)
    print(log_col.ok + "TABLAS CREADAS EN TEORÍA" + log_col.reset)
except Exception as ex:
    print(log_col.fail + str(ex) + log_col.reset)
 """