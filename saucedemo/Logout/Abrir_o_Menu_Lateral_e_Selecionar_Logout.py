#Abrir o menu lateral e selecionar Logout
driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()  #Clicar no botão Menu
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()  #Clicar no botão de Logout
time.sleep(2)

driver.quit()  #Fechar o navegador