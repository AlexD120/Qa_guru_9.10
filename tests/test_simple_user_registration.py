from qa_guru_9_10.data import users
from qa_guru_9_10.pages.simple_user_registration_page import SimpleUserRegistrationPage
from selene import browser, have, be, by


def test_registers_user():
    registration_page = SimpleUserRegistrationPage()
    alex = users.alex
    registration_page.open()

    """Заполняем Full Name"""
    registration_page.fill(alex)
