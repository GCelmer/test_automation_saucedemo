from selenium.webdriver.common.by import By


class LogIn:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    btn_login = (By.CLASS_NAME, "btn_action")
    open_menu = (By.XPATH, "//*[@class='bm-burger-button']")
    # "//div[@class='bm-burger-button']")
    log_out_menu = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def getusername(self):
        return self.driver.find_element(*LogIn.username)

    def getpassword(self):
        return self.driver.find_element(*LogIn.password)

    def loginpress(self):
        return self.driver.find_element(*LogIn.btn_login)

    def openmenu(self):
        return self.driver.find_element(*LogIn.open_menu)

    def logout(self):
        return self.driver.find_element(*LogIn.log_out_menu)
