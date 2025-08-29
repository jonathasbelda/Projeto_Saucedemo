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
    time.sleep(3)
    return driver

#realizar login
def realizar_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(By.XPATH, "//*[@id='inventory_container']").is_displayed()  # Confirmar se estamos dentro da página
    time.sleep(2)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(1)
   
#adicionar itens ao carrinho Name (A to Z)
def adicionar_ao_carrinho_A_to_Z(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()  #adicionar mochila ao carrinho
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
    time.sleep(3)

#continuar comprando
def continuar_comprando(driver):
    driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
    time.sleep(2)

#Selecionar itens por classificação Price (high to low)
def adicionar_itens_high_to_low(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Price (high to low)")
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()  #adicionar mochila ao carrinho
    time.sleep(3)
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()     
    time.sleep(3)

def continuar_comprando(driver):
    driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
    time.sleep(3)

#Selecionar itens por classificação Price (low to high)
def adicionar_itens_low_to_high(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Price (low to high)")
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()  #adicionar mochila ao carrinho
    time.sleep(3)
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
    time.sleep(3)
  
def continuar_comprando(driver):
    driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
    time.sleep(3)

#Selecionar itens por classificação Name (Z to A)
def adicionar_itens_name_z_to_a(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    select.select_by_visible_text("Name (Z to A)")
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()  #adicionar mochila ao carrinho
    time.sleep(3)
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click() 
    time.sleep(3)
    dropdown = driver.find_element(By.CLASS_NAME, "cart_contents_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)


# Chamada da função
driver = instanciar_chrome()
realizar_login(driver)
adicionar_ao_carrinho_A_to_Z(driver)
continuar_comprando(driver) 
adicionar_itens_high_to_low(driver)
continuar_comprando(driver)
adicionar_itens_low_to_high(driver)
continuar_comprando(driver)
adicionar_itens_name_z_to_a(driver)

driver.quit()
