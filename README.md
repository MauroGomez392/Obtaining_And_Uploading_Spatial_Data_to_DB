# Obtaining and Uploading Spatial Data to DB
This is a project that collects spatial data from different sources, standardizes it with a common reference system and stores it in a database, making it ready to be used in another geoprocess.

Obtaining_And_Uploading_Spatial_Data_to_DB consumes a database through an ORM (SQLAlchemy) where the data of all layers that need to be updated and the sources from which the latest versions of each layer can be consumed (Geoservice "WFS", "Download" links or uploading through "Local" files) are stored.

Each source has a priority associated with it in the database, which corresponds to the order in which the algorithm will try to update each layer respecting that order (WFS = 1 / Download = 2 / Local = 3). If the first one doesn't work, it will try to update with the second one and if not, with the third one.

The file that must be run is main.py.

Getting Started
These instructions will help you set up and run the project on your local machine for development and testing purposes.

Prerequisites
List of requirements needed to run the project:

Python => recommended version = Python 3.11.1
PIP
PostgreSQL with "postgis" extension to store spatial data ==> recommended version of postgis = 3.3.1
Download Posgis Extension for downloaded version of PostgreSQL
Installation
Steps to follow to install and set up the project:

1-  Clone the repository
2-  Unix: Create virtual environment: virtualenv -p python3 “env_name” // "venv" for general use. Windows: python3 -m venv "env_name"
3-  Unix: Run source ./venv/bin/activate to start the virtual environment server. 
    Windows: $ env_name\Scripts\activate.bat
    To exit your virtual environment, run the command: "$deactivate" in the console. 
4-  Run pip install -r requirements.txt in the project's root directory.
5-  Fill in fields with connection credentials in the .env file.
6-  Load/fill the seedfileJson.py file with the data of the layers. Use the classes created in capadescriptor.py as a reference for filling in the fields.
7-  Through CLI, navigate to the src/ folder and run the following command:
        *   If you have a version of Python 3 or later, run: python3 seedfile.py
        *   If you have earlier versions, run: python seedfile.py
8-  Check console messages. If everything is okay, the installation process is complete. Otherwise, review the messages in the console, entered data, credentials and       steps taken.
9-  Run main.py file with Python. This will execute the procces.
 
 
Implementation:

Currently, the script needs to be manually run (you can make the automation that runs every X time with bash).
To run it, we need to enter our virtual environment (steps described above), navigate to the src/ folder, and run main.py.
- If you have Python version 3 or later, run: python3 main.py
- If you have an earlier version, run: python main.py

Saved logs:
Every time the program is runned, a file with a .txt extension will be created that will store all error messages that occurred while the script was running.
This file is automatically created and saved in the Logs folder, stored in the path defined in the .env file, the same path where all layers to be loaded via "Local" files are loaded. The file name is auto-generated with the log date and will save all logs generated on that date. That is, if the script was run twice in the same day, the file is not overwritten but will save both logs. Each saved message shows the time it was generated.

Folder for Local layers:
Layers that want to be loaded via "Local" must be loaded in the path defined in the .env file (SHP_LOCAL_FOLDER).
It is IMPORTANT to note that any layer that is to be loaded must be in compressed .zip format and must contain either a shape file (.shp) or a geopackage (.gpkg), with the former being preferable. It should also be noted that whether the layer has been successfully loaded into the database or not, the file in that path will be deleted, making room for a new file, either to update the layer or to load another file without conflicts.

Adding a new layer to the database:
If you want to add a layer to the database, the layer must be created as a new instance of the CapaDescriptor class.
This instance must be created in the seedfile.py file and the "load_one_CapaDescriptor()" function must be called, passing the instance of the class with the layer data as a parameter. Subsequently, that file must be run through the console (instructions above).

Adding a new download source for an existing layer:
If you want to add one or more download sources for a layer in the database, the source must be loaded by creating a new instance of the CapaFuente class.
This instance must be created in the seedfile.py file (same file for loading CapaDescriptor instances) and the "load_one_FuenteCapa()" function must be called, passing the instance of the class with the layer source data as a parameter. Subsequently, that file must be run through the console (instructions above).

Future improvements:
These are the ideas for improving in the next version:

Functionality to delete shape files that were loaded using another priority?
A function that, when running the seedfile, checks which CapaDescriptor and CapaFuente instances already exist and thus ignores them and only loads new instances from the seedfileJson.



