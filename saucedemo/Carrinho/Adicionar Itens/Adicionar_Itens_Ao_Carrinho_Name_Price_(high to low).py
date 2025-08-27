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
