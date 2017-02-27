import unittest
from collector.modules.github.search import SearchService


class TestSearch(unittest.TestCase):
    def test_search_not_null(self):
        found_repos = SearchService('test').search_repositories_lazy().found_lazy_repos
        repos_count = 0
        for repo in found_repos:
            repos_count += 1
            self.assertIsNotNone(repo, 'Found repo is null')
        self.assertEqual(repos_count, SearchService.results_number)

    def test_search_with_results_number(self):
        test_results_number = 1
        found_repos = (SearchService('test')
                       .set_results_number(test_results_number)
                       .search_repositories_lazy()
                       .found_lazy_repos)
        repos_count = 0
        for repo in found_repos:
            repos_count += 1
            self.assertIsNotNone(repo, 'Found repo is null')
        self.assertEqual(repos_count, test_results_number)

    def test_search_with_fetching(self):
        test_results_number = 1
        fetched_repos = (SearchService('test')
                         .set_results_number(test_results_number)
                         .search_repositories_lazy()
                         .fetch_found_lazy_repos()
                         .fetched_repos)
        self.assertEqual(len(fetched_repos), test_results_number, 'Fetched repos are not found')
