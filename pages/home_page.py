from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):


    FEATURED_PRODUCTS_ITEM_SELECTOR = (By.CSS_SELECTOR, "div[class='product-item']")
    ACTUAL_PRODUCT_NAME_SELECTOR = (By.CLASS_NAME, "product-name")
    POLL_ANSWER_ITEM_SELECTOR = (By.CSS_SELECTOR, "li.answer")
    VOTE_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button#vote-poll-1")
    POLL_ERROR_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "div.poll-vote-error")



    def navigate_to_home_page(self):
        self.driver.get('https://demo.nopcommerce.com/')


    def click_on_Featured_Products_Item(self,Featured_Products_Item):
        self.get_element_by_link_text(Featured_Products_Item).click()


    def get_Product_Name(self):
        elements = self.driver.find_elements(*self.ACTUAL_PRODUCT_NAME_SELECTOR)
        if elements:
            return elements[0].text  # Returnează textul primului element
        else:
            return None


    def click_Poll_Answer_Item(self, Poll_Answer):
        poll_options = self.driver.find_elements(*self.POLL_ANSWER_ITEM_SELECTOR) #cauta toate optiunile de vot
        #iteram prin toate optiunile gasite
        for option in poll_options:
            if Poll_Answer in option.text:  #verificam daca textul optiunii contine textul specificat in Poll_Answer (community_poll.feature file)
                option.click()  # daca textul este gasit
                break  #se opreste iteratia fiindca am gasit si am dat click pe optiunea dorita

    def click_Vote_Button(self):
        self.driver.find_element(*self.VOTE_BUTTON_SELECTOR).click()

    def get_poll_error_message(self):
        return self.driver.find_element(*self.POLL_ERROR_MESSAGE_SELECTOR).text