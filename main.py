#!/usr/bin/env python
# _*_ coding: utf8 _*_

""" ********************************
autor : aaron.parodip@codeecuador.com

ultima vez editado: 29/06/2021 12:14
*********************************"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

# def main():
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
)

driver = webdriver.Chrome('chromedriver.exe', options=opts)
driver.get('https://www.linkedin.com/')
time.sleep(2)

# *** Iniciando sesión ***
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

# *** Credenciales ***

username.send_keys('parodi-14@hotmail.com')
clave = open('C:/code_linkedin/clave.txt').readline().strip()
password.send_keys(clave)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

driver.get("https://www.linkedin.com/company/codeecuador")
time.sleep(2)

driver.get("https://www.linkedin.com/company/78186439/admin/analytics/visitors/")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
boton_exportar = [btn for btn in all_buttons if btn.text == "Exportar"]

for i in range(0, len(boton_exportar)):
    boton_exportar[i].click()

    driver.execute_script("arguments[0].click();", boton_exportar[i])
    time.sleep(2)

boton_exportar2 = driver.find_element(By.XPATH, '//span[text()="Exportar"]')
boton_exportar2.click()

#todo poner todo en una funcion
#todo guardar el archivo exportado en una ruta especifica
#todo implementar libreria OPENPYXL
#TODO implementar librería FPDF para hacer un reporte vistoso
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("Saliendo")
