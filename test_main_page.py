from pages.main_page import MainPage
from .pages.login_page import LoginPage

#python -m  pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпл€р драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполн€ем метод страницы Ч переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()