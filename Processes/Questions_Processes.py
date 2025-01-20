class Questions_page:
    def __init__(self, questions_page):
        self.questions_page = questions_page

    def run_process(self, question_types, ques_abbreviation, ques):
        self.questions_page.main_page()
        #self.questions_page.close_opened()
        self.questions_page.questions_Page()
        self.questions_page.create_question()
        self.questions_page.question_type(question_types)
        self.questions_page.abbreviations(ques_abbreviation)
        self.questions_page.question_text(ques)
        self.questions_page.create()




