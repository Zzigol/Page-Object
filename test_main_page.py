from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # �������������� Page Object, �������� � ����������� ��������� �������� � url ����� 
    page.open()                      # ��������� ��������
    page.go_to_login_page()          # ��������� ����� �������� � ��������� �� �������� ������
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page2 = LoginPage(browser, link)
    page2.open()
    page2.should_be_login_page()

    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()  
    page.should_enter_basket()
    page2 = BasketPage(browser, browser.current_url)
    page2.is_basket_empty()
    page2.should_be_basket_empty_message()