from BasePage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    INPUT_USERNAME = (By.XPATH, '//input[@name="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    BTN_LOGIN = (By.XPATH, '//button[text()="Войти"]')
    BTN_MAIN_PAGE = (By.XPATH, '//button[text()="Главная страница"]')
    
    def enter_username(self, username):
        self.find_element(self.INPUT_USERNAME).send_keys(username)
        
    def enter_password(self, password):
        self.find_element(self.INPUT_PASSWORD).send_keys(password)
            
    def click_btn_login(self):
        self.element_is_clickable(self.BTN_LOGIN).click()
        
    def click_btn_main_page(self):
        self.element_is_clickable(self.BTN_MAIN_PAGE).click()
            
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn_login()    
        
    
        