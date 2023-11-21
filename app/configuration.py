import sys
import configparser
from .logs import logger

#SETTINGS
def get_bot_token() -> str:
    return config.get('Settings', 'token')

def get_name_pc() -> str:
    return config.get('Settings', 'pc_name')

def get_user_id() -> int:
    return config.getint('Settings', 'tg_user_id')

def get_debug() -> bool:
    return config.getboolean('Settings', 'DEBUG')

def get_invterval_sleep() -> tuple:
    return eval(config.get('Settings', 'interval_sleep'))

def get_wait_response() -> int:
    return config.getint('Settings', 'wait_response')

def get_profile_name() -> str:
    return config.get('Settings', 'profile_name')

#PRODUCT
def get_url_product() -> str:
    return config.get('Product', 'url_product')

def get_url_cart() -> str:
    return config.get('Product', 'url_cart')

def get_mod_product() -> str:
    return config.get('Product', 'modificated_product')

def get_purchase_price() -> int:
    return config.getint('Product', 'purchase_price')

#USERS
def get_user_mail() -> str:
    return config.get('Users', 'your_mail')

def get_user_phone() -> str:
    return config.get('Users', 'your_phone')

def get_address_pvz() -> str:
    return config.get('Users', 'adress_option')

#NavigationBrowser
def get_id_select_mod() -> str:
    return config.get('NavigationBrowser', 'id_select_mod')

def get_css_price_product() -> str:
    return config.get('NavigationBrowser', 'xpath_price_product')

def get_css_add_to_cart() -> str:
    return config.get('NavigationBrowser', 'css_add_to_cart')

def get_id_board_go_cart() -> str:
    return config.get('NavigationBrowser', 'id_board_go_cart')

def get_id_board_go_cart() -> str:
    return config.get('NavigationBrowser', 'id_board_go_cart')

def get_name_pvz_select() -> str:
    return config.get('NavigationBrowser', 'name_pvz_select')

def get_css_place_order() -> str:
    return config.get('NavigationBrowser', 'css_place_order')

def get_xpath_pay_but() -> str:
    return config.get('NavigationBrowser', 'xpath_pay_but')

#Robokassa
def get_xpath_send_mail() -> str:
    return config.get('Robokassa', 'xpath_send_mail')

def get_xpath_phone() -> str:
    return config.get('Robokassa', 'xpath_phone')

def get_xpath_send_phone() -> str:
    return config.get('Robokassa', 'xpath_send_phone')

def get_xpath_sberpay() -> str:
    return config.get('Robokassa', 'xpath_sberpay')

try:
    config = configparser.ConfigParser()
    config.read('config.ini', encoding="utf-8")
except Exception as e:
    logger.exception(e)
    sys.exit()