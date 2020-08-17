import pytest
from pageobjects.login import LogIn
from testdata.userpassword import Users
from Utilities.basesetup import BaseSetup


class TestPermissionsInvalid(BaseSetup):

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

    @pytest.fixture(params=Users.test_users_data_invalid_user)
    def getData(self, request):
        return request.param
