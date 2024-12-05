from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]')
items = upcoming_events.find_elements(By.TAG_NAME, 'li')

upcoming_dict = dict()
for i in range(len(items)):
    split = items[i].text.split('\n')
    upcoming_dict[i] = {'time': split[0], 'name': split[1]}

print(upcoming_dict)
driver.quit()
