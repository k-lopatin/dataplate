import re
from collector.modules.hh.vacancy.parser import VacanciesParser
from collector.modules.core.parser import AbstractParser


class Parser(AbstractParser):
    salaries = []

    def __init__(self, builder):
        self.builder = builder

    def make_start_link(self):
        return "http://hh.ru/search/vacancy?" \
               "text=%s" \
               "&only_with_salary=true" \
               "&experience=%s" \
               "&area=%s" \
               "&enable_snippets=true&clusters=true&salary=" % \
               (self.builder.language, self.builder.years_experience, self.builder.region)

    def make_page_num_link(self, page_num):
        return self.make_start_link() + "page=%d" % page_num

    def run(self):
        start_link = self.make_start_link()
        current_page = self.get_page_by_link(start_link)
        self.process_page(current_page)
        self.go_through_pages(current_page)
        print(self.salaries)
        print(len(self.salaries))

    def go_through_pages(self, page):
        max_num = self.get_max_page_num(page)
        for page_num in range(2, max_num):
            self.process_page_by_num(page_num)

    def process_page_by_num(self, page_num):
        curr_page_link = self.make_page_num_link(page_num)
        curr_page = self.get_page_by_link(curr_page_link)
        self.process_page(curr_page)

    def process_page(self, page):
        vacancies_parsers = VacanciesParser(page)
        self.salaries.extend(vacancies_parsers.run())

    def get_max_page_num(self, page):
        search = re.findall('"HH-Pager-Control".*>(\d*)</a>', page)
        found_num = int(search[-1])
        if found_num > 1:
            return found_num
        return 1


