from etl import etl

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
serviceMethod = "promediosSipsaCiudad"
arg0 = None
fields = [
    "ciudad",
    "codProducto",
    "enviado",
    "fechaCaptura",
    "fechaCreacion",
    "precioPromedio",
    "producto",
    "regId",
]
pathFile = str("./data/promediosSipsaCiudad.json")
etl.controller(wsdl, serviceMethod, arg0, fields, pathFile)
