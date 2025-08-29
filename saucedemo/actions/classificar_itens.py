from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
    assert driver.find_element(By.XPATH, "//*[@id='inventory_container']").is_displayed()  # Confirmar se estamos dentro da página


# Selecionar itens por classificação Price (high to low)
def classificar_itens_high_to_low(driver):
    driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select").click()  # fechar o menu
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Price (high to low)")
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)


# Selecionar itens por classificação Price (low to high)
def classificar_itens_low_to_high(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Price (low to high)")
    time.sleep(3)


# Selecionar itens por classificação Name (Z to A)
def classificar_itens_name_z_to_a(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Name (Z to A)")
    time.sleep(3)


# Selecionar itens por classificação Name (A to Z)
def classificar_itens_name_a_to_z(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Name (A to Z)")
    time.sleep(3)


# Chamada da função
driver = instanciar_chrome()
realizar_login(driver)
classificar_itens_high_to_low(driver)
classificar_itens_low_to_high(driver)
classificar_itens_name_z_to_a(driver)
classificar_itens_name_a_to_z(driver)

driver.quit()
