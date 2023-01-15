from behave import *

@when('products: I add product to basket "{product_name}"')
def step_impl(context, product_name):
    context.product_page.add_to_basket_by_partial_product_name(product_name)

@when('products: I click Vezi detalii cos')
def step_impl(context):
    context.product_page.click_vezi_detalii_cos()

@then('products: I verify that results contain search query "{query}"')
def step_impl(context, query):
    context.product_page.verify_results_contain_text(query)
