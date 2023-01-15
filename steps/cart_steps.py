from behave import *


@then('cart: I verify that total price is correct "{expected_price}"')
def step_impl(context, expected_price):
    context.cart_page.verify_total_price(expected_price)

@when('cart: I click sterge link')
def step_impl(context):
    context.cart_page.click_sterge_link()

@then('cart: I verify empty cart message is displayed')
def step_impl(context):
    context.cart_page.verify_empty_cart_msg()

@when('cart: I click checkout button')
def step_impl(context):
    context.cart_page.click_checkout_btn()