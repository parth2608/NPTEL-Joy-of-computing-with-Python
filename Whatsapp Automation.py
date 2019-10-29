from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/Dell/Downloads/chromedriver.exe')
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)
target = '"Didi"'
string = "Message sent using Python!!!"
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = driver.find_element_by_class_name('_13mgZ')
for i in range(50):
    input_box.send_keys(string + Keys.ENTER)
