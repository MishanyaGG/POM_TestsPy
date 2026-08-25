from basePage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    BTN_ADMIN = (By.XPATH, '//a[@href="/admin/"]')
    INPUT_SEARCH = (By.XPATH,'//input[@name="q"]')
    SELECT_CATEGORY = (By.XPATH,'//select[@name="cat"]')
    INPUT_MIN = (By.XPATH,'//input[@name="min"]')
    INPUT_MAX = (By.XPATH,'//input[@name="max"]')
    SELECT_SORT = (By.XPATH,'//select[@name="sort"]')
    BUTTON_SEARCH = (By.XPATH,'//button[text()="Найти"]')
    
    def btn_admin_click(self):
        return self.element_is_clickable(self.BTN_ADMIN).click()
        
        