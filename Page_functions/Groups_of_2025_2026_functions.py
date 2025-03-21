from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.Groups_of_2025_2026_page import Group_2025_2026
from selenium.webdriver.common.by import By


class Group_2025_2026_Function(Group_2025_2026):
    def navigate_to_table(self):
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
        time.sleep(2)
