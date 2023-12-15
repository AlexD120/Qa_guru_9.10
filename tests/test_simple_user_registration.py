from qa_guru_9_10.application import app
from qa_guru_9_10.data import users
from qa_guru_9_10.pages.profile_page import ProfilePage
from qa_guru_9_10.pages.simple_user_registration_page import SimpleUserRegistrationPage
from selene import browser, have, be, by


def test_registers_user():
    app.simple_registration.open()
    app.simple_registration.register(users.alex)

    app.profile.should_have_data(users.alex)
