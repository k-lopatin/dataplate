from config.service import ConfigService
from github3 import login


class AuthService:
    config_service = ConfigService()
    login = ''
    password = ''

    def __init__(self):
        try:
            self.__get_credentials_from_config()
        except KeyError:
            self.__create_config()

    def __get_credentials_from_config(self):
        self.login = self.config_service.get('collector', 'github', 'auth', 'login')
        self.password = self.config_service.get('collector', 'github', 'auth', 'password')

    def __set_credentials_to_config(self):
        parameters = {'login': self.login, 'password': self.password}
        self.config_service.set('collector', 'github', 'auth', parameters)

    def __login_from_console(self):
        print('It seems that there is no config file with authorization information')
        print('Please, enter your credentials on github')
        self.login = input('Login: ')
        self.password = input('Password: ')

    def __create_config(self):
        self.__login_from_console()
        self.__set_credentials_to_config()

    def authorize(self):
        g = login(self.login, self.password)
        return g
