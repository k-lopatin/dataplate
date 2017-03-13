from collector.modules.github.auth import AuthService


class Base:
    github_obj = None

    def __init__(self):
        auth_service = AuthService()
        self.github_obj = auth_service.authorize()
