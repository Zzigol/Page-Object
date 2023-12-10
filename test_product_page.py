from pages.product_page import ProductPage
#from .pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import random
import time

@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(120)
    product_page.should_not_be_success_message()
    product_page.should_be_book_price()
    
#solve_quiz_and_get_code