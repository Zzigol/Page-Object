from pages.main_page import MainPage

#python -m  pytest -v --tb=line --language=en test_main_page.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # �������������� Page Object, �������� � ����������� ��������� �������� � url ����� 
    page.open()                      # ��������� ��������
    page.go_to_login_page()          # ��������� ����� �������� � ��������� �� �������� ������
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()