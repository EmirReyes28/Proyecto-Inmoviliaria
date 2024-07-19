from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



website = 'https://urbania.pe/buscar/venta-de-propiedades'
path = 'C:\\Users\\ADMIN\\Downloads\\chromedriver-win64\\chromedriver.exe'

driver = uc.Chrome()
driver.get(website)
driver.maximize_window()

cookie=driver.find_element(By.XPATH,"//button[@data-qa='cookies-policy-banner']")
cookie.click()
time.sleep(3)


ultima_pagina=300
primera_pagina=1

direccion = []
distrito = []
precio = []
dormitorios=[]
metraje=[]



while primera_pagina <=ultima_pagina:
    time.sleep(2)
    container=driver.find_element(By.CLASS_NAME,'postings-container')
    casas=container.find_elements(By.XPATH,'./div')

    for casa in casas:
        try:
            direccion.append(casa.find_element(By.XPATH,".//div[@class='LocationBlock-sc-ge2uzh-1 cVCbkm']/div").text)
        except:
            direccion.append('NULL')
        try:
            distrito.append(casa.find_element(By.XPATH,".//div[contains(@class,'LocationBlock')]/h2").text)
        except:
            distrito.append('NULL')
        try:
            precio.append(casa.find_element(By.XPATH,".//div[contains(@class,'PriceContainer')]/div").text)
        except:
            precio.append('NULL')
        try:
            dormitorios.append(casa.find_element(By.XPATH,".//span[contains(text(),'dorm')]").text)
        except:
            dormitorios.append('NULL')
        try:
            metraje.append(casa.find_element(By.XPATH, ".//span[contains(text(),'m²')]").text)
        except:
            metraje.append('NULL')

    primera_pagina = primera_pagina + 1
    try:
        page = driver.find_element(By.XPATH, '//a[@data-qa="PAGING_NEXT"]')
        page.click()
    except:
        pass

driver.quit()


casas_ventas_df=pd.DataFrame({'direccion':direccion,'distrito':distrito,'metraje':metraje,'dormitorios':dormitorios,'precio':precio})
casas_ventas_df.to_csv('Urbania_Venta.csv',index=False)

