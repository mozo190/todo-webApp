import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Disable the search engine choice screen
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

# Set the download path
download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

# Set the path to the chromedriver executable
service_ = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service_)

driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

username_field.send_keys('zomo')
password_field.send_keys('Python123@')
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Text Box
elements = (WebDriverWait(driver, 10).
            until(EC.visibility_of_element_located((By.XPATH,
                                                    '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()

text_box = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0'))))
text_box.click()

# Locate the form fields and submit button
full_name = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName'))))
email_address = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail'))))
current_address = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress'))))
permanent_address = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress'))))
submit_button = driver.find_element(By.ID, 'submit')

# Fill the form fields
full_name.send_keys('Zomo')
email_address.send_keys('zozozo@citromail.com')
current_address.send_keys('Budapest')
permanent_address.send_keys('Budapest')
driver.execute_script("arguments[0].click();", submit_button)

# Locate the Upload and Download link
upload_download = (WebDriverWait(driver, 10).
                   until(EC.visibility_of_element_located((By.ID, 'item-7'))))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

input('Press Enter to close the browser...')
driver.quit()
