import inspect
import logging
import time

import pytest

from pageobjects.login import LogIn


@pytest.mark.usefixtures("setup")
class BaseSetup:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('././reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger

    def logout(self):
        LogIn.openmenu(self).click()
        time.sleep(4)
        LogIn.logout(self).click()
