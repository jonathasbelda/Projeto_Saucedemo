from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#Configurações do Chrome
def instanciar_chrome():
    driver = webdriver.Chrome()  #Instancializar o Chrome
    driver.implicitly_wait(10)
    driver.maximize_window()  #maximizar a janela do chrome
    driver.get("https://www.saucedemo.com")  # Abrir a página soucedemo
    time.sleep(5)
    return driver

#realizar login
def realizar_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(
        By.XPATH, "//*[@id='inventory_container']").is_displayed()  # Confirmar se estamos dentro da página

#Abrir o menu lateral
def abrir_menu(driver):
    driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(2)

#Clicar no botao about
def clicar_botao_about(driver):
    driver.find_element(By.PARTIAL_LINK_TEXT, "About").click()
    driver.back()  #botão de voltar da página https://saucelabs.com
    time.sleep(2)

# Chamada das funções
driver = instanciar_chrome()
realizar_login(driver)
abrir_menu(driver)
clicar_botao_about(driver)

driver.quit()