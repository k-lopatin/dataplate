import re
from collector.modules.hh.vacancy.vacancy import Vacancy


class VacanciesParser(object):
    def __init__(self, page):
        self.page = page

    def run(self):
        salaries = []
        for sal_text in self.find_all_salaries_on_page():
            salary = self.find_salary(sal_text)
            salaries.append(salary)
        return salaries

    def find_all_salaries_on_page(self):
        return re.findall('itemprop="salaryCurrency"(.*?)</div>', self.page)

    def find_salary(self, salary_text):
        search = re.findall('"baseSalary" content="(\d*)"', salary_text)
        return search[0]

