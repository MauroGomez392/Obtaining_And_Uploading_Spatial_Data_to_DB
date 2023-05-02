#-----------------/File that set the logs file/--------------------------
import logging
from datetime import datetime
from packages.Credentials.db_psql import *
from packages.colorsprint.colorsprint import *

#Class with credentials for DB value shp folder path
db_psql = Psql()
#Parameters:
shp_folder = db_psql.shp_folder
#Class with with color for the print logs
log_col = bcolors()
#-----------------/Logs Method`s/--------------------------
#Function made to the save the logs inside the Log´s file:
def set_loggs():
    date_today = datetime.today().date()    
    name = shp_folder + "Logs/" + "Logs from " + str(date_today)
    name += ".txt"
    logging.basicConfig(filename=name, filemode='a', format='%(asctime)s - %(levelname)s -  %(message)s', datefmt='%H:%M:%S')

#Initializing
set_loggs()