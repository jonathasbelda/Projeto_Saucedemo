from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()  #Instancializar o Chrome
driver.implicitly_wait(10)
driver.maximize_window()  #maximizar a janela do chrome
time.sleep(5)
driver.get("https://www.saucedemo.com")  # Abrir a página soucedemo


#Encontrar os elementos de e-mail,senha e o botão de clicar
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(
By.XPATH, "//*[@id='inventory_container']").is_displayed()  #confirmar se estamos dentro da página
time.sleep(3)


#Abrir o menu lateral
driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
time.sleep(2)

#Clicar no botao about
driver.find_element(By.PARTIAL_LINK_TEXT, "About").click()
time.sleep(2)
driver.back()  #botão de voltar da página https://saucelabs.com

#Selecionar itens por classificação Price (high to low)
driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select").click()  # fechar o menu
time.sleep(3)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Price (high to low)")
time.sleep(3)

#Selecionar itens por classificação Price (low to high)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") 
select = Select(dropdown)
select.select_by_visible_text("Price (low to high)")
time.sleep(3)

#Selecionar itens por classificação Name (Z to A)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Name (Z to A)")
time.sleep(3)

#Selecionar itens por classificação Name (A to Z)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Name (A to Z)")
time.sleep(3)

#Rolar até o elemento de dropdown para garantir que está visível
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(2)

#adicionar itens ao carrinho Name (A to Z)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()  #adicionar mochila ao carrinho
time.sleep(2)

#verificar se o item foi adicionado ao carrinho
assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
time.sleep(3)

#continuar comprando
driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
time.sleep(2)

#Selecionar itens por classificação Price (high to low)
driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select").click()  # fechar o menu
time.sleep(3)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Price (high to low)")
time.sleep(3)

#Rolar até o elemento de dropdown para garantir que está visível
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(2)

#adicionar itens ao carrinho  Price (higt to low)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()  #adicionar mochila ao carrinho
time.sleep(3)

#verificar se o item foi adicionado ao carrinho
assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
time.sleep(3)

#continuar comprando
driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
time.sleep(3)

#Selecionar itens por classificação Price (low to high)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") 
select = Select(dropdown)
select.select_by_visible_text("Price (low to high)")
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(3)

#adicionar itens ao carrinho Price (low to high)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()  #adicionar mochila ao carrinho
time.sleep(3)

#verificar se o item foi adicionado ao carrinho
assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
time.sleep(3)

#continuar comprando
driver.find_element(By.XPATH, "//*[@id='continue-shopping']").click()
time.sleep(3)

#Selecionar itens por classificação Name (Z to A)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Name (Z to A)")
time.sleep(3)

#Rolar até o elemento de dropdown para garantir que está visível
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(2)

#adicionar itens ao carrinho  Name (Z to A)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()  #adicionar mochila ao carrinho
time.sleep(3)

#verificar se o item foi adicionado ao carrinho
assert driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").is_displayed() #verifica se o elemento do carrinho está visível na página.
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
time.sleep(3)

#remover um item do carrinho
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']").click()  #remover item do carrinho
assert driver.find_element(By.XPATH, "//*[@id='cart_contents_container']").is_displayed() #Verifica se está na página do carrinho antes de remover outro item
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(2)

#remover um item do carrinho
driver.find_element(By.XPATH, "//*[@id='remove-test.allthethings()-t-shirt-(red)']").click()  #remover item do carrinho
assert driver.find_element(By.XPATH, "//*[@id='cart_contents_container']").is_displayed() #Verifica se está na página do carrinho antes de remover outro item
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(2)

#remover um item do carrinho
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bike-light']").click()  #remover item do carrinho
assert driver.find_element(By.XPATH, "//*[@id='cart_contents_container']").is_displayed() #Verifica se está na página do carrinho antes de remover outro item
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
time.sleep(2)

#Finalizar compra
driver.find_element(By.XPATH, "//*[@id='checkout']").click()  #clicar no botão de checkout
time.sleep(2)

#Preencher informações de compra
driver.find_element(By.ID, "first-name").send_keys("Teste")
driver.find_element(By.ID, "last-name").send_keys("Automatizado")
driver.find_element(By.ID, "postal-code").send_keys("12345-678")
time.sleep(2)  

#clicar no botão de continuar
driver.find_element(By.XPATH, "//*[@id='continue']").click()
time.sleep(2)

#verificar se está na página de overview
assert driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']").is_displayed()

#Finalizar a compra clicando no botão finish
driver.find_element(By.XPATH, "//*[@id='finish']").click()
time.sleep(2)

#verificar se a compra foi finalizada
assert driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']").is_displayed()
time.sleep(2)  

#verifica se o botão de voltar ao início está visível
assert driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']").is_displayed()
driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()  #clicar no botão de voltar ao início
time.sleep(2)

# Abrir o menu lateral e selecionar Logout
driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()  #Clicar no botão Menu
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()  #Clicar no botão de Logout
time.sleep(2)

driver.quit()  #Fechar o navegador