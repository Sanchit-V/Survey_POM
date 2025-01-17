from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Import_Libraries import Import_libraries
from user_details import Version_Options

By = Import_libraries.By
from Page_Objects.Version_Menu import VersionSelection

class Version_Selection(VersionSelection):
    if Version_Options == 0:
        def empty_template(self, version_name, version_abbreviation, mandatory_button):
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/button/text()")))

            Empty_Template = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div")
            Empty_Template.click()
            time.sleep(2)

            Continue_Version = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]")
            Continue_Version.click()
            time.sleep(2)


            Version_Name = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/input")
            Version_Name.click()
            time.sleep(2)
            Version_Name.send_keys(version_name)
            time.sleep(3)

            Version_Abbreviation = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input")
            Version_Abbreviation.click()
            time.sleep(2)
            Version_Abbreviation.send_keys(version_abbreviation)
            time.sleep(3)

            Mandatory_radio = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/label/span[1]/span[1]/input")

            if mandatory_button == 1:
                Mandatory_radio.click()
                time.sleep(2)

            elif mandatory_button == 0:
                print("Skipped, cause not mandatory was not selected.")

            else:
                print("Wrong option selected.")

            Accept_Button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[3]")
            Accept_Button.click()
            time.sleep(4)













