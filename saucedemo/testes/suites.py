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
    time.sleep(2)
    return driver

#realizar login
def realizar_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user") 
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(By.XPATH, "//*[@id='inventory_container']").is_displayed()  # Confirmar se estamos dentro da página
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
 
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

#Selecionar itens por classificação Price (high to low)
def adicionar_itens_high_to_low(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    time.sleep(1)
    select.select_by_visible_text("Price (high to low)")
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()  #adicionar mochila ao carrinho
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()     
    time.sleep(3)

def continuar_comprando(driver):
    driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()

#Selecionar itens por classificação Price (low to high)
def adicionar_itens_low_to_high(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    time.sleep(1)
    select.select_by_visible_text("Price (low to high)")
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()  #adicionar mochila ao carrinho
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
    time.sleep(3)

def continuar_comprando(driver):
    driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()

#Selecionar itens por classificação Name (Z to A)
def adicionar_itens_name_z_to_a(driver):
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(dropdown)
    time.sleep(1)
    select.select_by_visible_text("Name (Z to A)")
    dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()  #adicionar mochila ao carrinho
    assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click() 
    dropdown = driver.find_element(By.CLASS_NAME, "cart_contents_container") #Rolar até o elemento de dropdown para garantir que está visível
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)
    time.sleep(3)

#remover itens do carrinho
def remover_itens_carrinho(driver):
    driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']").click()  #remover item do carrinho
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='remove-test.allthethings()-t-shirt-(red)']").click()  #remover item do carrinho
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-onesie']").click()  #remover item do carrinho
    time.sleep(2)
 
#finalizar compra
def finalizar_compra(driver):
    driver.find_element(By.XPATH, "//*[@id='checkout']").click()  #clicar no botão checkout
    time.sleep(2)
    driver.find_element(By.ID, "first-name").send_keys("Teste") 
    driver.find_element(By.ID, "last-name").send_keys("Automatizado")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(3)
    driver.find_element(By.ID, "continue").click()  #clicar no botão continuar
    time.sleep(5)
    assert driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']").is_displayed()  #Confirmar se estamos dentro da página de finalização
    driver.find_element(By.XPATH, "//*[@id='finish']").click()  #clicar no botão finalizar
    time.sleep(2)
    assert driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']").is_displayed()  #Confirmar se a compra foi finalizada com sucesso
    driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()  #clicar no botão de voltar ao início
    time.sleep(2)

#abrir menu lateral
def abrir_menu(driver):
    #Abrir o menu lateral
    driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(2)

#logar botão about
def clicar_botao_about(driver):
    driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()  #Clicar no botão de Logout
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
remover_itens_carrinho(driver)
finalizar_compra(driver)
abrir_menu(driver)
clicar_botao_about(driver)

driver.quit()