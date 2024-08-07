import time
from behave import *


@when('I click on the "{Poll_Answer}" poll button')
def step_impl(context, Poll_Answer):
    context.home_page.click_Poll_Answer_Item(Poll_Answer)
    time.sleep(2)

@when('I click on the Vote button')
def step_impl(context):
    context.home_page.click_Vote_Button()
    time.sleep(2)

@then('I should see a voting error message')
def step_impl(context):
    actual_error_message = context.home_page.get_poll_error_message()
    expected_error_message = 'Only registered users can vote.'
    assert expected_error_message in actual_error_message