import github3
from collector.modules.github.base import Base


class UserService(Base):
    user_login = ''
    user = None

    def __init__(self, user_login):
        super().__init__()
        self.user_login = user_login
        self.user = self.github_obj.user(self.user_login)

    def get_public_repos(self):
        print(self.user.repos_url)
        return self.user.repos_url

    def get_commits(self):
        for repo in self.get_repos():
            for commit in repo.iter_commits(author=self.user_login, number=1):
                print(commit.commit.message)

    def get_repos(self):
        return github3.iter_user_repos(self.user_login)

    def get_commits_by_interval(self, start_date, end_date):
        for repo in self.get_repos():
            print(repo)
            for commit in repo.iter_commits(author=self.user_login, since=start_date, until=end_date):
                print(commit.commit.message)
