import time
from selenium import webdriver

from Page_functions.login_page_functions import Login_Page
from Process.login_process import Login_Process
from Import_libraries import Import_libraries
import user_details

driver = Import_libraries.initialize_driver()

driver.get(user_details.url)
driver.maximize_window()

time.sleep(4)

login_page_functions = Login_Page(driver)

def test_login_process():
    login_process = Login_Process(login_page_functions)
    login_process.run_process(user_details.username, user_details.password, user_details.language_selected)