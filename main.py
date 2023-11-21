from random import randint
from app.logs import logger
from app.service import Browser, get_run_time
from app.config_web import interval_sleep, wait_response, url_product, url_cart,\
                             purchase_price, DEBUG
from app.tg_bot import send_msg_err, send_msg_info

br = Browser(wait_response, interval_sleep)

@logger.catch(onerror=lambda err: send_msg_err(err))
def check_price() -> None:
    while True:
        rand = randint(0, 1)
        if rand:
            br.move_mouse_random()
        else:
            br.move_scroll_random()
            
        price = br.get_price_product()
        print(price)
        if purchase_price >= price:
            send_msg_info(url_product, price)
            if DEBUG:
                get_run_time(br.add_to_cart)
                get_run_time(br.get_site, url_cart)

                #work in cart
                get_run_time(br.wait_preloader)
                get_run_time(br.select_pvz)
                get_run_time(br.form_filling)
                get_run_time(br.place_order)
                get_run_time(br.go_to_pay)
                
                #robokassa
                get_run_time(br.form_payment)
            else: 
                br.add_to_cart()
                br.get_site(url_cart)

                #work in cart
                br.wait_preloader()
                br.select_pvz()
                br.place_order()
                br.go_to_pay()
                
                #robokassa
                br.form_payment()
            input('Ожидание пользователя после покупки')
        
        br.timeout()
        br.driver.refresh()


if '__main__' == __name__:
    if DEBUG:
        get_run_time(br.get_site, url_product)
    else:
        br.get_site(url_product)
    check_price()

    input('Ожидание пользователя\n')
    br.close()