import unittest
from collector.modules.github.repository import RepositoryService


class TestRepository(unittest.TestCase):

    def test_branches(self):
        branches = (RepositoryService('k-lopatin', 'dataplate')
                    .fetch_branches().branches)
        self.assertGreater(len(branches), 1, 'Too few branches')
