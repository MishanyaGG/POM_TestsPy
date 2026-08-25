from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открывает страницу по указанному URL."""
        self.driver.get(self.url)

    def find_element(self, locator):
        """Находит элемент с явным ожиданием его появления."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Находит все элементы по локатору."""
        return self.driver.find_elements(*locator)

    def element_is_visible(self, locator):
        """Ждёт, пока элемент станет видимым."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        """Ждёт, пока элемент станет кликабельным."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_title(self):
        """Возвращает заголовок страницы."""
        return self.driver.title

    def get_current_url(self):
        """Возвращает текущий URL."""
        return self.driver.current_url
