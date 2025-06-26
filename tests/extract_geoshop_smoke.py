import os
import logging
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

GEOSHOP_FRONT = os.environ.get("GEOSHOP_FRONT", "http://localhost:8080")
GEOSHOP_BACK = os.environ.get("GEOSHOP_BACK", "http://localhost:8000")
TEST_OUTPUT = os.environ.get("TEST_OUTPUT", "./test_output")

# Geoshop and Extract testing credentials in the username:password format
GEOSHOP_DEMO_LOGIN = tuple(
    os.environ.get("GEOSHOP_DEMO_LOGIN", "admin:Test1234").split(":")
)

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.FileHandler(f"{TEST_OUTPUT}/output.log"))


class GeoshopSmokeTest(unittest.TestCase):

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
        cls._driver = webdriver.Firefox(options=options)

    @classmethod
    def tearDownClass(cls):
        cls._driver.close()

    def take_screenshot(self):
        for i in range(100):
            fname = f"/{TEST_OUTPUT}/screenshot{i}.png"
            if not os.path.exists(fname):
                self._driver.save_screenshot(fname)
                return

    def test_geoshopLoginLogout(self):
        logger.info("Starting Geoshop login/logout test")
        self._driver.get(f"{GEOSHOP_BACK}")
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Geoshop API",
        )
        self.take_screenshot()

        # Login
        self._driver.find_element(By.LINK_TEXT, "Admin").click()
        self.take_screenshot()

        self._driver.find_element(By.ID, "id_username").send_keys(GEOSHOP_DEMO_LOGIN[0])
        self._driver.find_element(By.ID, "id_password").send_keys(GEOSHOP_DEMO_LOGIN[1])
        self.take_screenshot()
        self._driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
        self.take_screenshot()

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

    def test_geoshopFrontendLoginLogout(self):
        logger.info("Starting Geoshop Frontend login/logout test")
        self._driver.get(GEOSHOP_FRONT)
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "GeoShop",
        )

        # Login
        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(2)"
        ).click()
        self._driver.find_element(By.CSS_SELECTOR, ".mat-mdc-menu-content button").click()
        self._driver.find_element(By.CSS_SELECTOR, "input:nth-of-type(1)").send_keys(
            GEOSHOP_DEMO_LOGIN[0]
        )
        self._driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(
            GEOSHOP_DEMO_LOGIN[1]
        )
        self._driver.find_element(By.CSS_SELECTOR, ".form-login-button").click()

        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(2)"
        ).click()
        self.assertEqual(
            self._driver.find_element(
                By.CSS_SELECTOR, ".name-container span"
            ).get_attribute("innerText"),
            GEOSHOP_DEMO_LOGIN[0],
        )

        self._driver.find_element(
            By.CSS_SELECTOR, ".mat-mdc-menu-content button:nth-of-type(3)"
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(2)"
        ).click()
        self.assertRaises(
            NoSuchElementException,
            lambda: self._driver.find_element(
                By.CSS_SELECTOR, ".name-container span"
            ).get_attribute("innerText"),
        )

    def test_geoshopMakeOrder(self):
        logger.info("Starting Geoshop Frontend login/logout test")
        self._driver.get(GEOSHOP_FRONT)
        self.assertEqual(
            self._driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "GeoShop",
        )

        # Login
        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(2)"
        ).click()
        self._driver.find_element(By.CSS_SELECTOR, ".mat-mdc-menu-content button").click()
        self._driver.find_element(By.CSS_SELECTOR, "input:nth-of-type(1)").send_keys(
            GEOSHOP_DEMO_LOGIN[0]
        )
        self._driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(
            GEOSHOP_DEMO_LOGIN[1]
        )
        self._driver.find_element(By.CSS_SELECTOR, ".form-login-button").click()

        # Draw a rectangle
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".map-button-container"))
        )
        self._driver.find_element(
            By.CSS_SELECTOR, ".map-button-container button:nth-of-type(2)"
        ).click()
        map = self._driver.find_element(By.ID, "map")
        ActionChains(self._driver).move_to_element(map).move_by_offset(
            100, 100
        ).click().move_by_offset(200, 200).click().perform()

        # Make an order
        self._driver.find_element(By.CSS_SELECTOR, "button.item-cart").click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(3)"
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".mat-menu-panel button.action-button:nth-of-type(2)"
        ).click()
        self._driver.find_element(By.ID, "mat-select-0").click()
        self._driver.find_element(By.ID, "mat-option-1").click()
        self._driver.find_element(By.ID, "mat-input-6").send_keys("Test input title")
        self._driver.find_element(By.ID, "mat-input-8").send_keys(
            "Test input description"
        )
        self._driver.find_element(By.CSS_SELECTOR, ".mat-stepper-next").click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".bottom-container button:nth-of-type(3)"
        ).click()
        self._driver.find_element(By.ID, "mat-select-value-3").click()
        self._driver.find_element(By.CSS_SELECTOR, ".mat-option:nth-of-type(2)").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#cdk-step-content-0-2 button:nth-of-type(3)"
        ).click()
        self._driver.find_element(By.CSS_SELECTOR, "simple-snack-bar button").click()

        # Logout
        self._driver.find_element(
            By.CSS_SELECTOR, ".right-container button:nth-of-type(2)"
        ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, ".mat-mdc-menu-content button:nth-of-type(3)"
        ).click()


if __name__ == "__main__":
    unittest.main()
