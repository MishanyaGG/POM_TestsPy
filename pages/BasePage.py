from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from conftest import driver

class BasePage:
    """
    Класс для всех страниц сайта
    
    Attributes:
    
        driver: Драйвер бразуера (по умолчанию Chrome)

    Methods:
    
        __init__: конструктор создания стаднартных параметров страницы
        open(url:str): Открывает страницу по указанному URL
        find_element(locator:tuple): Находит элемент с явным ожиданием его появления
        find_elements(locator:tuple): Находит все элементы по локатору
        element_is_visible(locator:tuple): Ждёт, пока элемент станет видимым
        element_is_clickable(locator:tuple): Ждёт, пока элемент станет кликабельным
        get_title(): Возвращает заголовок страницы
        get_current_url(): Возвращает текущий URL.
    """
    
    __driverPage = webdriver.Chrome()
    
    def __init__(self,driver):
        """
        Конструктор создания стаднартных параметров страницы
        1) WEB-драйвер
                Генерирует по умолчанию явное ожидание элементов в 10 секунд
        """
        self.__driverPage = driver
        self.wait = WebDriverWait(self.__driverPage, 10)

    def open(self, url:str):
        """Открывает страницу по указанному URL."""
        self.__driverPage.get(url)

    def find_element(self, locator:tuple):
        """Находит элемент с явным ожиданием его появления."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator:tuple):
        """Находит все элементы по локатору."""
        return self.__driverPage.find_elements(*locator)

    def element_is_visible(self, locator:tuple):
        """Ждёт, пока элемент станет видимым."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator:tuple):
        """Ждёт, пока элемент станет кликабельным."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_title(self) -> str:
        """Возвращает заголовок страницы."""
        return self.__driverPage.title

    def get_current_url(self) -> str:
        """Возвращает текущий URL."""
        return self.__driverPage.current_url
