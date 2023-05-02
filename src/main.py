from packages.colorsprint.colorsprint import *
from packages.database import *
from packages.capadescriptor import *
from packages.servicesfunc import *

#-----------------/Inits & Parameters/--------------------------
#Class with with color for the logs
log_col = bcolors()
#Parents for the ORM class
Base = declarative_base()
#Parameters:
shp_folder = db_psql.shp_folder
crs_used = 'epsg:5382' #our reference system picked to work through


#-----------------/Logic Business/--------------------------
def updater(session):
    layers_list = get_all_layers_cods(session) #puede cambiar a traerme sólo los códigos en vez de los objetos
    for l in layers_list:        
        print(log_col.fail +"Comenzando carga de <" + str(l) + "> capa"+ log_col.reset)
        if(l == "mides_INAU"): 
            print("ACÁAA--------------------------------")
        logging.warning("Comenzando carga de <" + str(l) + "> capa")
        cod = l        
        is_an_update = check_if_existe_table_in_db(engine, cod.lower())        
        #if (check_if_frequency_expired(session, cod)):
        layer_data = get_layer_by_cod(session, cod, CapaFuente)    
        if (len(layer_data) < 1):
            print(log_col.warning + f"La capa con código {cod} no tiene una fuente relacionada en la base de datos `Fuente Capa` para poder obtener la capa." + log_col.reset)            
            logging.error(f"La capa con código {cod} no tiene una fuente relacionada en la base de datos `Fuente Capa` para poder obtener la capa.")
        elif(len(layer_data) == 1):            
            msj = f"1  son las posibles fuentes cargadas para esta capa {cod}"
            print(msj)            
            layer = layer_data[0]
            decision_maker_for_shp_import(session, layer, is_an_update)
        elif(len(layer_data) > 1):
            layer_sorted_list = priority_handler(layer_data)
            msj = str(len(layer_sorted_list)) + f"   son las posibles fuentes cargadas para esta capa {cod}"
            print(msj)            
            flag_out = False
            i = 0
            while (i < len(layer_sorted_list) and flag_out == False):
                layer = layer_sorted_list[i]
                logging.warning(f"Probando carga de capa {cod} mediante fuente {layer.descripcion}")            
                load = decision_maker_for_shp_import(session, layer, is_an_update)
                if load == True: flag_out = True
                i += 1
        




updater(session) 
logging.error("Capas que no funcionaron con WFS")
print("Capas que no funcionaron con WFS")
for wfs in layers_with_corrupt_wfs:
    logging.error(wfs)
    print(wfs)
print("Capas que no funcionaron en absoluto! REVISAR FUENTES")
logging.error("Capas que no funcionaron en absoluto! REVISAR FUENTES")
for l in layers_did_not_work:
    logging.error(l)
    print(l)