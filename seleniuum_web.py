from selenium import webdriver

class infow():
    def _init_(self):
        self.driver= webdriver.Chrome(executable_path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk')

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")

assist=infow()
assist.get_info("ram")