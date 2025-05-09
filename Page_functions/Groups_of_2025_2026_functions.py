import random
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Page_Object.Groups_of_2025_2026_page import Group_2025_2026
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# import tagui as t
# import rpa as r
# r.init()
import pyautogui

class Group_2025_2026_Function(Group_2025_2026):
    def navigate_to_table(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
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
        time.sleep(1)

    def interact_with_table_elements(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="td-session-cell-1-1"]')
            )
        )

        for x in range(1, 10):
            for y in range(1, 3):
                sem_2_table_element_path = f'[data-test-id="td-session-cell-{y}-{x}"]'
                sem_2_table_element = self.driver.find_element(By.CSS_SELECTOR, sem_2_table_element_path)
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        sem_2_table_element
                    )
                )
                sem_2_table_element.click()
                time.sleep(1)

                span_element = sem_2_table_element.find_element(By.XPATH,".//p//div//span[starts-with(@data-test-id, 'icon-selected-attendance-')]")
                test_id = span_element.get_attribute("data-test-id")
                # print(test_id)
                if test_id and test_id.startswith("icon-selected-attendance-"):
                    # Extract state from data-test-id
                    state = test_id.replace("icon-selected-attendance-", "")

                    # Perform actions based on the state
                    if state == "Justified":
                        # print("Button is in Justified state.")
                        delete_button = self.driver.find_element(*self.delete_justification_button)

                        delete_button.click()
                        time.sleep(1)
                        confirm_delete_justification_element = self.driver.find_element(*self.confirm_delete_justification_button)
                        confirm_delete_justification_element.click()
                        print("Justification Deleted")
                    else:
                        # print(f"Button is not in justified state")
                        arr = [1, 2, 3, 4, 5]  # 1 : Attendance, 2: Lateness, 3 : Absence, 4 : Release, 5 : Unmark
                        random_element = random.choice(arr)
                        # print(random_element)
                        try:
                            if random_element == 1:
                                present_button_element = self.driver.find_element(*self.present_button)
                                present_button_element.click()
                                time.sleep(1)
                                print("Attendance Marked")

                            elif random_element == 2:
                                late_button_element = self.driver.find_element(*self.late_button)
                                late_button_element.click()
                                time.sleep(1)
                                print("Lateness Marked")
                                print("Uploading file")
                                sem_2_table_element.click()
                                time.sleep(1)
                                justify_late_button = self.driver.find_element(*self.justify_late_button)
                                justify_late_button.click()

                                file_uploader_button = self.driver.find_element(*self.file_uploader_element)
                                file_uploader_button.click()
                                time.sleep(2)

                                pyautogui.write('"C:\\Users\\abhin\\Downloads\\just_s2s6_TYE027_1843560972_20250402 (1).docx"')
                                pyautogui.press('enter')


                                file_upload_confirm_button = self.driver.find_element(*self.file_upload_confirm_button)
                                WebDriverWait(self.driver,20).until(
                                    EC.element_to_be_clickable(file_upload_confirm_button)
                                )

                                file_upload_confirm_button.click()
                                time.sleep(5)
                            elif random_element == 3:
                                absence_button_element = self.driver.find_element(*self.absence_button)
                                absence_button_element.click()
                                time.sleep(1)
                                print("Absence Marked")

                            elif random_element == 4:
                                release_button_element = self.driver.find_element(*self.release_button)
                                release_button_element.click()
                                time.sleep(1)
                                print("Release Marked")

                            elif random_element == 5 and state in ("Attendance", "Lateness", "Absence", "Release"):
                                unmark_button_element = self.driver.find_element(*self.unmark_button)
                                unmark_button_element.click()
                                time.sleep(1)
                                print("Unmarked")

                            elif random_element == 5:
                                present_button_element = self.driver.find_element(*self.present_button)
                                present_button_element.click()
                                time.sleep(1)
                                print("Present Marked")

                            else:
                                print("The element doesn't exist")
                        except:
                            print("Student is disabled")

    # # def mark_unmark_all_elements(self):
    #     WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(
    #             (By.CSS_SELECTOR, '[data-test-id="btn-open-Session 1-menu"]')
    #         )
    #     )
    #     for x in range(1,10):
    #         more_options_button_path = f'[data-test-id="btn-open-Session {x}-menu"]'
    #         more_options_button = self.driver.find_element(By.CSS_SELECTOR, more_options_button_path)
    #         more_options_button.click()
    #         time.sleep(1)
    #         mark_all_as_button_element = self.driver.find_element(*self.mark_all_as_button)
    #         mark_all_as_button_element.click()
    #         time.sleep(1)
    #         arr = [1, 2, 3, 4, 5]  # 1 : Attendance, 2: Lateness, 3 : Absence, 4 : Release, 5 : Unmark
    #         random_element = random.choice(arr)

    #         if random_element == 1:
    #             mark_all_attendance_button = self.driver.find_element(*self.mark_all_attendance)
    #             mark_all_attendance_button.click()
    #             time.sleep(1)
    #         elif random_element == 2:
    #             mark_all_lateness_button = self.driver.find_element(*self.mark_all_lateness)
    #             mark_all_lateness_button.click()
    #             time.sleep(1)
    #         elif random_element == 3:
    #             mark_all_absence_button = self.driver.find_element(*self.mark_all_absence)
    #             mark_all_absence_button.click()
    #             time.sleep(1)
    #         elif random_element == 4:
    #             mark_all_release_button = self.driver.find_element(*self.mark_all_release)
    #             mark_all_release_button.click()
    #             time.sleep(1)
    #         elif random_element == 5:
    #             unmark_all_button = self.driver.find_element(*self.unmark_all)
    #             unmark_all_button.click()
    #             time.sleep(1)
    #         # print(random_element)

    # def session_edit(self):
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located(
        #         (By.CSS_SELECTOR, '[data-test-id="btn-open-Session 1-menu"]')
        #     )
        # )
        # for x in range(1,10):
        #     more_options_button_path = f'[data-test-id="btn-open-Session {x}-menu"]'
        #     more_options_button = self.driver.find_element(By.CSS_SELECTOR, more_options_button_path)
        #     more_options_button.click()
        #     time.sleep(1)
        #     print("Session Edit")

        #     edit_this_session_button_element = self.driver.find_element(*self.edit_this_session)
        #     edit_this_session_button_element.click()
        #     time.sleep(1)

        #     arr = [1,2]
        #     random_element = random.choice(arr)
        #     if random_element ==1:
        #         session_type_option_1_button_element = self.driver.find_element(*self.session_type_option_1_button)
        #         session_type_option_1_button_element.click()
        #         print("Session type changed to Theoritical/Pracitcal")
        #     else:
        #         session_type_option_2_button_element = self.driver.find_element(*self.session_type_option_2_button)
        #         session_type_option_2_button_element.click()
        #         print("Session type changed to Practical")

        #     number_of_hours_button = self.driver.find_element(*self.number_of_hours_field)
        #     number_of_hours_button.click()
        #     number_of_hours_button.clear()
        #     random_number = random.randint(1, 5)
        #     number_of_hours_button.send_keys(str(random_number))
        #     print("Number of hours changed")

    def search_name_or_ID(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="td-session-cell-1-1"]')
            )
        )

        search_field = self.driver.find_element(*self.input_search_student_attendance_button)
        search_field.click()
        search_field.clear()

        user_names_array = ["Barron Solis", "Bryant Kidd", "Dale Chan", "Wiggins Faith", "Woodward Petra"]
        random_user_name = random.choice(user_names_array)
        search_field.send_keys(random_user_name)
        time.sleep(2)
        print("Search name or ID")


        user_name_check = random_user_name.replace(" ", ", ")
        WebDriverWait(self.driver, 7).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), user_name_check)
        )
        time.sleep(2)


        search_field.send_keys(Keys.CONTROL, "a")  # Select all text
        search_field.send_keys(Keys.DELETE)
        print("Search name or ID")

        user_id_array = ["2025010183848", "2025010197463", "2025010139740", "2025010101991"]
        random_user_id = random.choice(user_id_array)

        search_field.send_keys(random_user_id)
        time.sleep(2)
        WebDriverWait(self.driver, 7).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), random_user_id)
        )
        time.sleep(1)

        search_field.send_keys(Keys.CONTROL, "a")  # Select all text
        search_field.send_keys(Keys.DELETE)
        time.sleep(3)

    # # def program_filter(self):
    #     WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(
    #             (By.CSS_SELECTOR, '[data-test-id="td-session-cell-1-1"]')
    #         )
    #     )
    #     program_filter_button = self.driver.find_element(*self.program_filter_button)
    #     program_filter_button.click()
    #     WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(
    #             (By.CSS_SELECTOR, '[data-test-id="icon-search"]')
    #         )
    #     )
    #     print("Program filter")

    #     """
    #     Select a random number of program options.

    #     Args:
    #         num_selections: Number of program options to select randomly

    #     Returns:
    #         List of selected program names
    #     """
    #     try:
    #         # Wait for dropdown menu items to be visible
    #         WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-test-id^='li-program-']"))
    #         )

    #         # Find all program options
    #         program_options = self.driver.find_elements(By.CSS_SELECTOR, "li[data-test-id^='li-program-']")
    #         print(f"Found {len(program_options)} program options")

    #         if not program_options:
    #             print("No program options found")
    #             return []
    #         num_selections = 3
    #         # Determine how many options to select (don't try to select more than available)
    #         num_to_select = min(num_selections, len(program_options))

    #         # Select random options without repeating
    #         selected_indices = random.sample(range(len(program_options)), num_to_select)
    #         selected_names = []
    #         print("Selecting 3 random programs")
    #         # Click each selected option
    #         for index in selected_indices:
    #             program = program_options[index]
    #             program_name = program.text

    #             # Check if the checkbox is already selected (optional)
    #             checkbox = program.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    #             if not checkbox.is_selected():
    #                 # Click on the program option to select it
    #                 program.click()
    #                 print(f"Selected program: {program_name}")
    #                 # Small delay between selections to avoid race conditions
    #                 time.sleep(0.3)
    #             else:
    #                 print(f"Program already selected: {program_name}")

    #             selected_names.append(program_name)

    #         return selected_names
    #     except Exception as e:
    #         print(f"Error selecting random programs: {e}")
    #         return []

    def rows_per_page(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="select-rows-per-page"]')
            )
        )
        rows_per_page_button = self.driver.find_element(*self.rows_per_page_button)
        rows = int(rows_per_page_button.text)
        students = self.driver.find_elements(By.CSS_SELECTOR, "tr[data-test-id^='tr-student-data-']")
        total_number_of_students = len(students)
        if total_number_of_students <= rows:
            print("Number of rows in the page is valid according to rows_per_page filter")
        else:
            print("Number of rows in the page is invalid")
            self.driver.quit()
        rows_per_page_button.click()


        time.sleep(2)

    def is_clickable(self, locator):
        """Check if an element is clickable"""
        try:
            element = self.driver.find_element(*locator)
            return element.is_enabled() and element.is_displayed()
        except NoSuchElementException:
            return False

    def navigate_all_pages(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-test-id="td-session-cell-1-1"]')
            )
        )
        next_selector = self.driver.find_element(*self.next_page_button)
        previous_selector = self.driver.find_element(*self.previous_page_button)
        """Navigate through all pages - first forward, then backward"""
        # Phase 1: Click next page button until not clickable
        print("Starting forward navigation...")
        forward_count = 0

        while self.is_clickable(self.next_page_button):
            try:
                # Process current page if needed
                # process_current_page()

                # Click next button
                next_button = self.driver.find_element(*self.next_page_button)
                next_button.click()
                forward_count += 1
                print(f"Moved to next page ({forward_count})")
                time.sleep(2)

                # Simple wait for page to load
                WebDriverWait(self.driver, 20).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )

            except Exception as e:
                print(f"Error during forward navigation: {e}")
                break

        print(f"Forward navigation complete. Navigated through {forward_count} pages.")

        # Phase 2: Click previous page button until not clickable
        print("Starting backward navigation...")
        backward_count = 0

        while self.is_clickable(self.previous_page_button):
            try:
                # Process current page if needed
                # process_current_page()

                # Click previous button
                prev_button = self.driver.find_element(*self.previous_page_button)
                prev_button.click()
                backward_count += 1
                print(f"Moved to previous page ({backward_count})")
                time.sleep(2)

                # Simple wait for page to load
                WebDriverWait(self.driver, 20).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )

            except Exception as e:
                print(f"Error during backward navigation: {e}")
                break

        print(f"Backward navigation complete. Navigated through {backward_count} pages.")
        print(f"Total pages navigated: {forward_count + backward_count}")

        return {
            "forward": forward_count,
            "backward": backward_count,
            "total": forward_count + backward_count
        }