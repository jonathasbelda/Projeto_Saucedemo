driver = webdriver.Chrome()  #Instancializar o Chrome
driver.implicitly_wait(10)
driver.maximize_window()  #Maximizar a janela do chrome
time.sleep(5) # Tempo de espera
driver.get("https://www.saucedemo.com")  # Abrir a página soucedemo


#Encontrar os elementos de e-mail,senha e o botão de clicar
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert driver.find_element(By.XPATH, "//*[@id='inventory_container']").is_displayed()  #confirmar se estamos dentro da página
time.sleep(3)


driver.quit()