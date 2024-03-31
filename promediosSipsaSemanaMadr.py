from etl import etl

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
serviceMethod = "promediosSipsaSemanaMadr"
arg0 = None
fields = [
    'artiId',
    'artiNombre',
    'enviado',
    'fechaCreacion',
    'fechaIni',
    'fuenId',
    'fuenNombre',
    'futiId',
    'maximoKg',
    'minimoKg',
    'promedioKg',
    'tmpMayoSemId'
]
pathFile = str("./data/promediosSipsaSemanaMadr.json")
etl.controller(wsdl, serviceMethod, arg0, fields, pathFile)
