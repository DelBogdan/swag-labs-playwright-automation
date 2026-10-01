from pages.authentication.login_page import LoginPage


def test_successful_authorization(login_page: LoginPage):
    login_page.visit(url="https://www.saucedemo.com/")
    login_page.email_input.fill("standard_user")
    login_page.password_input.fill("secret_sauce")
    login_page.click_login_button()