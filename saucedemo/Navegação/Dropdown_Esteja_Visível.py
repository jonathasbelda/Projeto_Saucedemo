#Rolar até o elemento de dropdown para garantir que está visível
dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(2)