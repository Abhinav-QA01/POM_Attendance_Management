import time
from Page_functions.login_page_functions import Login_Page
from Process.login_process import Login_Process
from Import_libraries import Import_libraries
import user_details
from Process.Groups_of_2025_2026_process import Group_Navigation_Process
from Page_functions.Groups_of_2025_2026_functions import Group_2025_2026_Function

driver = Import_libraries.initialize_driver()

driver.get(user_details.url)
driver.maximize_window()

time.sleep(4)

login_page_functions = Login_Page(driver)
group_2025_2026_function = Group_2025_2026_Function(driver, x = None, y = None)

def test_login_process():
    login_process = Login_Process(login_page_functions)
    login_process.run_process(user_details.username, user_details.password, user_details.language_selected)

def test_Group_of_2025_2026_process():
    group_navigation_2025_2026_process = Group_Navigation_Process(group_2025_2026_function)
    group_navigation_2025_2026_process.run_group_process()