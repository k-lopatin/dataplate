"""
Performs search for repositories on github.com
"""
import github3


class SearchService(object):
    """
    Performs search for repositories on github.com
    """

    search_word = ''
    results_number = 5

    found_repos = []

    def __init__(self, search_word):
        self.search_word = search_word

    def set_results_number(self, number):
        self.results_number = number
        return self

    def search_repositories(self):
        self.found_repos = github3.search_repositories(self.search_word, number=self.results_number)
        return self
