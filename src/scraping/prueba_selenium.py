from selenium import webdriver


driver = webdriver.Edge()

driver.get("https://www.google.com")

print("Título de la web:")
print(driver.title)

input("Pulsa ENTER para cerrar el navegador...")

driver.quit()