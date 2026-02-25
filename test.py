import pytest
from selene import browser, have, by
from pathlib import Path

file_path = Path(__file__).parent / 'images.jpeg'

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

    #Загружаем картинку
    browser.element('#uploadPicture').send_keys(str(file_path.resolve()))

    # Штат и город
    browser.element('#state').click()
    browser.element('#state').element(by.text("NCR")).click()

    browser.element('#city').click()
    browser.element('#city').element(by.text("Delhi")).click()

    # Адрес
    browser.element('#currentAddress').type('Москва, ул.Гоголя 10')

    # Отправка формы
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    # Проверка
    browser.element('.table-responsive').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Иван Петров',
            'Student Email ivanov@example.com',
            'Gender Male',
            'Mobile 1234567890',
            'Date of Birth 10 February,1995',
            'Subjects Maths',
            'Hobbies Sports',
            'Picture images.jpeg',
            'Address Москва, ул.Гоголя 10',
            'State and City NCR Delhi'
        )
    )