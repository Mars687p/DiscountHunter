from random import choice, randint
import time
from time import sleep

from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from .config_web import *
from .logs import logger


def get_interval_lst(interv:tuple):
    lst: list = []
    for item in range(int(interv[0]*10), int(interv[1]*10) + 1):
        lst.append(float(item/10))
    return lst

def get_run_time(func, *args):
    start = time.time()
    res = func(*args)
    end = time.time()
    logger.info(f'{func.__name__} - {end-start}')
    return res
 

class Browser:
    def __init__(self, wait_response:int, interval_sleep:tuple) -> None:
        self.interval_sleep: tuple = get_interval_lst(interval_sleep)
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'      
        if not DEBUG:
            options.add_argument(profile_name)        
        self.driver = webdriver.Firefox(options=options)

        self.wait = WebDriverWait(self.driver, wait_response, 0.1)
        self.action = ActionChains(self.driver, 100)  
        self.driver.maximize_window()
        self.window_size = tuple(i/2 for i in self.driver.get_window_size().values())

    #imitaion move
    def move_to_elem(self, elem, with_offset: bool = 0):
        try:
            if with_offset:
                self.action.move_to_element_with_offset(elem, 
                                randint(-300, 300),
                                randint(-300, 300))
            else:
                self.action.move_to_element(elem)
            self.action.perform()
        except ValueError:
            logger.warning(f'move_to_elem - Движения вне экрана')

    def move_mouse_random(self):
        try:
            x = randint((-self.window_size[0]), self.window_size[0])
            y = randint((-self.window_size[1]), self.window_size[1])
            self.action.w3c_actions.pointer_action.move_to_location(*self.window_size)
            self.action.move_by_offset(x, y).perform()
        except exceptions.MoveTargetOutOfBoundsException:
            logger.warning(f'move_mouse_random - Движения вне видимой области')
    
    def move_scroll_random(self):
        y = randint(80, 180)
        try:
            self.action.scroll_by_amount(0, y).perform()
            sleep(0.2)
            self.action.scroll_by_amount(0, -y).perform()
        except exceptions.MoveTargetOutOfBoundsException:
            logger.warning(f'move_scroll_random - Движения вне видимой области')
            

    #wait load js preloader
    def wait_preloader(self) -> None:
        preloader = self.driver.find_element(By.ID, 'preloader')
        self.wait.until(EC.invisibility_of_element(preloader))

    #click() or execute script
    def scroll_handler(self, but) -> None:
        try:
            but.click()
        except exceptions.ElementNotInteractableException: 
            logger.info('Обработка исключения скролл')
            self.driver.execute_script("arguments[0].click();", but)
    

    def get_site(self, url):
        self.driver.get(url)

    def get_price_product(self):
        price = self.wait.until(EC.presence_of_element_located((By.XPATH, 
                                    xpath_price_product)))
        self.move_to_elem(price)
        price = price.text
        price = int(price.split()[0])
        return price

    def add_to_cart(self) -> None:
        if modificated_product != '':
            select = self.driver.find_element(By.ID, id_select_mod)
            select = Select(select)
            select.select_by_visible_text(modificated_product)
            elem = self.driver.find_element(By.CSS_SELECTOR, css_add_to_cart)\
                        .find_elements(By.TAG_NAME, 'a')
            elem = [i for i in elem if i.is_displayed()][0]
        else:
            elem = self.driver.find_element(By.CSS_SELECTOR, css_add_to_cart)\
                              .find_element(By.TAG_NAME, 'a')

        self.wait.until(EC.visibility_of(elem))
        self.driver.execute_script("arguments[0].click();", elem)
        elem_board_cart = self.driver.find_element(By.ID, id_board_go_cart)
        self.wait.until(EC.visibility_of(elem_board_cart))

    def select_pvz(self) -> None:
        select = self.driver.find_element(By.NAME, html_name_pvz_select)
        select = Select(select)
        select.select_by_value(adress_option)

    def place_order(self) -> None:
        but_place_order = self.driver.find_element(By.CSS_SELECTOR, css_place_order)
        self.scroll_handler(but_place_order)

    def go_to_pay(self) -> None:        
        self.wait_preloader()
        pay_but = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_pay_but)))
        self.scroll_handler(pay_but)        

    def form_payment(self) -> None:
        #wait load DOM
        but_sberpay = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_sberpay)))
        #write mail and click sberpay
        mail = self.driver.find_element(By.XPATH, xpath_send_mail)
        mail.send_keys(your_mail)
        but_sberpay.click()

        #wait load DOM
        phone = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_phone)))
        phone.send_keys(your_phone)
        send_phone = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath_send_phone)))
        self.driver.execute_script("arguments[0].click();", send_phone)

    #for test. Random data
    def form_filling(self) -> None:
        first_name = self.driver.find_element(By.NAME, 'first_name')
        first_name.send_keys('Тест Тестович Тестов')

        passport = self.driver.find_element(By.NAME, 'passport')
        passport.send_keys('0000 000000')
        
        phone = self.driver.find_element(By.NAME, 'phone')
        phone.send_keys('9169999999')
        
        email = self.driver.find_element(By.NAME, 'email')
        email.send_keys('test@yandex.ru')

    def timeout(self):
        interv = choice(self.interval_sleep)
        sleep(interv)
        return interv

    def close(self) -> None:
        self.driver.close()    
        




    