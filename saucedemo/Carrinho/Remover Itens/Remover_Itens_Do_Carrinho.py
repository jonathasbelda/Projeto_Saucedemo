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