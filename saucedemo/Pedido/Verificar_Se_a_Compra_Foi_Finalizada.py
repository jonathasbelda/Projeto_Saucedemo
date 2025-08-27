#verificar se está na página de overview
assert driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']").is_displayed()

#Finalizar a compra clicando no botão finish
driver.find_element(By.XPATH, "//*[@id='finish']").click()
time.sleep(2)

#verificar se a compra foi finalizada
assert driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']").is_displayed()
time.sleep(2)  