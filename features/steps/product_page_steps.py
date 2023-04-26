from behave import when, then, given

@when('Store product name and price')
def store_product_name_n_price(context):
        context.app.product_page.store_product_name_n_price()

@when('Add product to the cart')
def add_product_to_cart(context):
        context.app.product_page.add_product_to_cart()


@when('Open Cart page')
def click_vew_cart_btn(context):
        context.app.product_page.click_vew_cart_btn()