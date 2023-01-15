from behave import *
from time import sleep


@when('products: I add to favorites cart the laptop "{product_name}"')
def step_impl(context, product_name):
    context.product_page.add_to_favorites_by_partial_product_name(product_name)

@when('products: I click Produse Favorite')
def step_impl(context):
    context.product_page.click_produse_favorite()

@when('login: I check that i have reached the favorites page url')
def step_impl(context):
    context.login_page.verify_favorites_url()

@when('products: I click on the button Add to Basket from Favorites "{product_name}"')
def step_impl(context, product_name):
    context.product_page.add_to_basket_by_partial_name_but_from_favorites_list(product_name)

@then('products: I click on the delete buton from Favorites "{product_name}"')
def step_impl(context, product_name):
    context.product_page.delete_from_favorites_by_partial_product_name(product_name)