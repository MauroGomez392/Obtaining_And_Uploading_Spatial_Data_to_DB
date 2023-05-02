from packages.capadescriptor import *
#Here we write the all data to populate the administrations tables from the DB.
#This are 3 arrays of jsons that ´ll be read for the seedfile.py and send it to DB
capasDescriptor = [
    {
    "layerCod" : "...",
    "layerName" : "...",
    "description" : "...",
    "nextProcess": "...",
    "updateFrequencyDays" : 180,
    "layerNameInDb" : "..."
    }
]
capasFuente = [
    {
    "layerCod" : "...",
    "description" : "...",
    "urlUpload" : "...",
    "priority" : 3,
    "layerNameIfWFS" : ""
    }
]
capasPreProceso = [
    {
    "layer" : "...",
    "algorithm" : "...",
    "resulted_name" : "..."
    }
]
