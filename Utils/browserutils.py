class BrowserUtils:           # Parent class for all other classes: Inheritence concept

    def __init__(self, driver):        # Constructor
        self.driver = driver



    def getTitle(self):
        return self.driver.title
