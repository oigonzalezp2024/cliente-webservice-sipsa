from etl import etl

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
serviceMethod = "promedioAbasSipsaMesMadr"
arg0 = None
fields = [
    "artiId",
    "artiNombre",
    "cantidadTon",
    "enviado",
    "fechaCreacion",
    "fechaMesIni",
    "fuenId",
    "fuenNombre",
    "futiId",
    "tmpAbasMesId"
]
pathFile = str("./data/promedioAbasSipsaMesMadr.json")
etl.controller(wsdl, serviceMethod, arg0, fields, pathFile)
