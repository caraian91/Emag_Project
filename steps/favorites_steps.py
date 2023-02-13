from behave import *

@when('favorite: I add to favorites cart the laptop "{product_name}"')
def step_impl(context, product_name):
    context.favorite_page.add_to_favorites_by_product_name(product_name)

@when('favorite: I click on Produse Favorite')
def step_impl(context):
    context.favorite_page.click_produse_favorite()

@when('favorite: I check that i have reached the favorites page url')
def step_impl(context):
    context.favorite_page.verify_favorites_url()

@when('favorite: I click on the button Add to Basket from Favorites "{product_name}"')
def step_impl(context, product_name):
    context.favorite_page.add_to_basket_by_name_but_from_favorites_list(product_name)

@when('favorite: I check the message on the basket to see that it has been added "{quantity}"')
def step_impl(context, quantity):
    context.favorite_page.check_product_in_cart(quantity)

@then('favorite: I click on the delete buton from Favorites "{product_name}"')
def step_impl(context, product_name):
    context.favorite_page.delete_from_favorites_by_product_name(product_name)

