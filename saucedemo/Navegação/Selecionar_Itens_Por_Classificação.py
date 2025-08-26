#Selecionar itens por classificação Price (high to low)
driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/div/span/select").click()  #fechar o menu
time.sleep(3)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Price (high to low)")
time.sleep(5)


#Selecionar itens por classificação Price (low to high)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container") 
select = Select(dropdown)
select.select_by_visible_text("Price (low to high)")
time.sleep(3)


#Selecionar itens por classificação Name (Z to A)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Name (Z to A)")
time.sleep(3)


#Selecionar itens por classificação Name (A to Z)
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(dropdown)
select.select_by_visible_text("Name (A to Z)")
time.sleep(3)

driver.quit()