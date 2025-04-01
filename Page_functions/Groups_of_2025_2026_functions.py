from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.Groups_of_2025_2026_page import Group_2025_2026
from selenium.webdriver.common.by import By


class Group_2025_2026_Function(Group_2025_2026):
    def navigate_to_table(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="btn-open-parent-academic-period-Groups of 2025-2026"]')
            )
        )
        group_element = self.driver.find_element(*self.groups_2025_2026)
        group_element.click()
        time.sleep(2)
        sem_2_element = self.driver.find_element(*self.sem_2)
        sem_2_element.click()
        time.sleep(2)
        sem_2_course_element = self.driver.find_element(*self.sem_2_course)
        sem_2_course_element.click()
        time.sleep(2)
        sem_2_course_element_attendances_elements = self.driver.find_element(*self.sem_2_course_attendances)
        sem_2_course_element_attendances_elements.click()


        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,'[data-test-id="td-session-cell-1-1"]')
            )
        )
        for x in range(1,10):
            for y in range(1,10):
                sem_2_table_element_path = f'[data-test-id="td-session-cell-{y}-{x}"]'
                sem_2_table_element =self.driver.find_element(By.CSS_SELECTOR, sem_2_table_element_path)
                sem_2_table_element.click()

                time.sleep(1)
                present_button = '[data-test-id="li-Attendance"]'
                present_button_element =  self.driver.find_element(By.CSS_SELECTOR, present_button)
                present_button_element.click()
                time.sleep(1)
