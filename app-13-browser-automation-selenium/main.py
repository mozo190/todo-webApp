from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_ = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_)

driver.get('https://demoqa.com/login')

input('Press Enter to close the browser...')

driver.quit()
