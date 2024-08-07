from selenium.webdriver.common.by import By
from browser import Browser


class RegisterPage(Browser):  # cream o pagina de Register cu Clasa RegisterPage ce mosteneste clasa Browser (import Browser)

    INSERT_FIRSTNAME_SELECTOR = (By.CSS_SELECTOR, "input#FirstName")
    INSERT_LASTNAME_SELECTOR = (By.CSS_SELECTOR, "[name=\"LastName\"]")
    INSERT_EMAIL_SELECTOR = (By.CSS_SELECTOR, "[name=\"Email\"]")
    INSERT_PASSWORD_SELECTOR = (By.CSS_SELECTOR, "[type=\"password\"]#Password")
    INSERT_CONFIRM_PASSWORD_SELECTOR = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON_SELECTOR = (By.CSS_SELECTOR, "button.register-next-step-button")
    LASTNAME_ERROR_MESSAGE_SELECTOR = (By.CSS_SELECTOR, "#LastName-error")
    REGISTRATION_CONFIRMATION_SELECTOR = (By.CSS_SELECTOR, "div.result")

    def navigate_to_register_page(self):  # functia pt navigarea pe pagina de register
        self.driver.get("https://demo.nopcommerce.com/register")

    def enter_first_name(self, first_name):
        first_name_element = self.driver.find_element(*self.INSERT_FIRSTNAME_SELECTOR).send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_element = self.driver.find_element(*self.INSERT_LASTNAME_SELECTOR).send_keys(last_name)
        pass

    def enter_email_address(self, email):
        email_element = self.driver.find_element(*self.INSERT_EMAIL_SELECTOR).send_keys(email)

    def enter_password(self, password):
        password_element = self.driver.find_element(*self.INSERT_PASSWORD_SELECTOR).send_keys(password)

    def confirm_password(self, confirm_password):
        confirm_password_element = self.driver.find_element(*self.INSERT_CONFIRM_PASSWORD_SELECTOR).send_keys(confirm_password)

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON_SELECTOR).click()

    def get_registration_confirmation_message(self):
        return self.driver.find_element(*self.REGISTRATION_CONFIRMATION_SELECTOR).text

    def get_lastname_error_message(self):
        return self.driver.find_element(*self.LASTNAME_ERROR_MESSAGE_SELECTOR).text
