#Preencher informações de compra
driver.find_element(By.ID, "first-name").send_keys("Teste")
driver.find_element(By.ID, "last-name").send_keys("Automatizado")
driver.find_element(By.ID, "postal-code").send_keys("12345-678")
time.sleep(2)  

#clicar no botão de continuar
driver.find_element(By.XPATH, "//*[@id='continue']").click()
time.sleep(2)