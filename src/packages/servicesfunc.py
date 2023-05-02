import os
import geopandas as gpd
from packages.fileHandler import *
from requests import Request, get
from packages.database import *
import ssl

layers_with_corrupt_wfs = []
layers_did_not_work = []

#method that given a layercod, it´ll search if it is already in the list and if not it´ll put it
#the ended list will have all the layers that couldn´t be uploaded in the DB
def add_layers_with_error(layer_cod):
    if(len(layers_did_not_work) > 0):
        flag = True
        for layer in layers_did_not_work:
            if layer == layer_cod: flag = False
        if (flag): layers_did_not_work.append(layer_cod)
    else:
        layers_did_not_work.append(layer_cod)
#-----------------/Get Shape Files and sent them to DB/--------------------------
#Get Shape files from local storage.
def import_shapefile(file_path, table_name):
    print(log_col.warning + f"IMPORTING {table_name} SHAPE FILE FROM LOCAL FILE!!!" + log_col.warning)
    logging.warning(f"IMPORTING {table_name} SHAPE FILE FROM LOCAL FILE!!!")
    layer_is_ok = check_if_file_extension_is_ok(file_path)
    if (layer_is_ok):
        try:
            layer_df = gpd.read_file(file_path)
            print(layer_df.crs)
            send_shp_to_db(layer_df, table_name)
            os.remove(file_path) #remove the file from the path leaving space for the next shape file with the update
            return True
        except Exception as ex:
            print(log_col.fail + str(ex) + log_col.reset)
            logging.error(str(ex))
            return False
    else:
        print("El archivo de la capa no tiene un formato aceptado. Procure que el formato sea shp o gpkg")
           
#Get Shape files from URL, download the .zip file and call the import_shapefile
def import_fileurl(url, url_file, table_name):   
    print(log_col.warning + f"IMPORTING {table_name} SHAPE FILE FROM DOWNLOAD LINK!!!" + log_col.warning)
    logging.warning(f"IMPORTING {table_name} SHAPE FILE FROM DOWNLOAD LINK!!!")
    if hasattr(ssl,'_create_unverified_context'): #Here we´re disconecting the SSL certificate validation
        ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    respuesta = get(url, headers= headers, verify=False)
    with open(url_file, 'wb') as archivo:
        archivo.write(respuesta.content)
    if respuesta.status_code == 200:
        print("Archivo descargado exitosamente")
        logging.warning("Archivo descargado exitosamente")
        return import_shapefile(url_file, table_name)        
    else:
        print(f"Error al descargar el archivo. Error ==> {respuesta.status_code}")
        logging.error(f"Error al descargar el archivo. Error ==> {respuesta.status_code}")
        return False
        
#Get Shape files from Geoservice.
def import_wfs(wfs_url, table_name, layer_name):
    print(log_col.warning + f"IMPORTING {table_name} SHAPE FILE FROM WFS!!!" + log_col.warning)
    logging.warning(f"IMPORTING {table_name} SHAPE FILE FROM WFS!!!")
    try:    
        if hasattr(ssl,'_create_unverified_context'): #Here we´re disconecting the SSL certificate validation
            ssl._create_default_https_context = ssl._create_unverified_context
        # Especifique los parámetros para obtener los datos
        params = dict(service = 'WFS', version = "1.1.0", request = 'GetFeature', typeName = layer_name, outputFormat = 'json', startIndex = 0)
        wfs_request_url = Request('GET',wfs_url, params=params).prepare().url
        print(wfs_request_url)    
        shp_data = gpd.read_file(wfs_request_url)
        send_shp_to_db(shp_data, table_name)
        return True
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        logging.warning(str(ex))
        return False

#-----------------/Import´s METHODS + logs/--------------------------
def import_by_Local(session, codLayer, urlFile, is_update):
    try:   
        change_table = is_update
        if(change_table):
            cod_with_alias = codLayer + "_new"            
            layer_imported = import_shapefile(urlFile, cod_with_alias)
        else:
            layer_imported = import_shapefile(urlFile, codLayer)            
        if layer_imported == True:
            print(log_col.ok + "-----------------------------------------------------------------------")
            print(log_col.ok + F"| Capa {codLayer} cargada en la base de datos mediante archivo local |")
            print(log_col.ok + "-----------------------------------------------------------------------" + log_col.reset)
            logging.warning( F"| Capa {codLayer} cargada en la base de datos mediante archivo local |")            
            logging.warning( "-----------------------------------------------------------------------")            
            true_cod = bring_the_correct_cod(codLayer)
            if(true_cod != False): update_last_acces_layer_date(session, true_cod)
            if(change_table):
                delete_old_table(engine, codLayer)
                rename_to_correct_table_in_db(engine, codLayer)
            alter_index_created(engine, codLayer, change_table)
                #alter_index_created(engine, codLayer)
        else:
            print(log_col.fail + "No se ha podido cargar la capa mediante archivo Local. Chequee que el archivo con extensión .zip se encuentre en la carpeta de destino." + log_col.reset)
            logging.error("No se ha podido cargar la capa mediante archivo Local. Chequee que el archivo con extensión .zip se encuentre en la carpeta de destino.")
            os.remove(str(urlFile))
            add_layers_with_error(codLayer)
        return layer_imported
    except Exception as ex:
        print(log_col.fail + str(ex) + "!!!" +log_col.reset)
        logging.error(str(ex))
        add_layers_with_error(codLayer)
        return False

def import_by_Download(session, codLayer, urlDownload, is_update):
    already_in_folder = False
    try:
        already_in_folder = False
        local_file_path = str(shp_folder)        
        if (urlDownload.endswith(".rar")):
            local_file_path += str(codLayer) + ".rar"         
            print(log_col.warning + f"La URL del link de descarga de la capa {codLayer} es con extensión .rar y no está soportada")   
            logging.error(f"La URL del link de descarga de la capa {codLayer} es con extensión .rar y no está soportada")   
            return False
        else:
            already_in_folder = check_file_in_folder(codLayer, ".zip") #Here we´re checking if the shp file is already in the folder regarding to the Local try. 
            if already_in_folder:
                local_file_path += str(codLayer) + "_downloaded.zip"
            else:
                local_file_path += str(codLayer) + ".zip"
                print(log_col.reset + f"El archivo con extensión .zip se descargará en la carpeta con ruta //{local_file_path} y se importará mediante archivo local.")                           
            change_table = is_update
            if(change_table):
                cod_with_alias = codLayer + "_new"            
                response = import_fileurl(urlDownload, local_file_path, cod_with_alias) #Returns bool
            else:
                response = import_fileurl(urlDownload, local_file_path, codLayer) #Returns bool
            if response == True:
                print(log_col.ok + "--------------------------------------------------------------------------")
                print(log_col.ok + f"| Capa {codLayer} cargada en la base de datos mediante link de Descarga |" + log_col.reset)
                print(log_col.ok + "--------------------------------------------------------------------------" + log_col.reset)
                logging.warning(f"| Capa {codLayer} cargada en la base de datos mediante link de Descarga |")
                logging.warning("--------------------------------------------------------------------------")
                true_cod = bring_the_correct_cod(codLayer)
                if(true_cod != False): update_last_acces_layer_date(session, true_cod)
                if(change_table):#Delete table in DB
                    delete_old_table(engine, codLayer)
                    rename_to_correct_table_in_db(engine, codLayer)
                alter_index_created(engine, codLayer, change_table)       
                    #alter_index_created(engine, codLayer)         
            else:            
                print(log_col.fail + "No se ha podido cargar la capa mediante link de Descarga" + log_col.reset)
                logging.error("No se ha podido cargar la capa mediante link de Descarga")
                os.remove(str(local_file_path))
            return response
    except Exception as ex:
        print(log_col.fail + str(ex) + "!!!" +log_col.reset)
        logging.error(str(ex))
        if already_in_folder:
            os.remove(str(local_file_path))
        return False

def import_by_wfs(session, codLayer, wfs_url, wfs_layer_name, is_update):
    try:        
        change_table = is_update
        print(change_table)
        if(change_table):
            cod_with_alias = codLayer + "_new"
            layer_imported = import_wfs(wfs_url, cod_with_alias, wfs_layer_name)
        else:
            layer_imported = import_wfs(wfs_url, codLayer, wfs_layer_name)          
        if layer_imported == True:
            print(log_col.ok + "---------------------------------------------------------------------------------")
            print(log_col.ok + F"| Capa {codLayer} cargada en la base de datos mediante archivo Geoservicio WFS |")
            print(log_col.ok + "---------------------------------------------------------------------------------" + log_col.reset)
            logging.warning(F"| Capa {codLayer} cargada en la base de datos mediante archivo Geoservicio WFS |")
            logging.warning("---------------------------------------------------------------------------------")
            true_cod = bring_the_correct_cod(codLayer)
            if(true_cod != False): update_last_acces_layer_date(session, true_cod)
            if(change_table):
                delete_old_table(engine, codLayer)
                print("borrada la tabla vieja")
                rename_to_correct_table_in_db(engine, codLayer)
                print("actualizada la tabla nueva ")
            alter_index_created(engine, codLayer, change_table)
                #alter_index_created(engine, codLayer)
        else:
            print(log_col.fail + "No se ha podido cargar la capa mediante conexión con Geoservicio WFS. Chequee que la URL del geoservicio es la correcta." + log_col.reset)
            logging.error("No se ha podido cargar la capa mediante conexión con Geoservicio WFS. Chequee que la URL del geoservicio es la correcta.")
            layers_with_corrupt_wfs.append(codLayer)
        return layer_imported
    except Exception as ex:
        print(log_col.fail + str(ex) + "!!!" +log_col.reset)
        logging.critical(str(ex))
        layers_with_corrupt_wfs.append(codLayer)
        return False

def priority_handler(layerList):
    priority_indented = sorted(layerList, key = lambda x: x.prioridad)
    return priority_indented

#this method is the one who decide what other method ´ll call depending on the source of the layer
def decision_maker_for_shp_import(session, capa_fuente_layer, is_update):
    response = False
    cod_lower_case = capa_fuente_layer.codCapa.lower()
    if (capa_fuente_layer.descripcion == "Local"):        
        response = import_by_Local(session, cod_lower_case, capa_fuente_layer.urlDescarga, is_update)
    elif (capa_fuente_layer.descripcion == "Descarga"):
        response = import_by_Download(session, cod_lower_case, capa_fuente_layer.urlDescarga, is_update)     
    elif (capa_fuente_layer.descripcion == "WFS"):
        response = import_by_wfs(session, cod_lower_case, capa_fuente_layer.urlDescarga, capa_fuente_layer.capaNombreWFS, is_update)
    else:
        print(f"Error al cargar capa  {cod_lower_case}")
        logging.error(f"Error al cargar capa  {cod_lower_case}")
        return False        
    return response

def layer_type_handler(shape_file_path, table_name):
    try:
        shp_df = gpd.read_file(shape_file_path)
        print(shp_df.crs)
        send_shp_to_db(shp_df, table_name)
        os.remove(shape_file_path) #remove the file from the path leaving space for the next shape file with the update
        return True
    except Exception as ex:
        print(log_col.fail + str(ex) + log_col.reset)
        logging.error(str(ex))
        return False


