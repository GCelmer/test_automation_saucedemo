import time
import pytest
from PageObjects.Cart import Cart
from PageObjects.LogIn import LogIn
from PageObjects.Products import Products
from TestData.UsernPassword import Users
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login_buy(self, getData,getData2):
        log = self.getLogger()
        login = LogIn(self.driver)

        username = getData["username"]
        password = getData["password"]

        login.getusername().send_keys(username)
        login.getpassword().send_keys(password)
        log.info("User:   " + username)

        login.loginpress().click()

        products = Products(self.driver)
        cart = Cart(self.driver)
        log.info("user is able to log in")
        name_prod = products.getproductname()
        i = -1
        for product in name_prod:
            i = i + 1
            title_prod = product.text
            log.info("Product: " + title_prod)
            if title_prod == "Test.allTheThings() T-Shirt (Red)":
                log.info("all products checked")
                products.addproductcart().click()  # clicks on the first item
                # .//button[text()='ADD TO CART'] --clica e torna ele remove
        products.presscard().click()
        cart.clickcheckout().click()

        firstname = getData2["firstname"]
        lastname = getData2["lastname"]
        postcode = getData2["postcode"]

        cart.getfirstname().send_keys(firstname)
        cart.getlastname().send_keys(lastname)
        cart.getpostcode().send_keys(postcode)
        cart.checkoutcontinue().click()
        cart.clickfinish().click()
        order_finalized = cart.order().text
        log.info(order_finalized)
        assert order_finalized == "THANK YOU FOR YOUR ORDER"
        log.info("End-to-end completed successfully")

        self.logout()

    @pytest.fixture(params=Users.test_users_Data)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=Users.test_users_Data_your_details)
    def getData2(self, request):
        return request.param