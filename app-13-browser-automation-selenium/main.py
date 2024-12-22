import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebAutomation:
    def __init__(self):
        # Disable the search engine choice screen
        chrome_options = Options()
        chrome_options.add_argument('--disable-search-engine-choice-screen')

        # Set the download path
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Set the path to the chromedriver executable
        service_ = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=service_)

    def login(self, username, password):
        self.driver.get('https://demoqa.com/login')

        # Locate the username and password fields and the login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, full_name_str, email_address_str, current_address_str, permanent_address_str):
        # Locate the Elements dropdown and Text Box
        elements = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()

        text_box = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0'))))
        text_box.click()

        # Locate the form fields and submit button
        full_name = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName'))))
        email_address = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail'))))
        current_address = (
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress'))))
        permanent_address = (
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress'))))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill the form fields
        full_name.send_keys(full_name_str)
        email_address.send_keys(email_address_str)
        current_address.send_keys(current_address_str)
        permanent_address.send_keys(permanent_address_str)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def upload_download(self):
        # Locate the Upload and Download link
        upload_download = (WebDriverWait(self.driver, 10).
                           until(EC.visibility_of_element_located((By.ID, 'item-7'))))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    # input('Press Enter to close the browser...')
    webAutomation = WebAutomation()
    webAutomation.login('Zomo', 'Python@123')
    webAutomation.fill_form('Zomo', 'zooo@gamil.com', 'Budapest', 'Budapest')
    webAutomation.upload_download()
    webAutomation.close_browser()
    # Program stops here
    print('Browser closed...')
