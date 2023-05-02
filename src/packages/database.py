""" from sqlalchemy import create_engine """
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from packages.fileHandler import *
from packages.logs import *
from packages.capadescriptor import *
from packages.Credentials.db_psql import *


#Class with credentials for DB connect
db_psql = Psql()

#-----------------/Connecting with Database/--------------------------
try:
    engine = create_engine(db_psql.get_url_connect())
    logging.warning("----------------------------------------------------------------------------------------------")
    logging.warning("Conexión con Postgres establecida")
    print(log_col.ok + "Conexión con Postgres establecida" + log_col.reset)
except Exception as ex:
    logging.error(str(ex))
    print(log_col.fail + str(ex) + log_col.reset)

#-----------------/Needed for the ORM/--------------------------
Session = sessionmaker(bind = engine)
session = Session()


#-----------------/Helpers Method`s related to DB/--------------------------

#Sending layers to the database
def send_shp_to_db(shp_layer, table_name):
    try:
        new_shp_layer = reproject_crs_file(shp_layer)    
        new_shp_layer.to_postgis(table_name, engine, schema = None, if_exists = 'fail', index = False, index_label = None, chunksize = None, dtype = None)        
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        logging.error(str(ex))
    
#This method will send the SQL query to the db. It has to be called after a SQL sentence and need to be passed as second parameter. The firstone´ll be the engine needed for the conection with db
def send_query_to_db(engine, query):
    conn = engine.connect()
    try:
        conn.execute(query)
        conn.close()
        return True
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        return False

#brings all the layer´s cod to read
def get_all_layers_cods(session):
    cods =[]
    codes = session.query(CapaDescriptor.codCapa).all()
    for c in codes:
        cods.append(c[0])
    return cods

#Method that search the layer in the db and returns true if it is found and false if it´s not       
def check_if_existe_table_in_db(engine, layer_cod):
    query = f'SELECT * FROM public."{layer_cod}"'
    return send_query_to_db(engine, query)

def rename_to_correct_table_in_db(engine, layer_cod):
    old_name = layer_cod + "_new"    
    query = f'ALTER TABLE public."{old_name}" RENAME TO "{layer_cod}"'
    return send_query_to_db(engine, query)

def delete_old_table(engine, layer_cod):
    query = f'DROP TABLE public."{layer_cod}"'
    return send_query_to_db(engine, query)

#Method to change the url from the DataBase CapaFuente
def update_urls_in_db(session, Table, codCapa, newURL, i = 0):
    try:
        stmts = session.query(Table).filter(Table.codCapa == codCapa).all() 
        stmt = stmts[i]
        print(stmt)
        stmt.urlDescarga = newURL
        session.add(stmt)
        session.commit()
        print(log_col.ok + "Cambio realizado exitosamente."+ log_col.reset)
        print(stmt)
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        logging.error(str(ex))

#delet the entry that matches with the layerCod passed in the table passed (capsDescriptor o LayerSource)
def delete_entry(session, layerCod, Table):
    try:
        stmt = session.query(Table).filter(Table.codCapa == layerCod).first()     #Syntax from ORM SQLAlqhemy // read doc
        session.delete(stmt)
        session.commit()
        print(log_col.ok + "Entrada eliminada correctamente"+ log_col.reset) 
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset) 
        logging.error(str(ex)) 

#Search for the iqual codCapa and returns an array with the entrys that matches in the Table (can be CapaDescriptor/LayerSource)
#Returns and ARRAY cause the LayerSource can have two or more entrys with the same codCapa. Always treat it like an array
def get_layer_by_cod(session, layerCod, Table):
    try:        
        layer_reference = session.query(Table).filter(Table.codCapa == layerCod).all() #Must be done with this query because .get() works with the PK and LayerSource has an id as PK
        #layer_reference = session.get(Table, layerCod)                          #Syntax from ORM SQLAlqhemy // read doc
        print(log_col.ok + f"Capa con código {layerCod} encontrada en base de datos `CapaDescriptors`." + log_col.reset)
        return layer_reference
    except Exception as ex:
        print(log_col.fail + "La Capa requerida no exite en la base de datos o ha habido un error. Detalle ==> \n " + str(ex) + log_col.reset)
        logging.error( "La Capa requerida no exite en la base de datos o ha habido un error. Detalle ==> \n " + str(ex))
        
#Work´s with CapaDescriptor
def check_if_frequency_expired(session, layerCod):
    try:
        layer_array = get_layer_by_cod(session, layerCod, CapaDescriptor) #CapaDescriptor here is hardcoded cause it is where frequency and lastAccess are
        layer = layer_array[0]
        lastAccesCount = datetime.today().date() - layer.ultimoAcceso.date()
        lastAcces = int(lastAccesCount.days)
        if (lastAcces >= layer.frecuenciaDias):
            expired_days = lastAcces - layer.frecuenciaDias
            msj = f"La capa {layer.nombreCapaDescript} está desactualizada desde hace {lastAcces}. Debería actualizarse desde hace {expired_days}"
            print(log_col.fail + msj + log_col.reset)
            logging.warning(msj)
            return True
            #Aquí se llamaría a una función para que actualice la capa??
        else:
            print(log_col.ok + "Esta capa aún está actualizada." + log_col.reset)
            logging.warning(f"La capa {layerCod} aún está actualizada.")
            return False
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        logging.error(str(ex))

#Work´s with CapaDescriptor ==> Method to be called when a layer is updated. Thisone will updste the last acces date
def update_last_acces_layer_date(session, codCapa):
    stmt = session.query(CapaDescriptor).filter(CapaDescriptor.codCapa == codCapa).first() 
    print(stmt)
    today = datetime.today()
    stmt.ultimoAcceso = today.replace(microsecond=0)
    session.add(stmt)
    session.commit()
    print("Fecha de última actualización editada a: " , log_col.fail + str(stmt.ultimoAcceso) + log_col.reset)    

#Everytime we update a layer in the DB a index is made and we change the table_name but not the index_name, so this method ´ll update the name of the index, deleting the lastone and leaving space for the newone
def alter_index_created(engine, layer_cod, is_an_update):    
    try:
        layer_cod_lower = layer_cod.lower()
        if(is_an_update):
            query = f"ALTER INDEX idx_{layer_cod_lower}_new_geometry RENAME TO idx_{layer_cod_lower}" #If it´s true is because already existed one shape before and the rename´ll have a "_new"
        else:
            print(layer_cod_lower)
            query = f"ALTER INDEX idx_{layer_cod_lower}_geometry RENAME TO idx_{layer_cod_lower}"
            print(query)
        send_query_to_db(engine, query)
        print("NOMBRE DE INDEX CAMBIADO!!??¿?¿?¿¿%&%$&·%/!%¿?")    
    except Exception as ex:
        print(ex)
        

def bring_the_correct_cod(cod_in_lower_case):
    cods = get_all_layers_cods(session)
    for cod in cods:
        if(cod.lower() == cod_in_lower_case): return cod
    return False