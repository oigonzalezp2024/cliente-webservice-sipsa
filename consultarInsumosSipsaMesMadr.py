from etl import etl

wsdl = 'https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL'
serviceMethod = "consultarInsumosSipsaMesMadr"
arg0 = 4
fields = [
    'deptNombre',
    'fechaMesIni',
    'insumoNombre',
    'muniId',
    'muniNombre',
    'promedio',
    'tireId',
    'tireNombre'
]
pathFile = str("./data/consultarInsumosSipsaMesMadr.json")
etl.controller(wsdl, serviceMethod, arg0, fields, pathFile)
