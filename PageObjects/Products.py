from selenium.webdriver.common.by import By


class Products:

    def __init__(self, driver):
        self.driver = driver

    product_identify = (By.XPATH, "//a/img")
    product_name = (By.XPATH, "//*[@class='inventory_item_name']")
    product_add_cart = (By.XPATH, "//div[@class='inventory_list']//div/button")
    card_button = (By.XPATH, "//*[@id='shopping_cart_container']/a")

    def identifyprod(self):
        return self.driver.find_element(*Products.product_identify)

    def getproductname(self):
        return self.driver.find_elements(*Products.product_name)

    def addproductcart(self):
        return self.driver.find_element(*Products.product_add_cart)

    def presscard(self):
        return self.driver.find_element(*Products.card_button)
