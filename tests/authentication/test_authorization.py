from pages.authentication.login_page import LoginPage


def test_successful_authorization(login_page: LoginPage):
    login_page.visit(url="https://www.saucedemo.com/")
    login_page.email_input.fill("standard_user")
    login_page.password_input.fill("secret_sauce")
    login_page.click_login_button()

def test_wrong_email_and_password_authorization(login_page: LoginPage):
    login_page.visit(url="https://www.saucedemo.com/")
    login_page.email_input.fill("wrong_email")
    login_page.password_input.fill("wrong_password")
    login_page.login_button.click()
    login_page.check_visible_wrong_email_or_password_alert(
        "Epic sadface: Username and password do not match any user in this service"
    )
    login_page.error_component.error_button.click()