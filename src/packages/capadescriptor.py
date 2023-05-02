from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey

from sqlalchemy.orm import declarative_base
from datetime import datetime
from .colorsprint.colorsprint import *
from .Credentials.db_psql import *

#from colorsprint.colorsprint import *
#from Credentials.database import *

db_psql = Psql()
log_col = bcolors()
#Parents for the ORM class
Base = declarative_base()


#-----------------/Class related to "CapaDescriptor" table in DB, connected with the ORM/--------------------------
class CapaDescriptor(Base):
    __tablename__ = 'CapaDescriptor'
    __table_args__ = {"schema" : "app"}

    codCapa = Column(String(100), nullable=False, primary_key=True) #Cambiar a cod    
    nombreCapaDescript = Column(String(150), nullable=False)
    descripcion = Column(String(300), nullable=False)
    ultimoAcceso = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    siguienteProceso = Column(String(10), nullable = False)
    frecuenciaDias = Column(Integer(), nullable = False)
    nombreTablaCapa = Column(String(100), nullable=False)

    def __init__(self, cod, nameDesc, desc, lastAcces, nextStep ,freq, layerTableName):
        self.nombreCapaDescript = nameDesc
        self.descripcion = desc
        self.siguienteProceso = nextStep
        self.codCapa = cod
        self.ultimoAcceso = lastAcces
        self.frecuenciaDias = freq
        self.nombreTablaCapa = layerTableName
        

    def __repr__(self):
        return f"({self.nombreCapaDescript} {self.descripcion} {self.codCapa} {self.ultimoAcceso} {self.frecuenciaDias} {self.nombreTablaCapa})"

#-----------------/Method to load the new value in DB/--------------------------
    def load_layer(self, session):
        try:
            session.add(self)
            print(log_col.ok + "Layer added correctly... commiting")
            session.commit()
            print(log_col.ok + "Layer loaded to database correctly.")
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

class CapaFuente(Base):
    __tablename__ = 'CapaFuente'
    __table_args__ = {"schema" : "app"}

    id = Column(Integer(), Sequence('id', start=1, increment=1), primary_key=True)
    codCapa = Column(String(100), ForeignKey("app.CapaDescriptor.codCapa"), nullable=False)
    descripcion = Column(String(100), nullable=False)
    urlDescarga = Column(String(350), nullable=False)
    prioridad = Column(Integer(), nullable = False)
    capaNombreWFS = Column(String(150))
    
    def __init__(self, codCapa, descripcion, url, prioridad, capaNombre = " "):
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


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

class CapaPreProceso(Base):
    __tablename__ = 'CapaPreProceso'
    __table_args__ = {"schema" : "app"}

    id = Column(Integer(), Sequence('id', start = 1, increment = 1), primary_key = True)
    codCapa = Column(String(100), ForeignKey("app.CapaDescriptor.codCapa"), nullable=False)
    algoritmo = Column(String(100), nullable = False)
    nombre_resultado = Column(String(30), nullable = False)

    def __init__(self, codCapa, algorithm, resulted_name):
        self.codCapa = codCapa
        self.algoritmo = algorithm
        self.nombre_resultado = resulted_name

    def load_layer_to_clean(self, session):
        try:
            session.add(self)
            print(log_col.ok + f"Clean Data Process for layer {self.codCapa} added correctly... commiting")
            session.commit()
            print(log_col.ok + "Clean Data Process loaded to database correctly.")
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



