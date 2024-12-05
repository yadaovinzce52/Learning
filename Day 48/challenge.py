from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Vinzce")
last_name.send_keys("Yadao")
email.send_keys("yadaovinzce@gmail.com")

submit = driver.find_element(By.XPATH, value='/html/body/form/button')
submit.click()

driver.quit()