
---

# Cliente - Webservice SIPSA  

***

El presente proyecto es un cliente de la Webservice SIPSA desarrollado en Python 3.8
usando la librería [Zeep](https://pypi.org/project/zeep/ "librería Zeep")
para acceder al servicio [SOAP](https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol "Simple Object Access Protocol") 
de la Webservice SIPSA mendiante la 
[WSDL](https://appweb.dane.gov.co/sipsaWS/SrvSipsaUpraBeanService?WSDL "WSDL de Webservice SIPSA")
que aparece en el 
[servicio web para consulta de la base de datos de sipsa](https://www.dane.gov.co/index.php/estadisticas-por-tema/agropecuario/sistema-de-informacion-de-precios-sipsa/servicio-web-para-consulta-de-la-base-de-datos-de-sipsa "WSDL de Webservice SIPSA").

Mejora:
<ul>
    <li>
        Ahora permite extraer la data en CSV, XML y Json, basta con definir el formato en el nombre del archivo destino.
    </li>
</ul>

## Procesos ETL
<ol>
    <li>Extrae los datos de su origen usando la librería Zeep. </li>
    <li>Transforma los datos que recibe de formato XML a objetos python.</li>
    <li>Almacena los datos en archivos planos en formato CSV, XML o JSON. </li>
</ol>

> La data recogida se almacenará en la carpeta data.

---

## Sobre la Webservice SIPSA

***

Teniendo en cuenta que el acceso a la información es un derecho de todos 
los colombianos, el DANE ha publicado de manera abierta y transparente la 
documentación de la Webservice SIPSA en su página web, para que cualquier 
interesado la pueda consultar.

Según sus desarrolladores:

> "Este servicio permite la consulta de la información consolidada 
en la base de datos del aplicativo SIPSA alimentada de los diferentes 
métodos de recolección para los productos agroalimentarios que se 
comercializan en el país" 

> "La implementación de este servicio Web está desarrollada bajo el estándar SOAP 
(Simple Object Access Protocol), en su versión 1.2, el cual permite el intercambio
de información en un formato XML bajo protocolo HTTP." 

El acceso se encuentra disponible para ser consumido bajo las siguientes condiciones:


Mayoristas - Están dispuestos los datos diarios, semanales y mensuales.  
> El consumo de los datos diarios y semanales,  
> se podrá llevar a cabo a partir de las 2 p.m.,  
> correspondientes a los datos del día,  
  
> los datos mensuales se actualizan el día 8 del mes en curso.  

Abastecimientos - La información se genera con una periodicidad mensual,  
> se actualiza el día 10 del mes en curso.  

---

## Documentación técnica del Cliente

***

### Configuración del entorno de desarrollo.
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |

***

### Librerías del proyecto.
| librería  | Descripción              | Comando                           |
| :----     | :---                     | :---                              |
| zeep      | Permite el acceso a SOAP | python -m pip install zeep        |
| xmltodict | Permite el acceso a SOAP | python -m pip install xmltodict   |

---

### Prueba - Realice un Test de los métodos.

***

#### Métodos

| Método Sipsa                  | Ejecución con python            |
| :---                          | :---                            |
| promedioAbasSipsaMesMadr()    | py promedioAbasSipsaMesMadr.py  |
| Cantidad promedio mensual en toneladas, <br> discriminada por productos y fuentes <br>de abastecimiento. | |
| promediosSipsaSemanaMadr()    | py promediosSipsaSemanaMadr.py  |
| Retorna los valores máximo, mínimo y <br> promedio semanal de recolección de <br> un producto, discriminando los datos <br> de la fuente. | |
| promediosSipsaParcial()       | py promediosSipsaParcial.py |
| Retorna los valores máximo, mínimo y <br> promedio parcial de recolección de un <br> producto, discriminando los datos de la <br> ubicación y la fuente. | |
| promediosSipsaCiudad()        | py promediosSipsaCiudad.py |
| Retorna los valores promedios<br> de cada producto por ciudad. | |
| promediosSipsaMesMadr()        | py promediosSipsaMesMadr.py |
| Retorna las cantidades máxima,<br> mínima y promedio mensual en Kg <br> de la recolección de un <br>producto, discriminando los <br>datos de la fuente. | |

***

### Realice sus pruebas, actualizaciones o modificaciones.
> Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.

> Si agregas nuevas librerías al proyecto, no olvides actualizar la receta.

``` CMD
pip freeze > requirements.txt
```

---

#### Comprobar que todo está en orden.
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    | Realice un Test de todos los métodos. |
| Paso 8 | Finalice su gestión.                          | deactivate                            |
