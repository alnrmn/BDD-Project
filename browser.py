from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()
