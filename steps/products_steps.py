import time

from behave import *

@when('products: I add product to basket "{product_name}"')
def step_impl(context, product_name):
    context.product_page.add_to_basket_product_name(product_name)

@when('products: I click Vezi detalii cos')
def step_impl(context):
    context.product_page.click_see_details_cart()

@when('products: Filter by brand "{brand}"')
def step_impl(context, brand):
    context.product_page.filter_by_brand_checkbox(brand)

@when('products: Activate the price range button')
def step_impl(context):
    context.product_page.click_activate_filter_bar_price()

@when('products: We select the slider on the right and enter the price "{slider_selected}" "{xoffset}"')
def step_impl(context, slider_selected , xoffset):
    context.product_page.select_interval_price(slider_selected , xoffset)

@then('products: I check if the search contains the searched result "{query}"')
def step_impl(context, query):
    context.product_page.verify_results_contain_text(query)
