from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

service_ = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_)

driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

username_field.send_keys('zomo')
password_field.send_keys('Python123@')
driver.execute_script("arguments[0].click();", login_button)

input('Press Enter to close the browser...')
driver.quit()
