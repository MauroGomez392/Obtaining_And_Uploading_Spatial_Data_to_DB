# mcda-carga-datos

Este es un proyecto que recolecta datos espaciales de diferentes fuentes, los estandariza con un sistema de referencia en común y los guara en una base de datos, dejándolos listos para ser utilizados en otro geoproceso.

mcda-carga-datos consume una base de datos mediante un ORM (SQLAlchemy) donde se guardan los datos de todas las capas (layers) que deben ser actualizadas y las fuentes de donde pueden consumirse las últimas versiones de cada capa (Geoservicio "WFS", links de "Descarga" o subida mediante archivos "Local"). 

Cada fuente tiene asociada en la base de datos una prioridad que equivale al orden con la que correrá el algoritmo intentando actualizar cada capa respetando dicho orden (WFS = 1 / Descarga = 2 / Local = 3). En caso de que el primero no funcione, intentará actualizar con el segundo y sino con el tercero.

El archivo que se debe correr es el main.py



Comenzando
Estas instrucciones te ayudarán a configurar y correr el proyecto en tu máquina local para propósitos de desarrollo y pruebas.



Prerrequisitos
Listado de los requisitos necesarios para correr el proyecto.

Listado:
- Python => versión recomendada = Python 3.11.1
- PIP
- PostgreSQL con extensión "postgis" para almacenar datos espaciales ==> versión recomendada de postgis = 3.3.1 
- Descargar Extensión Posgis para versión descargada de PostgreSQL



Instalación
Pasos a seguir para instalar y configurar el proyecto.

Pasos:
1. Clonar el repositorio
2.  Unix:    Crear entorno virtual: virtualenv -p python3 “nombre_entorno” // “venv” por lo gral.
    Windows: `python3 -m venv "nombre_entorno"`
2.  Unix:    Correr `source ./venv/bin/activate` para iniciar el servidor del entorno virtual.
            En caso de querer salir de su entorno virtual, corra el comando: "deactivate" en consola.
    Windows: `nombre_entorno\Scripts\activate.bat` 
3. Correr `pip install -r requirements.txt` en la raíz del proyecto.
4. Llenar campos con credenciales para conexión en archivo .env .
5. Cargar / llenar archivo "seedfileJson.py" con los datos de las Capas. Tomar como referencia las clases creadas en "capadescriptor.py" para el llenado de campos.
6. Mediante CLI, situarse en carpeta src/ y correr el siguiente comando:
    - en caso de tener versión de python 3 en adelante, correr:   python3 seedfile.py
    - en caso de versiones anteriores, correr: python seedfile.py
7. Chequear en consola mensajes. En caso de estar todo ok el proceso de instalación ha terminado. En caso opuesto revise los mensajes en consola, datos ingresados, credenciales y pasos seguidos.
8. Correr archio main.py con python. Esto ejecutará el proceso. Podibilidad de que este punto se corra automáticamente.

 
Implementación:

Actualmente el script se debe de correr manualmente (preveemos crear una automatización para que se corra 2 veces al año).
Para correrlo, debemos entrar a nuestro entorno virtual (pasos descriptos arriba), situarnos en la carpeta src/ y correr el main.py
    - en caso de tener versión de python 3 en adelante, correr:   python3 main.py
    - en caso de versiones anteriores, correr: python main.py

Logs guardados:
Cada vez que se corra el programa, se creará una archivo con extensión .txt que almacenará todos los mensajes de error que se hayan presentado mientras se corrió el script.
Este archivo se crea automáticamente y se guarda en la carpeta Logs, guardada en la Ruta que se haya definido en el archivo .env, misma ruta donde se cargan todas las capas que se deseen cargar mediante archivos "Local". El nombre del archivo se autogenera con fecha del log y guardará todos los logs que se genere en esa fecha. Es decir, si el script se corrió dos veces en el mismo día, el archivo no se sobreescribe, sino que guardará ambos logs. Cada mensaje guarda se muestra con la hora en la que se generó.

Carpeta para capas Locales:
Las capas que quieran ser cargadas mediante "Local" han de ser cargadas en la Ruta que se haya definido en el archivo .env (SHP_LOCAL_FOLDER). 
Es IMPORTANTE tener en cuenta que toda capa que se quiera cargar debe hacerse en formato comprimido .zip y dentro deberá ser un shape file (.shp) o un geopackage (.gpkg) siendo preferible el primero. También hay que tener en cuenta que así sea que la capa se haya cargado en la base de datos correctamente o no, el archivo en dicha Ruta será borrado, dejándole lugar a un nuevo archivo, ya sea para actualizar la capa o para cargar otro archivo que no de errores y poder hacerlo sin conflictos.


Agregar nueva capa a la base de datos:
En el caso de querer sumar una capa a la base de datos, la capa se deberá crear como una nueva instancia de la clase CapaDescriptor. 
Esta instancia se debe de crear en el archivo seedfile.py y se deberá llamar a la función "load_one_CapaDescriptor()" pasándole como parámetro la instancia de la clase con los datos de la capa. Posteriormente, se deberá de correr por consola ese archivo (indicaciones arriba).


Agregar nueva fuente de descarga para capa ya existente:
En el caso de querer sumar una o varias fuente/s de descarga una capa en la base de datos, la fuente se deberá cargar creando una nueva instancia de la clase CapaFuente. 
Esta instancia se debe de crear en el archivo seedfile.py (mismo archivo de carga para instancias de CapaDescriptor) y se deberá llamar a la función "load_one_FuenteCapa()" pasándole como parámetro la instancia de la clase con los datos de la fuente de la capa. Posteriormente, se deberá de correr por consola ese archivo (indicaciones arriba).


Futuras mejoras:
Estas son las ideas para mejorar en la próxima versión:
- Funcionalidad para eliminar archivos shape que se hayan cargado mediante otra prioridad?
- Función que, a la hora de correr el seedfile, revise qué CapaDescriptor y CapaFuente ya existen y de esa forma ignorarlos y sólo cargar las nuevas instancias del seedfileJson.



