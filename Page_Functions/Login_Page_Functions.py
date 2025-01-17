from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Import_Libraries import Import_libraries
By = Import_libraries.By
from Page_Objects.Login_Page import LoginPage

class Login_Page(LoginPage):

    def select_language(self, selected_language):
        if selected_language == 0:
            selected_language_button = self.driver.find_element(*self.Language_Button)
            selected_language_button.click()
            time.sleep(2)
            try:
                english_button = self.driver.find_element(*self.English_Button)
                english_button.click()
                time.sleep(1)

            except Exception as e:
                print("Error or already selected")
                print(f"Logs-->{e}")

        elif selected_language == 1:
            selected_language_button = self.driver.find_element(*self.Language_Button)
            selected_language_button.click()
            time.sleep(2)
            try:
                portuguese_button = self.driver.find_element(*self.Portuguese_Button)
                portuguese_button.click()
                time.sleep(1)

            except Exception as e:
                print("Error or already selected")
                print(f"Logs-->{e}")

        else:
            print('Spanish already selected.')

    def sign_in(self):
        sign_in_button = self.driver.find_element(*self.Sign_In)
        sign_in_button.click()
        time.sleep(2)

    def google_sign_in(self, google_account, google_password):
        main_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        # Get all window handles and switch to the new one
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        )
        email_field.send_keys(google_account)
        time.sleep(2)

        self.driver.find_element(By.ID, "identifierNext").click()


        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        password_field.send_keys(google_password)
        time.sleep(2)

        show_password_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']"))
        )
        if not show_password_checkbox.is_selected():
            show_password_checkbox.click()

        time.sleep(2)

        self.driver.find_element(By.ID, "passwordNext").click()
        time.sleep(1)
        self.driver.switch_to.window(main_window)
        print("Successfully switched back to the main window.")
        time.sleep(4)













