from selenium.webdriver.common.by import By
from Import_libraries import DriverManager
class Group_2025_2026:
    def __init__(self, driver,x,y):
        self.driver=DriverManager.get_driver()
        self.groups_2025_2026 = By.CSS_SELECTOR, '[data-test-id="btn-open-parent-academic-period-Groups of 2025-2026"]'
        self.sem_2 = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-period-Sem 2"]'
        self.sem_1 = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-period-Sem 1"]'
        self.sem_2_course = By.CSS_SELECTOR, '[data-test-id="btn-open-academic-element-Physics"]'
        self.sem_1_course = By.CSS_SELECTOR, '[data-test-id="text-selected-academic-element-title-Biología - IYA024-v1"]'
        self.sem_2_course_attendances = By.CSS_SELECTOR, '[data-test-id="btn-open-attendance-group-G2V2 A2B2 VCF"]'
        self.sem_1_course_attendances = By.CSS_SELECTOR, '[data-test-id="btn-open-attendance-group-G1V1 A1B1 VCE"]'


        self.table_element = By.CSS_SELECTOR,'[data-test-id="td-session-cell-{y}-{x}"]'
        self.present_button = By.CSS_SELECTOR, '[data-test-id="li-Attendance"]'
        self.late_button = By.CSS_SELECTOR, '[data-test-id="li-Lateness"]'
        self.absence_button = By.CSS_SELECTOR, '[data-test-id="li-Absence"]'
        self.release_button = By.CSS_SELECTOR, '[data-test-id="li-Release"]'
        self.justify_late_button = By.CSS_SELECTOR, '[data-test-id="li-justify-late"]'
        self.justify_absence_button = By.CSS_SELECTOR, '[data-test-id="li-justify-absent"]'
        self.delete_justification_button = By.CSS_SELECTOR, '[data-test-id="li-delete-justification"]'
        self.confirm_delete_justification_button = By.CSS_SELECTOR, '[data-test-id="btn-confirm-Delete justification"]'

        self.file_uploader_element = By.CSS_SELECTOR, '[data-test-id="div-file-uploader"]'
        self.file_upload_confirm_button = By.CSS_SELECTOR, '[data-test-id="btn-confirm-justification"]'


        self.unmark_button = By.CSS_SELECTOR,'[data-test-id="li-unmark-attendance"]'

        # self.more_vertical_options_button = By.CSS_SELECTOR, '[data-testid="MoreVertIcon"]'
        self.mark_all_as_button = By.CSS_SELECTOR, '[data-test-id="icon-user"]'
        self.mark_all_attendance = By.CSS_SELECTOR, '[data-test-id="icon-Attendance"]'
        self.mark_all_lateness = By.CSS_SELECTOR, '[data-test-id="icon-Lateness"]'
        self.mark_all_absence = By.CSS_SELECTOR, '[data-test-id="icon-Absence"]'
        self.mark_all_release = By.CSS_SELECTOR, '[data-test-id="icon-Release"]'
        self.unmark_all = By.CSS_SELECTOR, '[data-test-id="icon-unmark"]'


        self.edit_this_session = By.CSS_SELECTOR, '[data-test-id="li-edit-session-8f8e391d-2dbf-42af-b2e5-49b16dc69259"]'

        self.session_type_button = By.CSS_SELECTOR, '[data-test-id="select-session-type-8f8e391d-2dbf-42af-b2e5-49b16dc69259"]'
        self.session_type_option_1_button = By.CSS_SELECTOR,'[data-test-id="li-session-type-Theoretical/practical-8f8e391d-2dbf-42af-b2e5-49b16dc69259"]'
        self.session_type_option_2_button = By.CSS_SELECTOR, '[data-test-id="li-session-type-Practical-8f8e391d-2dbf-42af-b2e5-49b16dc69259"]'

        self.number_of_hours_field = By.CSS_SELECTOR, '[data-test-id="input-number-of-hours-8f8e391d-2dbf-42af-b2e5-49b16dc69259"]'


        self.input_search_student_attendance_button = By.CSS_SELECTOR, '[data-test-id="input-search-student-attendance"]'

        self.program_filter_button = By.CSS_SELECTOR, '[data-test-id="select-program"]'

        self.rows_per_page_button = By.CSS_SELECTOR, '[data-test-id="select-rows-per-page"]'

        self.next_page_button = By.CSS_SELECTOR, '[data-test-id="btn-next-page"]'
        self.previous_page_button = By.CSS_SELECTOR, '[data-test-id="btn-previous-page"]'

        self.rows_per_page_50 = By.CSS_SELECTOR, '[]'
        self.rows_per_page_100 = By.CSS_SELECTOR, '[]'
        self.rows_per_page_150 = By.CSS_SELECTOR, '[]'
