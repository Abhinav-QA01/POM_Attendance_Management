import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
username = "abhinav.1154@zenmonk.tech"
password = "Abhizenmonk1234"

driver = webdriver.Edge()
driver.maximize_window()

page_url = "https://academic-teaching-attendance-control-app-develop-iymj66chvq-uc.a.run.app/"
driver.get(page_url)
time.sleep(3)

main_window = driver.current_window_handle

driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(8)
all_windows = driver.window_handles

for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break
driver.find_element(By.ID, "identifierId").send_keys(username)
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(password)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

driver.switch_to.window(main_window)  # Switch back to the main window

text_field = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 heading mui-9l3uo3']"))
)
time.sleep(3)