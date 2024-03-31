from etl import etl

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
serviceMethod = "promediosSipsaParcial"
arg0 = None
fields = [
    'artiNombre',
    'deptNombre',
    'enmaFecha',
    'fuenId',
    'fuenNombre',
    'futiId',
    'grupNombre',
    'idArtiSemana',
    'maximoKg',
    'minimoKg',
    'muniId',
    'muniNombre',
    'promedioKg'
]
pathFile = str("./data/promediosSipsaParcial.json")
etl.controller(wsdl, serviceMethod, arg0, fields, pathFile)
