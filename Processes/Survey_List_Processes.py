class Survey_list:
    def __init__(self, survey_list):
        self.survey_list = survey_list

    def run_process(self, Survey_Name, Abbreviation, Category, Modality, Language):
        self.survey_list.Create_survey()
        self.survey_list.survey_name(Survey_Name)
        self.survey_list.survey_abbreviation(Abbreviation)
        self.survey_list.category_section(Category)
        self.survey_list.modality_section(Modality)
        self.survey_list.language_selection(Language)
        self.survey_list.create_survey()
