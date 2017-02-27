import github3


class RepositoryService(object):

    owner = ''
    repo_name = ''

    repository = None

    branches = []

    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name
        self.repository = github3.repository(self.owner, self.repo_name)

    def fetch_branches(self):
        branches = self.repository.iter_branches()
        for branch in branches:
            self.branches.append(branch)
        return self
