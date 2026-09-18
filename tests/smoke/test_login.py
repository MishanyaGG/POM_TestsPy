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
    
def test_errors_login(driver):
    # Инициализация страниц
        login_page = Login(driver)
    
        # Открыть страницу входа
        login_page.open("http://mischa3h.beget.tech/admin/login.php")
    
        # Выполнить вход с несуществующим логином
        login_page.login(".", "admin123")
        
        assert login_page.get_alert_danger() == "Неверный логин или пароль"
        
        # Открыть страницу входа
        login_page.open("http://mischa3h.beget.tech/admin/login.php")
        
        # Выполнить вход с несуществующим паролем
        login_page.login("admin", "admin1")
        
        assert login_page.get_alert_danger() == "Неверный логин или пароль"
        
        