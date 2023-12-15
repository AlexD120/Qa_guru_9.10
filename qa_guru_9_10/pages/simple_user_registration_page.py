from selene import browser, have, be, by
from selene.support.shared.jquery_style import s

from qa_guru_9_10.data.users import User


class SimpleUserRegistrationPage:
    """Открываем страницу и выполняем проверку"""

    def __init__(self):
        self.full_name = s('#userName')
        self.email = s('#userEmail')
        self.current_adress = s('#currentAddress')
        self.permanent_address = s('#permanentAddress')
        self.submit = s('#submit')
        self.should_registered_user_with = s('#output')

    def open(self):
        browser.open('/text-box')
        s('.pattern-backgound').should(have.exact_text('Text Box'))
        return self

    def get_should_registered_user_with(self):
        return self.should_registered_user_with

    def register(self, user: User):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_adress.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit.click()
        self.get_should_registered_user_with().should(
            have.text(
                user.full_name
                and user.email
                and user.current_address
                and user.permanent_address
            )
        )
        return self
