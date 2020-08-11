import pytest
from PageObjects.LogIn import LogIn
from TestData.UsernPassword import Users
from Utilities.BaseClass import BaseClass


class TestPermissionsInvalid(BaseClass):

    def test_login_buy(self, getData):
        log = self.getLogger()
        login = LogIn(self.driver)

        username = getData["username"]
        password = getData["password"]

        login.getusername().send_keys(username)
        login.getpassword().send_keys(password)
        log.info("User:   " + username)

        login.loginpress().click()
        if username == "standard_user1" and password == "secret_sauce1":
            log.info("Wrong user or password")
            message = self.driver.find_element_by_xpath("//*[@id='login_button_container']/div/form/h3").text
            assert "do not match any user" in message
            log.info(message)
            self.driver.refresh()

    @pytest.fixture(params=Users.test_users_Data_invalid_user)
    def getData(self, request):
        return request.param
