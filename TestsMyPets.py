import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import email, password

@pytest.fixture(autouse=True)
def test_login():
    pytest.driver = webdriver.Chrome('C:/chromedriver.exe')
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_all_pets():
    # вводим логин и пароль
    pytest.driver.find_element_by_id("email").send_keys(email)
    pytest.driver.find_element_by_id("pass").send_keys(password)

    # нажимаем на кнопку Войти
    pytest.driver.find_element_by_xpath("//button[@type='submit']").click()

    pytest.driver.implicitly_wait(10)

    #переходим на страницу со списком питомцев пользователя
    pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()

    #получаем количество питомцев из статистики
    count_of_my_pets = pytest.driver.find_element_by_css_selector('div.\\.col-sm-4.left').text.split()

    #получаем количество строк из таблицы Все мои питомцы
    all_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr')


    # получаем количество питомцев с фото
    images = pytest.driver.find_elements_by_tag_name('img')

    #получаем имена, возраст, породу через список питомцев
    value_of_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td') # получаем данные из таблицы



    # Проверки:
    # Присутствуют все питомцы,
    for i in range(len(all_my_pets)):
        assert len(all_my_pets) is int(count_of_my_pets[(2)])

    # у половины питомцев есть фото,
    for i in range(len(all_my_pets)):
        assert len(images) / len(all_my_pets) > 0.5

    # У всех питомцев есть имя, возраст и порода,
    for i in range(len(value_of_my_pets)):
        assert value_of_my_pets[i].text != ''

    # У всех питомцев разные имена,
    for i in range(len(names)):
        assert len(names) is len(set(names))

    names = pytest.driver.find_elements_by_xpath('//table/tbody/tr/td[1]')
    for pet in range(len(names)):
        assert names[pet].text != '', "WARNING not all pets have a name"

    images = pytest.driver.find_elements_by_tag_name('img')
    for pet in range(len(names)):
        assert images[i].get_attribute('src') != ''

