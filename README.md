<h1 align="center">Proyecto Inmoviliario</h1>
<img src="https://github.com/EmirReyes28/Contenido/blob/main/Diagrama%20sin%20título.drawio.png" width="100%">


### [Web Scraping Inmobiliario](https://github.com/EmirReyes28/Proyecto-Inmoviliaria/blob/master/WebScrapping/Remax_venta.py)
-A la izquierda, se muestra un proceso de scraping inmobiliario que se realiza mediante un script en Python. 
 Este script está siendo ejecutado en Azure Databricks.
 <h3 align="left">Generación de CSV:</h3>
 -Los datos obtenidos por el scraping se transforman en un archivo CSV. Este formato es común para almacenar datos tabulares.
 <h3 align="left">Azure Data Lake:</h3>
 El archivo CSV se almacena en Azure Data Lake Storage, que actúa como un repositorio de datos brutos o 
 sin procesar (esta etapa a menudo se denomina "Capa Bronce").
 <h3 align="left">Capa de procesamiento en Azure Databricks:</h3>
 En el lado derecho, se muestra Azure Databricks nuevamente, pero en este caso con el objetivo de realizar transformaciones adicionales de los datos, estructurados en tres capas:
#### [Capa Bronce](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/705185451510856/3027012851737615/779980591931427/latest.html)
Capa Plata: Aquí se procesan los datos (limpieza, validación).
Capa Oro: Datos completamente transformados y listos para análisis o uso en reportes y dashboards.
