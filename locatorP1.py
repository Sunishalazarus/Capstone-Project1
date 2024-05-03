class WebLocators:

    def __init__(self):
        self.usernameLocator = "username"
        self.passwordLocator = "password"
        self.loginButtonLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
        self.topRightLocator = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span"
        self.logoutButtonLocator = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
        self.errorMessageLocator = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]"
