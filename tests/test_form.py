import os.path
from selene import have, be, by
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
    registration_page.fill_gender()

    """Заполняем Mobile"""
    registration_page.fill_user_number('8005553535')

    """Заполняем Date of Birth"""
    registration_page.fill_birthday("1992", "June", "20")

    """Заполняем Subjects"""
    registration_page.fill_subjects('English')

    """Заполняем Hobbies"""
    registration_page.fill_hobbies()

    """Подгружаем Picture"""
    registration_page.fill_picture('image/selfies.jpeg')

    """Вводим Address"""
    registration_page.fill_address('South Street')

    """Выбираем State """
    registration_page.fill_state('Haryana')

    """Выбираем  City"""
    registration_page.fill_city('Karnal')

    """Нажимаем Отправить"""
    registration_page.fill_submit()

    """Выполняем проверки что форма отправилась и заполнены все поля"""
    registration_page.get_should_registered_user_with().should(
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
