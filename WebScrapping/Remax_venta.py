from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



website = 'https://www.remax.pe/web/search/all/propertys/list/?&page=2'
path = 'C:\\Users\\ADMIN\\Downloads\\chromedriver-win64\\chromedriver.exe'

driver = uc.Chrome()
driver.get(website)
driver.maximize_window()

ultima_pagina=400
primera_pagina=1

direccion = []
Tipo=[]
precio_soles = []
precio_dolares = []
Pisos=[]
banos=[]
cochera=[]
dormitorios=[]
Area_construida=[]
Area_total=[]



while primera_pagina <=ultima_pagina:
    time.sleep(2)
    container=driver.find_element(By.XPATH,"//div[@class='col-12 col-md-12 ']/div")
    casas=container.find_elements(By.XPATH,'./div')

    for casa in casas:
        try:
            direccion.append(casa.find_element(By.XPATH,".//div[@class='__casadat']/h5[1]").text)
        except:
            direccion.append('NULL')
        try:
            Tipo.append(casa.find_element(By.XPATH,".//div[@class='__tipov']/span[1]").text)
        except:
            Tipo.append('NULL')
        try:
            precio_soles.append(casa.find_element(By.XPATH,".//div[@class='__casventap']/ul/li[1]").text)
        except:
            precio_soles.append('NULL')
        try:
            precio_dolares.append(casa.find_element(By.XPATH,".//div[@class='__casventap']/ul/li[3]").text)
        except:
            precio_dolares.append('NULL')
        try:
            dormitorios.append(casa.find_element(By.XPATH,".//div[@class='feature-data']/div[4]/p").text)
        except:
            dormitorios.append('NULL')
        try:
            Area_construida.append(casa.find_element(By.XPATH, ".//div[@class='feature-data']/div[1]/p").text)
        except:
            Area_construida.append('NULL')
        try:
            Area_total.append(casa.find_element(By.XPATH, ".//div[@class='feature-data']/div[2]/p").text)
        except:
            Area_total.append('NULL')
        try:
            Pisos.append(casa.find_element(By.XPATH, ".//div[@class='feature-data']/div[3]/p").text)
        except:
            Pisos.append('NULL')
        try:
            banos.append(casa.find_element(By.XPATH, ".//div[@class='feature-data']/div[5]/p").text)
        except:
            banos.append('NULL')
        try:
            cochera.append(casa.find_element(By.XPATH, ".//div[@class='feature-data']/div[6]/p").text)
        except:
            cochera.append('NULL')

    primera_pagina = primera_pagina + 1
    try:
        page = driver.find_element(By.XPATH, '//ul[@class="pagination"]/li[3]/a')
        page.click()
    except:
        pass

driver.quit()


casas_ventas_df=pd.DataFrame({'Tipo de Inmueble':Tipo,'Direccion':direccion,'Area Construida':Area_construida,
                              'Area Total':Area_total,'Pisos':Pisos,'dormitorios':dormitorios,'baños':banos,
                              'Cochera':cochera,'Precio Soles':precio_soles,'Precio Dolares':precio_dolares})
casas_ventas_df.to_csv('Remax_Venta.csv',index=False)