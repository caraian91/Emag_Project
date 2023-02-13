from behave import *


@given('home: I am a user on emag.ro Home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()
    context.home_page.click_accept_cookies_btn()
    context.home_page.click_enter_in_account_close_btn()

@when('home: I click on contul meu')
def step_impl(context):
    context.home_page.click_my_account_btn()

@when('home: I search after "{query}"')
def step_impl(context, query):
    context.home_page.search_after(query)

@then('home: I verify login message "{message}"')
def step_impl(context, message):
    context.home_page.verify_login_message(message)

@then('home: I verify home page url')
def step_impl(context):
    context.home_page.verify_url_message()

@when('home: I hover over "{category}"')
def step_impl(context, category):
    context.home_page.hover_over_menu_category(category)

@when('home: I click subcategory "{subcategory}"')
def step_impl(context, subcategory):
    context.home_page.click_menu_subcategory(subcategory)

