import time
from behave import *


@given('I am on the register page')
def step_impl(context):
    context.register_page.navigate_to_register_page()
    time.sleep(2)


@when('I fill in "{first_name}" in First Name field')
def step_impl(context, first_name):
    context.register_page.enter_first_name(first_name)
    time.sleep(2)


@when('I fill in "{last_name}" in Last Name field')
def step_imp(context, last_name):
    context.register_page.enter_last_name(last_name)
    time.sleep(2)


@when('I leave blank the Last Name field')
def step_impl(context):
    pass


@when('I fill in "{email}" in Email field')
def step_impl(context, email):
    context.register_page.enter_email_address(email)
    time.sleep(2)


@when('I fill in "{password}" in Password field')
def step_impl(context, password):
    context.register_page.enter_password(password)
    time.sleep(2)


@when('I fill in "{confirm_password}" in Confirm password field')
def step_impl(context, confirm_password):
    context.register_page.confirm_password(confirm_password)
    time.sleep(2)


@when('I click on the Register button')
def step_impl(context):
    context.register_page.click_register_button()
    time.sleep(2)


@then('I should see a registration confirmation message')
def step_impl(context):
    actual_registration_confirmation_message = context.register_page.get_registration_confirmation_message()
    expected_registration_confirmation_message = 'Your registration completed'
    assert actual_registration_confirmation_message in expected_registration_confirmation_message


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.register_page.get_lastname_error_message()  # contextul din register page al mesajului de eroare pentru LastName (atunci cand apare)
    expected_error_message = 'Last name is required.'
    assert expected_error_message in actual_error_message
