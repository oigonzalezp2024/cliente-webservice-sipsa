import csv
import json
import zeep
import xmltodict

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

def loadData(pathFile:str, fields:list, data:object)->str:
    if(pathFile[-4:]=='json'):
        jsonData(pathFile, data)
    elif(pathFile[-4:]=='.csv'):
        csvData(pathFile, fields, data)
    elif(pathFile[-4:]=='.xml'): 
        xmlData(pathFile, data)

def jsonData(pathFile:str, data:object)->None:
    content = json.dumps(data, indent=4)
    fData = open(pathFile,"w")
    fData.write(content)
    fData.close()

def csvData(pathFile:str, fields:list, data:object)->None:
    with open(pathFile, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
        i = 0
        while(len(data)>i):
            record = []
            for field in fields:
                record.append(data[i][field])
            spamwriter.writerow(record)
            i+=1

def xmlData(pathFile:str, data:object)->None:
    content = ""
    i = 0
    for elem in data:
        txt = ""
        mydict = {'return': elem}
        txt = xmltodict.unparse(mydict, pretty=True)
        if(i>0):
            txt = txt.replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>","")
        i+=1
        content += txt
    fData = open(pathFile,"w")
    fData.write(content)
    fData.close()   

def controller(wsdl:str, serviceMethod:str, arg0:int, fields:list, pathFile:str)->None:
    getService = extractData(wsdl, serviceMethod, arg0)
    print(">>> Data consultada.")
    data = transformData(getService, fields)
    print(">>> Data transformada en objectos.")
    loadData(pathFile, fields, data)
    print(">>> Data almacenada en archivo Json." + pathFile[-4:])
    print(">>> Load data in:", pathFile)
