class Version_menu:
    def __init__(self, version_menu):
        self.version_menu = version_menu

    def run_process(self, version_name, version_abbreviation, mandatory_button):
        self.version_menu.empty_template(version_name, version_abbreviation, mandatory_button )
