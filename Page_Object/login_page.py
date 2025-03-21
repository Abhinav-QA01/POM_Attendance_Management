from selenium.webdriver.common.by import By
from Import_libraries import Import_libraries
class LoginPage:
    def __init__(self, driver):
        self.driver=Import_libraries.driver
        self.dropdown_element = By.CSS_SELECTOR, '[data-test-id="select-language"]'
        self.spanish = By.CSS_SELECTOR, '[data-test-id="text-language-option-Español (España)"]'
        self.english = By.CSS_SELECTOR, '[data-test-id="text-language-option-English (EE.UU.)"]'
        self.login_button = By.CSS_SELECTOR, '[data-test-id="text-google-login"]'
        self.email = By.XPATH, '//*[@id="identifierId"]'
        self.next_email = By.XPATH, "//span[normalize-space()='Next']"
        self.Password = By.XPATH, "//input[@name='Passwd']"
        self.show_password = By.XPATH, "//input[@type='checkbox']"
        self.next_password = By.XPATH, "//span[normalize-space()='Next']"