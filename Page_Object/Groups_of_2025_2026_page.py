from selenium.webdriver.common.by import By
from Import_libraries import Import_libraries
class Group_2025_2026:
    def __init__(self,driver):
        self.driver=Import_libraries.driver
        self.groups_2025_2026 = By.CSS_SELECTOR, '[data-test-id="btn-open-parent-academic-period-Groups of 2025-2026"]'
        self.sem_2 = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-period-Sem 2"]'
        self.sem_1 = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-period-Sem 1"]'
        self.sem_2_course = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-element-Physics"]'
        self.sem_1_course = By.CSS_SELECTOR, '[data-test-id="text-selected-academic-element-title-Biología - IYA024-v1"]'
        self.sem_2_course_attendances = By.CSS_SELECTOR, '[data-test-id="btn-open-attendance-group-G2V2 A2B2 VCF"]'
        self.sem_1_course_attendances = By.CSS_SELECTOR, '[data-test-id="btn-open-attendance-group-G1V1 A1B1 VCE"]'
