import os.path
from selene import browser, have, be
from selene.support.shared.jquery_style import s


def test_practice_form():
    browser.open('/')

    """Выполняем проверку что находимся на нужной странице"""
    s('.pattern-backgound').should(have.exact_text('Practice Form'))

    """Заполняем Name"""
    s('#firstName').should(be.blank).type("Alex")
    s('#lastName').should(be.blank).type('Davydov')

    """Заполняем Email"""
    s('#userEmail').should(be.blank).type('AlexDavydov92@gmail.com')

    """Заполняем Gender"""
    s('#gender-radio-1').double_click()

    """Заполняем Mobile"""
    s('#userNumber').type('8005553535')

    """Заполняем Date of Birth"""
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().type('June').press_enter()
    s('.react-datepicker__year-select').click().type('1992').press_enter()
    s('.react-datepicker__day--020').click()

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
    s('#submit').click()

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
