import time
from behave import *

@given('I am on the home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    # time.sleep(2)

@when('I click on "{Featured_Product}" button')
def step_impl(context, Featured_Product):
    context.home_page.click_on_Featured_Products_Item(Featured_Product)   #da click pe fiecare produs din zona Featured Products
    # time.sleep(2)

@then('I should access "{Featured_Product_Item}" webpage')
def step_impl(context, Featured_Product_Item):
    context.home_page.get_Product_Name()
    # actual_Product_Item_Name = context.home_page.get_Product_Name()
    # assert actual_Product_Item_Name == Featured_Product_Item, f'{Featured_Product_Item} product item was expected. Actual product item: {actual_Product_Item_Name}'
