from selenium.webdriver.common.by import By
from Import_libraries import DriverManager
class LoginPage:
    def __init__(self, driver):
        self.driver=DriverManager.get_driver()
        # App language selection
        self.dropdown_element = By.CSS_SELECTOR, '[data-test-id="select-language"]'
        self.spanish = By.CSS_SELECTOR, '[data-test-id="text-language-option-Español (España)"]'
        self.english = By.CSS_SELECTOR, '[data-test-id="text-language-option-English (EE.UU.)"]'
        
        # Google login button in the app
        self.login_button = By.CSS_SELECTOR, '[data-test-id="text-google-login"]'
        
        # Google login form - multiple selectors for better compatibility
        # Email field selectors
        self.email = By.XPATH, '//input[@type="email" or @id="identifierId"]'
        
        # Next button after email - multiple options
        self.next_email = By.XPATH, "//span[text()='Next']/parent::button | //div[@id='identifierNext']//button | //button[contains(., 'Next')]"
        
        # Password field selectors
        self.Password = By.XPATH, "//input[@name='Passwd' or @type='password']"
        self.show_password = By.XPATH, "//input[@type='checkbox']"
        
        # Next button after password - multiple options
        self.next_password = By.XPATH, "//span[text()='Next']/parent::button | //div[@id='passwordNext']//button | //button[contains(., 'Next')]"
        
        # Error messages
        self.error_message = By.XPATH, "//div[contains(@class, 'error') or contains(@class, 'Error')]"