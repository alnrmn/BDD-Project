from selenium.webdriver.common.by import By
from browser import Browser


class BasePage(Browser):

    def get_element_by_link_text(self, text):
        return self.driver.find_element(By.LINK_TEXT, text)

