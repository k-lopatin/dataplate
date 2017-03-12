from config.service import ConfigService


class AuthService:
    config_service = ConfigService()
    login = ''
    password = ''

    def __init__(self):
        try:
            self.get_credentials_from_config()
        except KeyError:
            self.create_config()

    def get_credentials_from_config(self):
        self.login = self.config_service.get('collector', 'github', 'auth', 'login')
        self.password = self.config_service.get('collector', 'github', 'auth', 'password')

    def set_credentials_to_config(self):
        parameters = {'login': self.login, 'password': self.password}
        self.config_service.set('collector', 'github', 'auth', parameters)

    def login_from_console(self):
        print('It seems that there is no config file with authorization information')
        print('Please, enter your credentials on github')
        self.login = input('Login: ')
        self.password = input('Password: ')

    def create_config(self):
        self.login_from_console()
        self.set_credentials_to_config()



