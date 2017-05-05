class ParserBuilder(object):
    def __init__(self):
        self.language = ''
        self.region = ''
        self.years_experience = ''

    def set_language(self, language):
        self.language = language
        return self

    def set_region(self, region):
        self.region = region
        return self

    def set_years_experience(self, years_experience):
        self.years_experience = years_experience
        return self