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



