from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Import_Libraries import Import_libraries

By = Import_libraries.By

from Page_Objects.Survey_List import SurveyList

class Survey_List(SurveyList):
    def Create_survey(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/button"))
        )
        time.sleep(1)
        create_survey = self.driver.find_element(*self.Create_Survey)

        create_survey.click()
        time.sleep(1)

    def survey_name(self, Survey_Name):
        survey_name = self.driver.find_element(*self.Survey_name)
        survey_name.click()
        time.sleep(2)
        survey_name.send_keys(Survey_Name)
        time.sleep(1)

    def survey_abbreviation(self, Abbreviation):
        survey_abb = self.driver.find_element(*self.abbreviation)
        survey_abb.click()
        time.sleep(2)
        survey_abb.send_keys(Abbreviation)
        time.sleep(1)

    def category_section(self, Category):
        category = self.driver.find_element(*self.Category)
        category.click()
        time.sleep(1)

        if Category == 0:
            SSTP = self.driver.find_element(*self.SSTP)
            SSTP.click()
            print('SSTP Selected')

        elif Category == 1:
            SSAC = self.driver.find_element(*self.SSAC)
            SSAC.click()
            print('SSAC Selected')

        else:
            print('No option selected.')

        time.sleep(2)

    def modality_section(self, Modality):
        modality = self.driver.find_element(*self.Modality)
        modality.click()
        time.sleep(1)
        in_Person = self.driver.find_element(*self.In_Person)
        virtual = self.driver.find_element(*self.Virtual)

        if Modality == 0:
            in_Person.click()
            time.sleep(1)
            print('In-Person Selected')

        elif Modality == 1:
            virtual.click()
            time.sleep(1)
            print('Virtual Selected')

        elif Modality == 2:
            in_Person.click()
            time.sleep(1)
            virtual.click()
            time.sleep(1)
            print('Both Selected')

        else:
            print('Nothing Selected')

        time.sleep(1)
        self.driver.find_element(*self.Open_Xpath).click()


    def language_selection(self, Language):
        language = self.driver.find_element(*self.Language)
        language.click()
        time.sleep(1)

        spanish = self.driver.find_element(*self.Spanish_Option)
        english = self.driver.find_element(*self.English_Option)
        portuguese = self.driver.find_element(*self.Portuguese_Option)
        italian = self.driver.find_element(*self.Italian_Option)
        french = self.driver.find_element(*self.French_Option)
        chinese = self.driver.find_element(*self.Chinese_Option)

        if Language == 0:
            spanish.click()
            time.sleep(1)
            print("Spanish selected")

        elif Language == 1:
            english.click()
            time.sleep(1)
            print("English selected")

        elif Language == 2:
            portuguese.click()
            time.sleep(1)
            print("Portuguese selected")

        elif Language == 3:
            italian.click()
            time.sleep(1)
            print("French selected")

        elif Language == 4:
            french.click()
            time.sleep(1)
            print("French selected")

        elif Language == 5:
            chinese.click()
            time.sleep(1)
            print("Chinese selected")

    def create_survey(self):
        create_button = self.driver.find_element(*self.Create)
        create_button.click()
        time.sleep(2)






