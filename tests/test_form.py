import os.path
from selene import browser, have, be, by
from selene.support.shared.jquery_style import s


class RegistrationPage:
    """Открываем страницу и выполняем проверку"""

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
        s(f'.react-datepicker__day--{day}').click()


def test_student_registration_form():
    """Открываем страницу и выполняем проверку что находимся на нужной странице"""
    registration_page = RegistrationPage()
    registration_page.open()

    """Заполняем Name"""
    registration_page.fill_first_name('Alex')
    registration_page.fill_last_name('Davydov')

    """Заполняем Email"""
    registration_page.fill_email('AlexDavydov92@gmail.com')

    """Заполняем Gender"""
    s('#gender-radio-1').double_click()

    """Заполняем Mobile"""
    s('#userNumber').type('8005553535')

    """Заполняем Date of Birth"""
    registration_page.fill_date_birth("1992", "June", "020")

    """Заполняем Subjects"""
    s('#subjectsInput').should(be.blank).type('English').press_enter()

    """Заполняем Hobbies"""
    s('[for="hobbies-checkbox-2"]').click()

    """Подгружаем Picture"""
    s('#uploadPicture').send_keys(os.path.abspath('image/selfies.jpeg'))

    """Вводим Address"""
    s('#currentAddress').should(be.blank).type('South Street')

    """Выбираем State """
    s('#react-select-3-input').type('Haryana').press_enter()

    """Выбираем  City"""
    s('#react-select-4-input').type('Karnal').press_enter()

    """Нажимаем Отправить"""
    s('#submit').press_enter()

    """Выполняем проверки что форма отправилась и заполнены все поля"""
    s('#example-modal-sizes-title-lg').should(
        have.exact_text('Thanks for submitting the form')
    )
    s('.table-responsive').should(
        have.text(
            'Alex Davydov'
            and 'AlexDavydov92@gmail.com'
            and 'Male'
            and '8005553535'
            and '20 June,1992'
            and 'English'
            and 'Reading'
            and 'selfies.jpeg'
            and 'South Street'
            and 'Haryana Karnal'
        )
    )
