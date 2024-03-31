import json
import zeep

def extractData(wsdl:str, serviceMethod:str, arg0:int)->object:
    client = zeep.Client(wsdl=wsdl)
    getService = {}
    if(serviceMethod == "promedioAbasSipsaMesMadr"):
        getService = client.service.promedioAbasSipsaMesMadr()
    elif(serviceMethod == "promediosSipsaCiudad"):
        getService = client.service.promediosSipsaCiudad()
    elif(serviceMethod == "promediosSipsaMesMadr"):
        getService = client.service.promediosSipsaMesMadr()
    elif(serviceMethod == "promediosSipsaParcial"):
        getService = client.service.promediosSipsaParcial()
    elif(serviceMethod == "promediosSipsaSemanaMadr"):
        getService = client.service.promediosSipsaSemanaMadr()
    elif(serviceMethod == "consultarInsumosSipsaMesMadr"):
        getService = client.service.consultarInsumosSipsaMesMadr(arg0 = arg0)
        
    return getService

def transformData(getService:object, fields:list)->object:
    response = []
    if(len(getService)>0):
        for record in getService:
            data = {}
            for field in fields:
                data[field] = str(record[field])
            response.append(data)    
    return response

def loadData(pathFile:str, data:object)->str:
    content = json.dumps(data, indent=4)
    fData = open(pathFile,"w")
    fData.write(content)
    fData.close()
    
def controller(wsdl:str, serviceMethod:str, arg0:int, fields:list, pathFile:str)->None:
    getService = extractData(wsdl, serviceMethod, arg0)
    print(">>> Data consultada.")
    data = transformData(getService, fields)
    print(">>> Data transformada en objectos.")
    loadData(pathFile, data)
    print(">>> Data almacenada en archivo Json.")
    print(">>> Load data in:", pathFile)