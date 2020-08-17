import pytest
from pageobjects.login import LogIn
from testdata.userpassword import Users
from Utilities.basesetup import BaseSetup


class TestPermissionsLockedOut(BaseSetup):

    def test_login_buy(self, getData):
        log = self.getLogger()
        login = LogIn(self.driver)

        username = getData["username"]
        password = getData["password"]

        login.getusername().send_keys(username)
        login.getpassword().send_keys(password)
        log.info("User:   " + username)

        login.loginpress().click()

        if username == "locked_out_user":
            log.info("lock out user")
            message = self.driver.find_element_by_xpath("//*[@id='login_button_container']/div/form/h3").text
            assert "locked out" in message
            log.info(message)
            self.driver.refresh()

    @pytest.fixture(params=Users.test_users_data_locked_out)
    def getData(self, request):
        return request.param
