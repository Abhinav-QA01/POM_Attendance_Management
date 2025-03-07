class Login_Process:
    def __init__(self, login_page):  # Accept instance of Login_Page
        self.login_page = login_page

    def run_process(self, username, password, language_selected):
        self.login_page.language_selection(language_selected)
        self.login_page.sign_in_with_google(username,password)
        # self.login_page.login(username,password)

