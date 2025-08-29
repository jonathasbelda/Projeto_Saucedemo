from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def instanciar_chrome():
    driver = webdriver.Chrome()  # Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  # maximizar a janela do chrome
    driver.get("https://www.saucedemo.com")  # Abrir a página soucedemo
    time.sleep(5)
    return driver

def realizar_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='inventory_container']")))
    

# Chamada das funções
driver = instanciar_chrome()
realizar_login(driver)

driver.quit()