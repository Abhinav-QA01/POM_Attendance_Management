class Group_Navigation_Process:
    def __init__(self, Groups_of_2025_2026_page):  # Accept instance of Login_Page
        self.Groups_of_2025_2026_page = Groups_of_2025_2026_page

    def run_group_process(self):
        self.Groups_of_2025_2026_page.navigate_to_table()
