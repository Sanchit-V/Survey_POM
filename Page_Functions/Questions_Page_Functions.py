from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Import_Libraries import Import_libraries

By = Import_libraries.By

from Page_Objects.Questions import question_creation

class question_Creation(question_creation):
    def main_page(self):
        main_page_button = self.driver.find_element(*self.home_page)
        main_page_button.click()
        time.sleep(2)

    def close_opened(self):
        close_button = self.driver.find_element(*self.close_opened_surveys)
        close_button.click()
        time.sleep(2)

    def questions_Page(self):
        questions_page_button = self.driver.find_element(*self.questions_page)
        questions_page_button.click()
        time.sleep(2)

    def create_question(self):
        create_question_button = self.driver.find_element(*self.create_questions)
        create_question_button.click()
        time.sleep(1)

    def question_type(self, question_types):
        ques_type_button = self.driver.find_element(*self.question_Type_Button)
        ques_type_button.click()
        time.sleep(1)

        if question_types == 1:
            scale_1to3 = self.driver.find_element(*self.scale1to3)
            scale_1to3.click()
            time.sleep(2)
        elif question_types == 2:
            scale_1to4 = self.driver.find_element(*self.scale1to4)
            scale_1to4.click()
            time.sleep(2)
        elif question_types == 3:
            scale_1to5 = self.driver.find_element(*self.scale1to5)
            scale_1to5.click()
            time.sleep(2)
        elif question_types == 4:
            scale_1to7 = self.driver.find_element(*self.scale1to7)
            scale_1to7.click()
            time.sleep(2)
        elif question_types == 5:
            YesorNo = self.driver.find_element(*self.YorN)
            YesorNo.click()
            time.sleep(2)
        elif question_types == 6:
            TrueorFalse = self.driver.find_element(*self.TorF)
            TrueorFalse.click()
            time.sleep(2)
        elif question_types == 7:
            GoodorBad = self.driver.find_element(*self.GorB)
            GoodorBad.click()
            time.sleep(2)
        elif question_types == 8:
            Text = self.driver.find_element(*self.Text)
            Text.click()
            time.sleep(2)
        else:
            print('Correct option not chosen')

    def abbreviations(self, ques_abbreviation):
        abbreviations = self.driver.find_element(*self.abbreviation)
        abbreviations.click()
        time.sleep(1)
        abbreviations.send_keys(ques_abbreviation)
        time.sleep(2)

    def question_text(self, ques):
        questions = self.driver.find_element(*self.question)
        questions.click()
        time.sleep(1)
        questions.send_keys(ques)
        time.sleep(2)

    def create(self):
        create_button = self.driver.find_element(*self.Create)
        create_button.click()
        time.sleep(2)
















