from packages.capadescriptor import *

capasDescriptor = [
    {
    "codCapa" : "inteMont_Cents",
    "nombreCapaDescript" : "Centralidades",
    "descripcion" : "Fuente: IMM",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Centralidades"
    },
    {
    "codCapa" : "inteMont_BienPatrs",
    "nombreCapaDescript" : "Bienes patrimoniales",
    "descripcion" : "Fuente: IMM",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Control de vertidos"
    },
    {
    "codCapa" : "mvot_InstApros",
    "nombreCapaDescript" : "Otras intervenciones de OT",
    "descripcion" : "Fuente: MVOT",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "INSTRUMENTOS"
    },
    {
    "codCapa" : "ma_ContVerts",
    "nombreCapaDescript" : "Residuos y vertederos",
    "descripcion" : "Fuente: Observatorio Ambiental Nacional (OAN) - MA",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Control de vertidos"
    },
    {
    "codCapa" : "ma_SDFNO",
    "nombreCapaDescript" : "Residuos y vertederos",
    "descripcion" : "Fuente: Observatorio Ambiental Nacional (OAN) - MA",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Sitios de disposición final (no operativos)"
    },
    {
    "codCapa" : "ma_SDFO",
    "nombreCapaDescript" : "Residuos y vertederos",
    "descripcion" : "Fuente: Observatorio Ambiental Nacional (OAN) - MA",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Sitios de disposición final (operativos)"
    },
    {
    "codCapa" : "sinae_RiesInces",
    "nombreCapaDescript" : "Riesgo de incendios",
    "descripcion" : "Fuente: SINAE a través de Datos Abiertos. Incendios de campo, Bosque nativo, Bosque plantado, Interfaz urbana",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Área afectada por los incendios forestales Plantaciones forestales"
    },
    {
    "codCapa" : "ma_app",
    "nombreCapaDescript" : "Áreas potenciales de protección",
    "descripcion" : "Fuente: DINARA - MGAP / Observatorio Ambiental Nacional (OAN) - MA",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Áreas potenciales protegidas (DINARA)"
    },
    {
    "codCapa" : "ma_anp",
    "nombreCapaDescript" : "Áreas protegidas",
    "descripcion" : "Fuente: Observatorio Ambiental Nacional (OAN) - MA",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Áreas naturales protegidas"
    },
    {
    "codCapa" : "ma_RiesInun",
    "nombreCapaDescript" : "Curvas de inundación",
    "descripcion" : "Fuente: DINAGUA - MA",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Riesgo de inundación"
    },
    {
    "codCapa" : "dgc_PadrAi",
    "nombreCapaDescript" : "Titularidad de los predios",
    "descripcion" : "",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "padrones_ai_total-v2"
    },
    {
    "codCapa" : "mvot_CateSuel",
    "nombreCapaDescript" : "Afectación por normativa urbanística / Parcelas rurales",
    "descripcion" : "Predios rurales ajustados y no ajustados, Categorización del suelo: Rural, Rural Natural, Rural Productivo, Suburbana, Urbano, Urbano Consolidado, Urbano no consolidado",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "Categorización del suelo"
    },
    {
    "codCapa" : "anep_CentEducs",
    "nombreCapaDescript" : "Centros educativos",
    "descripcion" : "Centros ANEP: CFE - Formación en educación, DGEIP - Escuelas y Jardines, DGES - Liceos, DGETP - Escuelas técnicas",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Centros_ANEP_22"
    },
    {
    "codCapa" : "asse_UnidAsiss",
    "nombreCapaDescript" : "Unidades Asistenciales",
    "descripcion" : "Primer Nivel, Segundo Nivel, Tercer Nivel. Fuente: ASSE",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 180,
    "nombreTablaCapa" : "unidadesTodas"
    },
    {
    "codCapa" : "mides_CentApoy",
    "nombreCapaDescript" : "Centros de apoyo MIDES",
    "descripcion" : "Fuente: MIDES",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "inteMont_ParaUrbas",
    "nombreCapaDescript" : "Paradas de ómnibus",
    "descripcion" : "Paradas urbanas / Fuente: MTOP",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Paradas urbanas"
    },
    {
    "codCapa" : "mtop_ParaSubus",
    "nombreCapaDescript" : "Paradas de ómnibus",
    "descripcion" : "Paradas suburbanas / Fuente: MTOP",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Paradas suburbanas"
    },
    {
    "codCapa" : "ide_AreaPobls",
    "nombreCapaDescript" : "Adecuación de la ocupación territorial / Áreas pobladas",
    "descripcion" : "Áreas pobladas",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Áreas pobladas"
    },
    {
    "codCapa" : "inteMont_Manzs",
    "nombreCapaDescript" : "Trama urbana/ Manzanas",
    "descripcion" : "Fuente: IMM",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Manzanas"
    },
    {
    "codCapa" : "ide_EjeCalls_topo",
    "nombreCapaDescript" : "Esta capa fue el resultado de una correción topológica para conectar nodos y permitir geoprocesos",
    "descripcion" : "Fuente: IDE",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Eje de Calle"
    },
    {
    "codCapa" : "ute_TensMedi",
    "nombreCapaDescript" : "Líneas de tensión media de UTE",
    "descripcion" : "Fuente: UTE",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Líneas de tensión media de UTE"
    },
    {
    "codCapa" : "ute_TensAlta",
    "nombreCapaDescript" : "Líneas de tensión alta de UTE",
    "descripcion" : "Fuente: UTE",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "Líneas de tensión alta de UTE"
    },
    {
    "codCapa" : "mides_Coops",
    "nombreCapaDescript" : "Cooperativas",
    "descripcion" : "Fuente: MIDES",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "igm_LimiDepas",
    "nombreCapaDescript" : "Límites departamentales",
    "descripcion" : "Fuente: IGM",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "ma_LineCost",
    "nombreCapaDescript" : "Línea de costa Cuantil 80%",
    "descripcion" : "Fuente: MA - OA",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "inteMont_SaneColes",
    "nombreCapaDescript" : "Colectores de saneamiento de Montevideo",
    "descripcion" : "Fuente: IMM",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "ose_SaneColes",
    "nombreCapaDescript" : "Colectores de saneamiento de Uruguay, excepto Montevideo",
    "descripcion" : "Fuente: OSE",
    "siguienteProceso": "Lmpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "ose_DistTubes",
    "nombreCapaDescript" : "Tuberías de distribución de agua para Uruguay",
    "descripcion" : "Fuente: OSE",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "ine_ZonaPobl",
    "nombreCapaDescript" : "Población por zona - Censo 2011",
    "descripcion" : "Fuente: INE",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "asse_Ambus",
    "nombreCapaDescript" : "Bases SAME y Transporte de Ambulancias",
    "descripcion" : "Fuente: ASSE",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "ide_EjCa032023",
    "nombreCapaDescript" : "Eje de Calles actualizadas a marzo del 2023, contiene la caminería nacional",
    "descripcion" : "Fuente: IDE",
    "siguienteProceso": "Limpieza",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "mvot_EspaLibrs2018",
    "nombreCapaDescript" : "Espacios libres en 2018 por MVOT",
    "descripcion" : "Fuente: MVOT",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "mvot_ProyPmb",
    "nombreCapaDescript" : "Programa de Mejoramiento de Barrios",
    "descripcion" : "Fuente: MVOT",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "mvot_ConjHabis",
    "nombreCapaDescript" : "Conjuntos Habitacionales (BHU, Autoconstrucción, Ley Promoción de Inversores, MEVIR, MVOT e Intendencias)",
    "descripcion" : "Fuente: MVOT",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    },
    {
    "codCapa" : "mides_INAU",
    "nombreCapaDescript" : "Instituto del Niño y Adolescente del Uruguay",
    "descripcion" : "Fuente: MIDES",
    "siguienteProceso": "Geoproceso",
    "frecuenciaDias" : 90,
    "nombreTablaCapa" : "varias"
    }
]
capasFuente = [
    {
    "codCapa" : "inteMont_Cents",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/inteMont_Cents.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_Cents",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://intgis.montevideo.gub.uy/sit/php/common/datos/generar_zip2.php?nom_shp=/inetpub/wwwroot/sit/mapserv/data/centralidades&tipo=shp",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_BienPatrs",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/inteMont_BienPatrs.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_BienPatrs",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://intgis.montevideo.gub.uy/sit/php/common/datos/generar_zip2.php?nom_tab=v_mdg_parcelas&tipo=gis",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_InstApros",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mvot_InstApros.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_InstApros",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://sit.mvot.gub.uy/shp/INSTRUMENTOS.zip",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_ContVerts",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=u19600217:c005&outputFormat=SHAPE-ZIP",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_ContVerts",
    "descripcion" : "WFS",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/wms?layers=u19600217:c719",
    "prioridad" : 1,
    "capaNombreWFS" : "c005"
    },
    {
    "codCapa" : "ma_ContVerts",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_ContVerts.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_SDFNO",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=u19600217:c733&outputFormat=SHAPE-ZIP",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_SDFNO",
    "descripcion" : "WFS",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/wms?layers=u19600217:c719",
    "prioridad" : 1,
    "capaNombreWFS" : "c733"
    },
    {
    "codCapa" : "ma_SDFNO",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_SDFNO.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_SDFO",
    "descripcion" : "WFS",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/wms?layers=u19600217:c719",
    "prioridad" : 1,
    "capaNombreWFS" : "c732"
    },
    {
    "codCapa" : "ma_SDFO",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=u19600217:c732&outputFormat=SHAPE-ZIP",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_SDFO",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_SDFO.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "sinae_RiesInces",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://catalogodatos.gub.uy/dataset/9650fdcf-b63c-44fb-90de-323c752537c7/resource/277e01cd-d81b-4ee4-b279-76489d705f6e/download/incendios_forestales_mira.zip",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "sinae_RiesInces",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/sinae_RiesInces.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_app",
    "descripcion" : "WFS",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/wms?layers=u19600217:c292",
    "prioridad" : 1,
    "capaNombreWFS" : "c292"
    },
    {
    "codCapa" : "ma_app",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=u19600217:c292&outputFormat=SHAPE-ZIP",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_app",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_app.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_anp",
    "descripcion" : "WFS",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/wms?layers=u19600217:c719",
    "prioridad" : 1,
    "capaNombreWFS" : "c716"
    },
    {
    "codCapa" : "ma_anp",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/geoserver/u19600217/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=u19600217:c397&outputFormat=SHAPE-ZIP",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_anp",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_anp.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "dgc_PadrAi",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/dgc_PadrAi.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_CateSuel",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mvot_CateSuel.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "anep_CentEducs",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/anep_CentEducs.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "anep_CentEducs",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://sig.anep.edu.uy/SIGANEP/FORMATOS/CENTROS_ANEP.rar",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "asse_UnidAsiss",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/asse_UnidAsiss.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "asse_UnidAsiss",
    "descripcion" : "Descarga",
    "urlDescarga" : "http://gis.asse.uy/gisasse/sigi/descargas/geojson/unidades.zip",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ide_AreaPobls",
    "descripcion" : "WFS",
    "urlDescarga" : "https://mapas.ide.uy/geoserver-vectorial/ideuy/wfs",
    "prioridad" : 1,
    "capaNombreWFS" : "ideuy:areas_urbanizadas_2"
    },
    {
    "codCapa" : "ide_AreaPobls",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ide_AreaPobls.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ide_EjeCalls_topo",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ide_EjeCalls_topo.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_Manzs",
    "descripcion" : "WFS",
    "urlDescarga" : "http://geoserver.montevideo.gub.uy/geoserver/ows",
    "prioridad" : 1,
    "capaNombreWFS" : "mdg_manzanas"
    },
    {
    "codCapa" : "inteMont_Manzs",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/inteMont_Manzs.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_ParaUrbas",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/inteMont_ParaUrbas.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_ParaUrbas",
    "descripcion" : "WFS",
    "urlDescarga" : "http://geoserver.montevideo.gub.uy/geoserver/ows",
    "prioridad" : 1,
    "capaNombreWFS" : "imm:v_uptu_paradas"
    },
    {
    "codCapa" : "mtop_ParaSubus",
    "descripcion" : "WFS",
    "urlDescarga" : "https://geoservicios.mtop.gub.uy/geoserver/inf_tte_pasajeros/v_paradas_suburbanos/ows?service=WFS&request=GetFeature&typeName=v_paradas_suburbanos",
    "prioridad" : 1,
    "capaNombreWFS" : "inf_tte_pasajeros:v_paradas_suburbanos"
    },
    {
    "codCapa" : "mtop_ParaSubus",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mtop_ParaSubus.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_LineCost",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://www.ambiente.gub.uy/oan/wp-content/uploads/2020/12/Costa_Q80.zip",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ma_LineCost",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ma_LineCost.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ute_TensMedi",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ute_TensMedi.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ute_TensAlta",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ute_TensAlta.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mides_Coops",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mides_Coops.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "igm_LimiDepas",
    "descripcion" : "Geoservicio",
    "urlDescarga" : "https://mapas.ide.uy/geoserver-vectorial/ideuy/wfs",
    "prioridad" : 1,
    "capaNombreWFS" : "ideuy:limites_departamentales_igm_20220211"
    },
    {
    "codCapa" : "igm_LimiDepas",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://catalogodatos.gub.uy/dataset/9bfa6e97-f40f-437e-aa13-a3406c50f762/resource/8bbbbc94-7d1c-47e2-abcf-6353ec8b5c48/download/limitesdepartamentales_shp.zip",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "igm_LimiDepas",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/igm_LimiDepas.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "inteMont_SaneColes",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/inteMont_SaneColes.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ose_SaneColes",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ose_SaneColes.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ose_DistTubes",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ose_DistTubes.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ine_ZonaPobl",
    "descripcion" : "Geoservicio",
    "urlDescarga" : "https://mapas.ide.uy/geoserver-vectorial/INE_NO_SEGURO_CLON_NS/wfs",
    "prioridad" : 1,
    "capaNombreWFS" : "INE_NO_SEGURO_CLON_NS:zona_tot"
    },
    {
    "codCapa" : "ine_ZonaPobl",
    "descripcion" : "Descarga",
    "urlDescarga" : "https://mapas.ide.uy/geoserver-vectorial/INE_NO_SEGURO_CLON_NS/wfs?service=WFS&request=GetFeature&version=1.0.0&outputFormat=shape-zip&typeName=zona_tot",
    "prioridad" : 2,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ine_ZonaPobl",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ine_ZonaPobl.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mides_CentApoy",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mides_CentApoy.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mides_INAU",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mides_INAU.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_EspaLibrs2018",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mvot_EspaLibrs2018.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "ide_EjCa032023",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/ide_EjCa032023.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_ProyPmb",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mvot_ProyPmb.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    },
    {
    "codCapa" : "mvot_ConjHabis",
    "descripcion" : "Local",
    "urlDescarga" : "/Users/maurogomez/Desktop/Mauro_DINOT/Develop/Capas/mvot_ConjHabis.zip",
    "prioridad" : 3,
    "capaNombreWFS" : ""
    }
]
capasPreProceso = [
    {
    "layer" : "ma_anp",
    "algorithm" : "clean_ma_anp",
    "resulted_name" : "ma_anp"
    },
    {
    "layer" : "mvot_CateSuel",
    "algorithm" : "cateSuel_clean",
    "resulted_name" : "mvot_CateSuel"
    },
    {
    "layer" : "mvot_InstApros",
    "algorithm" : "clean_mvot_instapros",
    "resulted_name" : "mvot_InstApros"
    },
    {
    "layer" : "mtop_ParaSubus",
    "algorithm" : "clean_stops",
    "resulted_name" : "ParaMont"
    },
    {
    "layer" : "inteMont_ParaUrbas",
    "algorithm" : "clean_stops",
    "resulted_name" : "ParaMont"
    },
    {
    "layer" : "ide_EjCa032023",
    "algorithm" : "clean_ide_ejca",
    "resulted_name" : "ide_EjCa032023"
    },
    {
    "layer" : "ma_SDFO",
    "algorithm" : "clean_SitiDisp",
    "resulted_name" : "sitiDisp"
    },
    {
    "layer" : "ma_SDFNO",
    "algorithm" : "clean_SitiDisp",
    "resulted_name" : "sitiDisp"
    },
    {
    "layer" : "ute_TensMedi",
    "algorithm" : "clean_LineTens",
    "resulted_name" : "ute_LineTens"
    },
    {
    "layer" : "ute_TensAlta",
    "algorithm" : "clean_LineTens",
    "resulted_name" : "ute_LineTens"
    },
    {
    "layer" : "inteMont_SaneColes",
    "algorithm" : "clean_SaneColes",
    "resulted_name" : "saneColes"
    },
    {
    "layer" : "ose_SaneColes",
    "algorithm" : "clean_SaneColes",
    "resulted_name" : "saneColes"
    }
]
