from selenium import webdriver

browser = webdriver.Chrome('C:/Users/Dell/Downloads/chromedriver.exe')
browser.get('https://www.seleniumhq.org')
elem = browser.find_element_by_link_text('Download')
elem.click()
search = browser.find_element_by_id('q')
search.send_keys('Download')
