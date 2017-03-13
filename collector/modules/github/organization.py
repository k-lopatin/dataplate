import github3
from collector.modules.github.base import Base


class OrganizationService(Base):
    user_login = ''
    organization_name = ''

    def __init__(self, organization_name, user_login=''):
        super().__init__()
        self.organization_name = organization_name
        self.organization = self.github_obj.organization(self.organization_name)
        self.user_login = user_login

    def get_repos(self):
        return self.organization.iter_repos()

    # def get_commits(self):
    #     for repo in self.get_repos():
    #         for commit in repo.iter_commits(author=self.user_login, number=1):
    #             print(commit.commit.message)
    #
    # def get_repos(self):
    #     return github3.iter_user_repos(self.user_login)

    def get_commits_by_interval(self, start_date, end_date):
        for repo in self.get_repos():
            print(repo)
            for commit in repo.iter_commits(author=self.user_login, since=start_date, until=end_date):
                print(commit.commit.to_json())
        print(self.github_obj.rate_limit())
