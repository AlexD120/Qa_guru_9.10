import os.path
from selene import have, be
from selene.support.shared.jquery_style import s

from qa_guru_9_10.pages.registration_page import RegistrationPage


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
    registration_page.fill_birthday("1992", "June", "20")

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
    registration_page.should_registered_user_with().should(
        have.text(
            'Alex Davydov'
            and 'AlexDavydov92@gmail.com'
            and 'Male'
            and '8005553535'
            and '20 June,1992'
            and 'English'
            and 'Reading'
            and 'image/selfies.jpeg'
            and 'South Street'
            and 'Haryana Karnal'
        )
    )
