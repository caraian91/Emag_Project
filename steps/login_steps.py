from behave import *

@when('login: I set my email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I set my password "{password}" and click Continua')
def step_impl(context, password):
    context.login_page.set_email(password)
    context.login_page.click_continua_btn()
    context.login_page.click_activeaza_mai_tarziu_btn()

@when('login: I click emag logo')
def step_impl(context):
    context.login_page.click_logo_img()

@then('login: I verify login page url')
def step_impl(context):
    context.login_page.verify_login_url()