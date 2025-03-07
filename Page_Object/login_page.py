import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Import_libraries import Import_libraries
class LoginPage:
    def __init__(self, driver):
        self.driver=Import_libraries.driver
        self.dropdown_element = By.XPATH, "//div[@class='item-language MuiBox-root mui-0']"
        self.spanish = By.XPATH, '//*[@id=":r0:"]/li[2]'
        self.english = By.XPATH, '//*[@id=":r0:"]/li[1]'
        self.login_button = By.XPATH, "//button[@type='button']"
        self.email = By.XPATH, '//*[@id="identifierId"]'
        self.next_email = By.XPATH, "//span[normalize-space()='Next']"
        self.Password = By.XPATH, "//input[@name='Passwd']"
        self.show_password = By.XPATH, "//input[@type='checkbox']"
        self.next_password = By.XPATH, "//span[normalize-space()='Next']"