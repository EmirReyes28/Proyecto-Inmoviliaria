<h1 align="center">Proyecto Inmoviliario</h1>
<img src="https://github.com/EmirReyes28/Contenido/blob/main/inmov.png" width="100%">
### texto explicativo
<img src="https://github.com/EmirReyes28/Contenido/blob/main/Diagrama%20sin%20título.drawio.png" width="100%">


## [Web Scraping Inmobiliario](https://github.com/EmirReyes28/Proyecto-Inmoviliaria/blob/master/WebScrapping/Remax_venta.py)
-A la izquierda, se muestra un proceso de scraping inmobiliario que se realiza mediante un script en Python. 
 Este script está siendo ejecutado en Azure Databricks.
 ## Generación de CSV
 -Los datos obtenidos por el scraping se transforman en un archivo CSV. Este formato es común para almacenar datos tabulares.
 ## Azure Data Lake:
 El archivo CSV se almacena en Azure Data Lake Storage, que actúa como un repositorio de datos brutos o 
 sin procesar (esta etapa a menudo se denomina "Capa Bronce").
 ## Capa de procesamiento en Azure Databricks:
 En el lado derecho, se muestra Azure Databricks nuevamente, pero en este caso con el objetivo de realizar transformaciones adicionales de los datos, estructurados en tres capas:
### [Capa Bronce](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/705185451510856/3027012851737615/779980591931427/latest.html)
- En esta capa se almacena la data cruda en un contenedor del ADLS llamado **bronze_layer**
### [Capa Plata](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/705185451510856/3027012851737620/779980591931427/latest.html)
- En esta capa se hace el limpiado de la informacion tales como eliminacion de elementos duplicados, separacion de columnas por elementos, cambio de tipo de dato de la columna y generado de un archivo parquet.
### [Capa Oro](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/705185451510856/696789662287551/779980591931427/latest.html)
- En esta capa se hizo un analisis mas detallado con respecto al costo promedio de departamentos y casas por distrito asi como el costo por metro cuadrado, con esta informacion es posible generar dashboards en power BI o Tableu.
