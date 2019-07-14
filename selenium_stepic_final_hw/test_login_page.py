from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_is_login_page_login_page(browser):
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_page()
