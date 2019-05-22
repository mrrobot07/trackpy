from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://tienda.claro.com.do')
browser.maximize_window()
result = browser.find_element_by_class_name('c-brand-bar__region-drop-down[data-toggle="brand-bar-MiCuenta"]')
result.click()
result2 = browser.find_element_by_xpath("//*[contains(@value,'Inicia sesión')] | //*[contains(text(),'Inicia sesión')]")

result2.click()