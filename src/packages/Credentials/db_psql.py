import os
from dotenv import load_dotenv

load_dotenv()
#-----------------/Class with the ENV credentials/--------------------------
class Psql:
    def __init__(self):
        self.passW = os.getenv('DB_SECRET_KEY')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.shp_folder = os.getenv('SHP_LOCAL_FOLDER')
        self.i = 0

#-----------------/Builds the URL for the connect/--------------------------
    def get_url_connect(self):
        #"postgresql://postgres:" + self.passW + "@localhost:5432/PruebaAsentamiento"
        db_connection = "postgresql://" + self.db_user + ":" + self.passW + "@" + self.db_host + ":" + self.db_port + "/" + self.db_name 
        return db_connection
