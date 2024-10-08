import os
import logging
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

SELENIUM_LOCAL = os.environ.get("SELENIUM_LOCAL", "False") == "True"
SELENIUM_HOST = os.environ.get("SELENIUM_HOST", "http://selenium:4444") + "/wd/hub"
FRONTEND_HOST = os.environ.get("FRONTEND_HOST", "http://frontend")
TEST_OUTPUT = os.environ.get("TEST_OUTPUT", "/test_output")

# Geoshop and Extract testing credentials in the username:password format
EXTRACT_DEMO_LOGIN = tuple(os.environ.get("EXTRACT_DEMO_LOGIN").split(":"))
GEOSHOP_DEMO_LOGIN = tuple(os.environ.get("GEOSHOP_DEMO_LOGIN").split(":"))

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.FileHandler(f"{TEST_OUTPUT}/output.log"))


class ExtractGeoshopSmokeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info("Starting tests")
        options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        profile.set_preference("app.update.silent", True)
        profile.set_preference("app.update.url", "")
        profile.set_preference("app.update.auto", False)
        profile.set_preference("app.update.enabled", False)
        options.profile = profile
        if SELENIUM_LOCAL:
            cls._driver = webdriver.Firefox(options=options)
        else:
            cls._driver = webdriver.Remote(
                command_executor=SELENIUM_HOST, options=options
            )

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    def test_geoshopLoginLogout(self):
        logger.info("Starting Geoshop login/logout test")
        self._driver.get(f"{FRONTEND_HOST}/geoshop")
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Geoshop API",
        )

        # Login
        self._driver.find_element(By.LINK_TEXT, "Admin").click()
        self._driver.find_element(By.ID, "id_username").send_keys(GEOSHOP_DEMO_LOGIN[0])
        self._driver.find_element(By.ID, "id_password").send_keys(GEOSHOP_DEMO_LOGIN[1])
        self._driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()

        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Site administration | GeoShop Admin",
        )

        # Logout
        self._driver.find_element(By.CSS_SELECTOR, "#logout-form button").click()
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Logged out | GeoShop Admin",
        )

    def test_extractLoginLogout(self):
        logger.info("Starting Extract login/logout test")
        self._driver.get(f"{FRONTEND_HOST}/extract")
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Extract",
        )
        # Login
        self._driver.find_element(By.NAME, "username").send_keys(EXTRACT_DEMO_LOGIN[0])
        self._driver.find_element(By.NAME, "password").send_keys(EXTRACT_DEMO_LOGIN[1])
        self._driver.find_element(By.ID, "loginButton").click()
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title")
            .get_attribute("innerText")
            .strip(),
            "Extract – Accueil",
        )
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#currentRequestsTable.loaded")) and
            EC.presence_of_element_located((By.CSS_SELECTOR, "#currentRequestsTable.loaded")))
        time.sleep(5)
        self._driver.find_element(By.ID, "logoutLink").click()
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Extract",
        )


if __name__ == "__main__":
    unittest.main()
