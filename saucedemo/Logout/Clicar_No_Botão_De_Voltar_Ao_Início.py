#verifica se o botão de voltar ao início está visível
assert driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']").is_displayed()
driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()  #clicar no botão de voltar ao início
time.sleep(2)