from browser import Browser
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.register_page import RegisterPage


# aceasta metoda se va apela inainte de executarea tuturor testelor
def before_all(context):
    context.Browser = Browser()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.base_page = BasePage()


# aceasta metoda se va apela dupa executarea tuturor testelor
def after_all(context):
    context.Browser.quit()  # inchidem browser-ul apeland metoda quit (declarata in browser.py)





