class Login_Process:
    def __init__(self, login_page):
        self.login_page = login_page

    def run_process(self, selected_language, google_account, google_password):
        self.login_page.select_language(selected_language)
        self.login_page.sign_in()
        self.login_page.google_sign_in(google_account, google_password)
