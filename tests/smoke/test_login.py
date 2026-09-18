from pages.login import Login

def test_successful_login(driver):
    # Инициализация страниц
    login_page = Login(driver)

    # Открыть страницу входа
    login_page.open("http://mischa3h.beget.tech/admin/login.php")

    # Выполнить вход
    login_page.login("admin", "admin123")

    # Проверить, что попали на главную
    assert "ShopLite" in driver.title