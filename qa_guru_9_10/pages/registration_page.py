from selene import browser, have, be, by
from selene.support.shared.jquery_style import s


class RegistrationPage:
    """Открываем страницу и выполняем проверку"""

    def __init__(self):
        self.should_registered_user_with = s('.table-responsive')

    def open(self):
        browser.open('/')
        s('.pattern-backgound').should(have.exact_text('Practice Form'))

    """Заполняем Name"""

    def fill_first_name(self, value):
        return s('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        return s('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        return s('#userEmail').should(be.blank).type(value)

    def fill_birthday(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().element(by.text(month)).click()
        s('.react-datepicker__year-select').click().element(by.text(year)).click()
        s(f'.react-datepicker__day--0{day}').click()
