#-----------------/In this file we will load the first´s entrys of the Admin tables to the DB/--------------------------
from packages.database import *
from datetime import datetime
from packages.colorsprint.colorsprint import bcolors
from packages.capadescriptor import Base, CapaDescriptor, CapaFuente
from seedfileJson import capasDescriptor, capasFuente, capasPreProceso

#-----------------/Inits & Parameters/--------------------------
#Class with with color for the logs
log_col = bcolors()

#-----------------/Tables for the Admin Tasks/--------------------------
#Sólo correr cuando necesitamos crear nuvas tablas con clases ORM
try:
    Base.metadata.create_all(bind = engine)
    print("TABLAS CREADAS EN TEORÍA" )
except Exception as ex:    
    print(log_col.fail + str(ex) + log_col.reset)

#-----------------/Doing the First Entry´s in the DB/--------------------------
capas = []
sources = []
toCleans = []

for l in capasDescriptor:
    layer = CapaDescriptor(l["codCapa"], l["nombreCapaDescript"], l["descripcion"], datetime.today().date() , l["siguienteProceso"],l["frecuenciaDias"], l["nombreTablaCapa"])
    capas.append(layer)

for f in capasFuente:
    source = CapaFuente(f["codCapa"], f["descripcion"], f["urlDescarga"], f["prioridad"], f["capaNombreWFS"])
    sources.append(source)

for p in capasPreProceso:
    toClean = CapaPreProceso(p["layer"], p["algorithm"], p["resulted_name"])
    toCleans.append(toClean)

#-----------------/Loading data into CapaDescriptor and CapaFuente tables in DB/--------------------------
def load_layers(session):
    session.add_all(capas)
    session.commit()
def load_layers_sources(session):
    session.add_all(sources)
    session.commit()
def load_layers_pre_process(session):
    session.add_all(toCleans)
    session.commit()

def load_seed_entrys(session):
    try:
        load_layers(session)
        print(log_col.ok + "Precarga de CapaDescriptor realizada con éxito" + log_col.reset)
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset) 
   
    try:
        load_layers_sources(session)
        print(log_col.ok + "Precarga de CapaFuente realizada con éxito" + log_col.reset)
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)

    try:
        load_layers_pre_process(session)
        print(log_col.ok + "Precarga de CapaPreProceso realizada con éxito" + log_col.reset)
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
    
load_seed_entrys(session)

def load_one_CapaDescriptor(capaDescriptor):
    session.add(capaDescriptor)
    session.commit()

def load_one_FuenteCapa(capaFuente):
    session.add(capaFuente)
    session.commit()

def load_one_CapaPreProceso(capaPreProcess):
    session.add(capaPreProcess)
    session.commit()