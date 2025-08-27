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