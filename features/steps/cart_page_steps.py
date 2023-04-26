from behave import given, then, when

@then('Verify that {expected_num} items shown')
def num_items_in_cart(context, expected_num):
    context.app.cart_page.num_items_in_cart(expected_num)


@then('Verify product name and price')
def verify_product_name_n_price(context):
    context.app.cart_page.verify_product_name_n_price()