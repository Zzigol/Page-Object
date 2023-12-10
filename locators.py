from selenium.webdriver.common.by import By


class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_EMAIL =(By.CSS_SELECTOR,  '#id_registration-email')
    USER_PASS1 =(By.CSS_SELECTOR,  '#id_registration-password1')
    USER_PASS2 =(By.CSS_SELECTOR,  '#id_registration-password2')
    BUTTON_REGISTER_USER =(By.XPATH,  '//button [@name="registration_submit"]')