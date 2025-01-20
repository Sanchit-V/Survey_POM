from Import_Libraries import Import_libraries
By = Import_libraries.By

class question_creation:
    def __init__(self, driver):
        self.driver = Import_libraries.driver
        self.home_page = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[1]/div/div[1]"
        self.questions_page = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[2]/div/div[1]"
        self.close_opened_surveys = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/button/svg"
        self.create_questions = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/button"

        self.question_Type_Button = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/div"
        self.scale1to3 = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
        self.scale1to4 = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"
        self.scale1to5 = By.XPATH, "/html/body/div[4]/div[3]/ul/li[3]"
        self.scale1to7 = By.XPATH, "/html/body/div[4]/div[3]/ul/li[4]"
        self.YorN = By.XPATH, "/html/body/div[4]/div[3]/ul/li[5]"
        self.TorF = By.XPATH, "/html/body/div[4]/div[3]/ul/li[6]"
        self.GorB = By.XPATH, "/html/body/div[4]/div[3]/ul/li[7]"
        self.Text = By.XPATH, "/html/body/div[4]/div[3]/ul/li[8]"

        self.abbreviation = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"

        self.question = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/div/div/textarea[1]"

        self.Create = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
        self.Cancel = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[1]"








