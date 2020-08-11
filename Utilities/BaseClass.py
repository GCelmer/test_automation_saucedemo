import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from PageObjects.LogIn import LogIn


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('/Users/gabrielijungcelmer/PycharmProjects/test_automation_saucedemo/Reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def logout(self):
        LogIn.openmenu(self).click()
        time.sleep(4)
        LogIn.logout(self).click()
