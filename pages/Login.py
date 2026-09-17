from .basePage import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):
    """
    Класс страницы Логин, является наследником BasePage
    Attributes:
        INPUT_USERNAME (tuple): Поле логина
        INPUT_PASSWORD (tuple): Поле пароля
        BTN_LOGIN (tuple): Кнопка Войти
        BTN_MAIN_PAGE (tuple): Кнопка Главная страница
        
    Methods:
        enter_username(username:str): Ввод значения в поле Логина
        enter_password(self, password:str): Ввод значения в поле Пароль
        click_btn_login(): Клик по кнопке Войти
        click_btn_main_page(): Клик по кнопке Главная страница
        login(username:str, password:str): Авторизация
    """
    
    INPUT_USERNAME = (By.XPATH, '//input[@name="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    BTN_LOGIN = (By.XPATH, '//button[text()="Войти"]')
    BTN_MAIN_PAGE = (By.XPATH, '//button[text()="Главная страница"]')
    
    def enter_username(self, username:str):
        """
        Ввод значения в поле Логина
        
        Args:
            username(string): логин
        """
        
        self.find_element(self.INPUT_USERNAME).send_keys(username)
        
    def enter_password(self, password:str):
        """
        Ввод значения в поле Пароль
                
        Args:
            username(str): логин
        """
        
        self.find_element(self.INPUT_PASSWORD).send_keys(password)
            
    def click_btn_login(self):
        """
        Клик по кнопке Войти
        """
        self.element_is_clickable(self.BTN_LOGIN).click()
        
    def click_btn_main_page(self):
        """
        Клик по кнопке Главная страница
        """
        self.element_is_clickable(self.BTN_MAIN_PAGE).click()
            
    def login(self, username:str, password:str):
        """
        Авторизация
        Args:
            username(str): логин
            password(str): пароль
        """
        
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn_login()    
        
    
        