import configparser

class ReadConfig:
    config = configparser.RawConfigParser()
    config.read("Configuration/config.ini")  # Ensure the path is correct

    @staticmethod
    def getapplicationurl():
        return ReadConfig.config.get('common info', 'baseurl')  # Return URL

    @staticmethod
    def getapplicationusername():
        return ReadConfig.config.get('common info', 'username')  # Return username

    @staticmethod
    def getapplicationpassword():
        return ReadConfig.config.get('common info', 'password')  # Return password
