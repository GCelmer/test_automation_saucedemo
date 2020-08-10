import pytest
from PageObjects.LogIn import LogIn
from TestData.UsernPassword import Users
from Utilities.BaseClass import BaseClass


class TestPermissionsLockedOut(BaseClass):

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

    @pytest.fixture(params=Users.test_users_Data_locked_out)
    def getData(self, request):
        return request.param
