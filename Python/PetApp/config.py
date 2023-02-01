#Configuartion file for PetApp. In the config fil, just put key value pairs such as : table_name = 'pets_regs1' and then in the app.py file, import config and use config.table_name to get the value of the key table_name. This is a good way to keep your code clean and easy to read.

#Also make logger file and put it in the same folder as the app.py file. Then import logger and use logger.info("message") to log messages to the log file.

class Config:
    def __init__(self):
        self.table_name = "pets_regs1"
        self.dbanme = "Flask_things"
        self.userDB = "postgres"
        self.passwordDB = "Finserv@2023"
        self.secretKey = "01hashSecretKey10"
        # self.homepageFlename = "homepage.html"
        # self.viewFilename = "view.html"
        # self.viewRoute = "/view"

    def table(self):
        return self.table_name

    def db(self):
        return self.dbanme

    def user(self):
        return self.userDB

    def password(self):
        return self.passwordDB

    def secret(self):
        return self.secretKey

    # def homepage(self):
    #     return self.homepageFlename

    # def view(self):
    #     return self.viewFilename

    # def viewR(self):
    #     return self.viewRoute
