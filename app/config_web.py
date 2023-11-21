from .configuration import *

DEBUG = get_debug()
interval_sleep = get_invterval_sleep()
wait_response = get_wait_response()

profile_name = get_profile_name()

your_mail = get_user_mail()
your_phone = get_user_phone()

#product
url_cart = get_url_cart()
url_product = get_url_product()
modificated_product = get_mod_product()
id_select_mod = get_id_select_mod()
purchase_price:int = get_purchase_price()

xpath_price_product = get_css_price_product()

css_add_to_cart = get_css_add_to_cart()
id_board_go_cart = get_id_board_go_cart()

#in cart config order
html_name_pvz_select = get_name_pvz_select()
adress_option = get_address_pvz()

#Оформить заказ
css_place_order = get_css_place_order()

#alphard place order
xpath_pay_but = get_xpath_pay_but()

#robokassa
xpath_send_mail = get_xpath_send_mail()
xpath_sberpay = get_xpath_sberpay()
xpath_phone = get_xpath_phone()
xpath_send_phone = get_xpath_send_phone()