import unittest
from collector.modules.github.search import SearchService


class TestSearch(unittest.TestCase):
    def test_search_not_null(self):
        found_repos = SearchService('test').search_repositories().found_repos
        repos_count = 0
        for repo in found_repos:
            repos_count += 1
            self.assertIsNotNone(repo, 'Found repo is null')
        self.assertEqual(repos_count, 5)
