from Import_Libraries import Import_libraries
By = Import_libraries.By

class SurveyList:
    def __init__(self ,driver):
        self.driver = Import_libraries.driver
        # self.Create_Survey = By.CSS_SELECTOR, '[data-test-id="btn-open-create-survey-dialog"]'
        # self.Survey_Name = By.CSS_SELECTOR, '[data-test-id="input-create-survey-name"]'
        # self.Abbreviation = By.CSS_SELECTOR, '[data-test-id="label-create-survey-abbreviation"]'
        # self.Category = By.CSS_SELECTOR, '[data-test-id="label-create-survey-category"]'
        #
        #
        #
        # self.Modality = By.CSS_SELECTOR, '[data-test-id="label-create-survey-modality"]'
        # self.In_Person = By.CSS_SELECTOR, '[data-test-id="text-create-survey-modality-select-input-option-in_person"]'
        # self.Virtual = By.CSS_SELECTOR, '[data-test-id="text-create-survey-modality-select-input-option-virtual"]'
        #
        #
        # self.Language = By.CSS_SELECTOR, '[data-test-id="label-create-survey-language"]'
        # self.Spanish_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-es_ES"]'
        # self.English_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-en_US"]'
        # self.Portuguese_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-pt_BR"]'
        # self.Italian_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-it_IT"]'
        # self.French_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-fr_FR"]'
        # self.Chinese_Option = By.CSS_SELECTOR, '[data-test-id="li-create-survey-language-option-zh_CN"]'


        # self.Cancel = By.CSS_SELECTOR, '[data-test-id="btn-cancel-create-survey"]'
        # self.Create = By.CSS_SELECTOR, '[data-test-id="btn-create-survey"]'

        self.Create_Survey = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/button"
        self.Survey_name = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/input"
        self.abbreviation = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"

        self.Category = By.XPATH, "//body[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]"
        self.SSTP = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
        self.SSAC = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"


        self.Modality = By.XPATH, "//body[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]"
        self.In_Person = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
        self.Virtual = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"
        self.Open_Xpath = By.XPATH, "/html/body/div[4]/div[1]"

        self.Language = By.XPATH, "//body[1]/div[3]/div[3]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]"
        self.Spanish_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
        self.English_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"
        self.Portuguese_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[3]"
        self.Italian_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[4]"
        self.French_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[5]"
        self.Chinese_Option = By.XPATH, "/html/body/div[4]/div[3]/ul/li[6]"

        self.Cancel = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[1]"
        self.Create = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
