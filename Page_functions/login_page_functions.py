from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.login_page import LoginPage
from selenium.webdriver.common.by import By
class Login_Page(LoginPage):

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
    def sign_in_with_google(self, username, password):
        try:
            print("Starting Google sign-in process...")
            # Store the main window handle
            main_window = self.driver.current_window_handle
            
            # Click the Google login button
            print("Clicking login button...")
            wait = WebDriverWait(self.driver, 20)
            login_button = wait.until(EC.element_to_be_clickable(self.login_button))
            login_button.click()
            
            # Wait for the new window to open and switch to it
            print("Waiting for Google login window...")
            wait.until(EC.number_of_windows_to_be(2))
            all_windows = self.driver.window_handles
            
            for window in all_windows:
                if window != main_window:
                    self.driver.switch_to.window(window)
                    break
            
            # Enter email
            print("Entering email...")
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # Try multiple selectors for email field
            try:
                email_field = wait.until(EC.visibility_of_element_located(self.email))
            except:
                # Alternative selectors if the primary one fails
                try:
                    email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
                except:
                    email_field = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
            
            email_field.clear()
            email_field.send_keys(username)
            
            # Click Next after entering email
            print("Clicking Next after email...")
            try:
                # Try multiple selectors for the Next button
                try:
                    next_button = wait.until(EC.element_to_be_clickable(self.next_email))
                except:
                    try:
                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                    except:
                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='identifierNext']//button")))
                
                next_button.click()
            except Exception as e:
                print(f"Error clicking Next after email: {e}")
                # Try JavaScript click as a fallback
                self.driver.execute_script("arguments[0].click();", next_button)
            
            # Wait for password field
            print("Entering password...")
            try:
                password_field = wait.until(EC.visibility_of_element_located(self.Password))
            except:
                # Alternative selectors if the primary one fails
                password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
            
            password_field.clear()
            password_field.send_keys(password)
            
            # Click Next after entering password
            print("Clicking Next after password...")
            try:
                try:
                    next_button = wait.until(EC.element_to_be_clickable(self.next_password))
                except:
                    try:
                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]")))
                    except:
                        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']//button")))
                
                next_button.click()
            except Exception as e:
                print(f"Error clicking Next after password: {e}")
                # Try JavaScript click as a fallback
                self.driver.execute_script("arguments[0].click();", next_button)
            
            # Switch back to the main window
            print("Switching back to main window...")
            self.driver.switch_to.window(main_window)
            print("Google sign-in completed successfully")
            
        except Exception as e:
            print(f"Error during Google sign-in: {e}")
            # Take screenshot on error
            self.driver.save_screenshot("/app/error_screenshot.png")
            raise

        try:
            config_error = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.ID, "error-code"))
            ).text
            print("Provided email is invalid")
        except:
            print("Logged in successfully")

        self.driver.switch_to.window(main_window)  # Switch back to the main window

        text_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="text-dashboard-heading"]'))
        ).text
        time.sleep(3)
        print(text_field)


