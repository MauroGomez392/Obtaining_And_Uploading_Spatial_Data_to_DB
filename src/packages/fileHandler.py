#-----------------/Here´re all the methods that have contact with the shape files/--------------------------
import os
from packages.Credentials.db_psql import Psql
from packages.logs import *
from geopandas import *
import zipfile

#Class with credentials for DB connect
db_psql = Psql()
shp_folder = db_psql.shp_folder
crs_used = 'epsg:5382' #our reference system picked to work through

#-----------------/Helpers Method`s/--------------------------
#Check if the file exists in the shp_folder and returns bool
def check_file_in_folder(file_name, extension):
    return os.path.exists(shp_folder + file_name + str(extension))

#function to check and change the CRS of the file
def reproject_crs_file(readed_file):
    current_crs = readed_file.crs
    if readed_file.crs != crs_used :
        msj = "El sisetema de referencia de la capa es " + str(current_crs) + " y necesita ser cambiado." 
        print(log_col.warning + str(msj))
        logging.warning(str(msj))
        msj = "Cambiando a " + crs_used + " ..."
        print(log_col.warning + str(msj) + log_col.reset)
        try:
            new_crs_file = readed_file.to_crs({"init": crs_used})
            print(log_col.ok + "Sistema de referencia cambiado con éxito." + log_col.ok)
            logging.warning("Sistema de referencia cambiado con éxito.")
            return new_crs_file
        except Exception as ex:
            print(log_col.fail + str(ex) + log_col.fail)
            logging.error(str(ex))
    else:
        msj = "El sistema de referencia de la actual capa corresponde con ", crs_used
        print(log_col.reset + str(msj) + log_col.reset)   
        return readed_file     

#if it is geojson ´ll return True, if it is shape ´ll return False, and if it is other ´ll return NONE
def check_if_file_extension_is_ok(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if (file_name.endswith('.shp') or file_name.endswith('.gpkg')):
                return True            
        return False






