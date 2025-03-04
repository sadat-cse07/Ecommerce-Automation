import configparser

config = configparser.RawConfigParser()

config.read(".\\configuration\\config.ini")


class Read_config:

    @staticmethod
    def login_url():
        url = config.get("login info", 'page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get("login info", 'textbox_username')
        return username

    @staticmethod
    def get_password():
        password = config.get("login info", 'textbox_password')
        return password

    @staticmethod
    def get_invalid_user():
        invalid_users = config.get("login info", 'invalid_user')
        return invalid_users
