class Group_Navigation_Process:
    def __init__(self, Groups_of_2025_2026_page):  # Accept instance of Login_Page
        self.Groups_of_2025_2026_page = Groups_of_2025_2026_page

    def run_group_process(self):
        self.Groups_of_2025_2026_page.navigate_to_table()
        # self.Groups_of_2025_2026_page.interact_with_table_elements()
        # self.Groups_of_2025_2026_page.mark_unmark_all_elements()
        # self.Groups_of_2025_2026_page.search_name_or_ID()
        # self.Groups_of_2025_2026_page.program_filter()
        self.Groups_of_2025_2026_page.rows_per_page()
        # self.Groups_of_2025_2026_page.navigate_all_pages()
