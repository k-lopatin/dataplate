import github3


class RepositoryService(object):

    owner = ''
    repo_name = ''

    repository = None

    branches = []
    issues = []

    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name
        self.repository = github3.repository(self.owner, self.repo_name)

    def fetch_branches(self):
        branches = self.repository.iter_branches()
        for branch in branches:
            self.branches.append(branch)
        return self

    def fetch_issues(self):
        issues = self.repository.iter_issues()
        for issue in issues:
            self.issues.append(issue)
            print(issue.body)
        return self