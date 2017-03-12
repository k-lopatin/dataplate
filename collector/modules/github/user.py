import github3

class UserService:

    user_login = ''
    user = None

    def __init__(self, user_login):
        self.user_login = user_login
        self.user = github3.user(self.user_login)

    def get_public_repos(self):
        print(self.user.repos_url)
        return self.user.repos_url

    def get_commits(self):
        repos = github3.iter_user_repos(self.user_login)
        for repo in repos:
            print(repo)
            for commit in repo.iter_commits(author=self.user_login, number=1):
                print(commit.commit.message)

