from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Login_Page(LoginPage,):

    def language_selection(self, language_selected):
        if language_selected == 0:
            # dropdown_button = self.driver.find_element(*self.dropdown_element)
            # dropdown_button.click()
            # time.sleep(2)
            # choose_spanish = self.driver.find_element(*self.spanish)
            # choose_spanish.click()
            print("Spanish already selected")
            time.sleep(2)
        elif language_selected == 1:
            dropdown_button = self.driver.find_element(*self.dropdown_element)
            dropdown_button.click()
            time.sleep(2)
            choose_english = self.driver.find_element(*self.english)
            choose_english.click()
            time.sleep(2)
        else:
            print("Invalid option selected")
    def sign_in_with_google(self,username,password):
        main_window = self.driver.current_window_handle
        login_Button = self.driver.find_element(*self.login_button)
        login_Button.click()
        time.sleep(8)
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
        time.sleep(1)
        email_button = self.driver.find_element(*self.email)
        email_button.send_keys(username)
        time.sleep(3)
        email_next_button = self.driver.find_element(*self.next_email)
        email_next_button.click()
        time.sleep(3)

        password_button = self.driver.find_element(*self.Password)
        password_button.send_keys(password)
        password_next_button = self.driver.find_element(*self.next_password)
        show_Password_button = self.driver.find_element(*self.show_password)
        time.sleep(3)
        show_Password_button.click()
        password_next_button.click()

        try:
            config_error = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.ID, "error-code"))
            ).text
            print("Provided email is invalid")
        except:
            print("Logged in successfully")

        self.driver.switch_to.window(main_window)  # Switch back to the main window

        text_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 heading mui-9l3uo3']"))
        ).text
        time.sleep(3)

        print(text_field)

