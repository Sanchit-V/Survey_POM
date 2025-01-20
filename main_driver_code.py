import time
import Import_Libraries
import user_details
from Import_Libraries import Import_libraries
from Page_Functions.Login_Page_Functions import Login_Page
from Page_Functions.Questions_Page_Functions import question_Creation
from Page_Functions.Survey_List_Functions import Survey_List
from Page_Functions.Version_Menu_Functions import Version_Selection
from Processes.Login_Process import Login_Process
from Processes.Questions_Processes import Questions_page
from Processes.Survey_List_Processes import Survey_list
from Processes.Version_Menu_Processes import Version_menu
from user_details import Version_Options

# Initialize WebDriver
driver = Import_libraries.initialize_driver()

# Navigate to the URL
driver.get(user_details.url)
driver.maximize_window()

time.sleep(4)

login_page_functions = Login_Page(driver)
survey_functions = Survey_List(driver)
version_menu_functions = Version_Selection(driver)
create_questions_functions = question_Creation(driver)



def test_login_process():
    login_process = Login_Process(login_page_functions)
    login_process.run_process(user_details.selected_language, user_details.google_account, user_details.google_password)

def test_survey_processes():
    survey_processes = Survey_list(survey_functions)
    survey_processes.run_process(user_details.Survey_Name, user_details.Abbreviation, user_details.Category, user_details.Modality,user_details.Language)

def test_version_menu():
    version_menu_processes = Version_menu(version_menu_functions)
    version_menu_processes.run_process(user_details.version_name, user_details.version_abbreviation, user_details.mandatory_button)

def test_questions_creation():
    create_questions_processes = Questions_page(create_questions_functions)
    create_questions_processes.run_process(user_details.question_types,user_details.ques_abbreviation, user_details.ques)