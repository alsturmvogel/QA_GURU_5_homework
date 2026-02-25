import pytest
from selene import browser, have

def test_form():
    # Открываем браузер
    browser.open('https://demoqa.com/automation-practice-form')

    # Заполняем текстовые поля
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Петров')
    browser.element('#userEmail').type('ivanov@example.com')

    # Выбираем пол
    browser.element('label[for="gender-radio-1"]').click()

    # Заполняем номер телефона
    browser.element('#userNumber').type('1234567890')

    # Заполняем дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('option[value="1995"]').click()
    browser.element('.react-datepicker__day--010').click()

    # Предмет
    browser.element('#subjectsInput').type('Maths').press_enter()

    # Хобби
    browser.element('label[for="hobbies-checkbox-1"]').click()

    # Адрес
    browser.element('#currentAddress').type('Москва, ул.Гоголя 10')

    # Отправка формы
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
