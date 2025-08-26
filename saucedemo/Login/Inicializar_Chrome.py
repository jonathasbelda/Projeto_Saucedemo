from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()  #Instancializar o Chrome
driver.implicitly_wait(10)
driver.maximize_window()  #maximizar a janela do chrome
time.sleep(5)
driver.get("https://www.saucedemo.com")  #Abrir a página soucedemo

driver.quit()