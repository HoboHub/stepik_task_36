import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

class TestAddToCart:
    def test_add_to_cart_btn_is_exist(self, browser):
        try:
            browser.implicitly_wait(5)

            link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
            browser.get(link)

            btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
            
            # ошибочный класс. выдаст exception
            # btn = browser.find_element(By.CSS_SELECTOR, ".btd-to-baset")

            # 
            # button = WebDriverWait(browser, 5).until(
            #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
            # )

            if btn:
                print("'Add to cart' button exists!")

        except NoSuchElementException:
            assert False, "No 'Add to cart' button on the page was found during 5 sec"
        
        finally:
            time.sleep(5)
            print('test_add_to_cart_btn_is_exist finished')

# https://stepik.org/lesson/237240/step/10
