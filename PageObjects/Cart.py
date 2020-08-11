from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, driver):
        self.driver = driver

    list_prod_name = (By.XPATH, "//*[@class='inventory_item_name']")
    check_out_btn = (By.XPATH, "//*[@id='cart_contents_container']/div/div[2]/a[2]")
    first_name = (By.XPATH, "//*[@id='first-name']")
    last_name = (By.XPATH, "//*[@id='last-name']")
    post_code = (By.XPATH, "//*[@id='postal-code']")
    checkout_continue_btn = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input")
    finish_btn = (By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]/a[2]")
    complete_order = (By.XPATH, "//h2[@class='complete-header']")

    def getprodname(self):
        return self.driver.find_element(*Cart.list_prod_name)

    def clickcheckout(self):
        return self.driver.find_element(*Cart.check_out_btn)

    def getfirstname(self):
        return self.driver.find_element(*Cart.first_name)

    def getlastname(self):
        return self.driver.find_element(*Cart.last_name)

    def getpostcode(self):
        return self.driver.find_element(*Cart.post_code)

    def checkoutcontinue(self):
        return self.driver.find_element(*Cart.checkout_continue_btn)

    def clickfinish(self):
        return self.driver.find_element(*Cart.finish_btn)

    def order(self):
        return self.driver.find_element(*Cart.complete_order)
