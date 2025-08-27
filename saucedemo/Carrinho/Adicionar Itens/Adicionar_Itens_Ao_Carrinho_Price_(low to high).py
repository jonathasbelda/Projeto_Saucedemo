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