from Import_Libraries import Import_libraries
By = Import_libraries.By

class LoginPage:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
        # self.Language_Button = By.CSS_SELECTOR, '[data-test-id="select-translation-language"]'
        # self.English_Button = By.CSS_SELECTOR, '[data-test-id="text-language-option-en_US"]'
        # self.Spanish_Button = By.CSS_SELECTOR, '[data-test-id="text-language-option-es_ES"]'
        # self.Portuguese_Button = By.CSS_SELECTOR, '[data-test-id="text-language-option-pt_BR"]'
        # self.Sign_In = By.CSS_SELECTOR, '[data-test-id="text-google-signin"]'

        self.Language_Button = By.XPATH, "//div[@id='translation-select']"
        self.Spanish_Button = By.XPATH, "//span[normalize-space()='Spanish']"
        self.English_Button = By.XPATH, "//span[normalize-space()='Inglés']"
        self.Portuguese_Button = By.XPATH, "//span[normalize-space()='Portugués']"

        self.Sign_In = By.XPATH, "//span[@class='MuiTypography-root MuiTypography-paragraphMd css-9uht4d']"




