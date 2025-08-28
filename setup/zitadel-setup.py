import os
import shutil
import logging
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

SELENIUM_HOST = os.environ.get("SELENIUM_HOST", "http://selenium:4444") + "/wd/hub"
ZITADEL_HOST = os.environ.get("ZITADEL_HOST", "https://zitadel")

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.FileHandler(f"./output.log"))

logger.info("Starting initial configuration")
options = webdriver.FirefoxOptions()
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
profile.set_preference("app.update.silent", True)
profile.set_preference("app.update.url", "")
profile.set_preference("app.update.auto", False)
profile.set_preference("app.update.enabled", False)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "/keys/")
options.enable_downloads = True
options.profile = profile

driver = webdriver.Remote(command_executor=SELENIUM_HOST, options=options)
driver.implicitly_wait(5)
driver.get(ZITADEL_HOST)

def click(selector, allowNotFound=False):
    try:
        driver.find_element(By.CSS_SELECTOR, selector).click()
    except NoSuchElementException as e:
        if not allowNotFound:
           raise e

def keys(selector, text):
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(text)

def getText(selector):
    return driver.find_element(By.CSS_SELECTOR, selector).text

errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
wait.until(lambda _ : driver.find_element(By.TAG_NAME, "h1").text == "Welcome Back!" or True)

keys("#loginName", "zitadel-admin@zitadel.zitadel")
click("#submit-button")
keys("#password", "Password1!")
click("#submit-button")
click("button[name='skip']", allowNotFound=True)
keys("#change-old-password", "Password1!")
keys("#change-new-password", "Aa!1Aa!1")
keys("#change-password-confirmation", "Aa!1Aa!1")
click("#change-password-button")
click("button[type='submit']")

# Adding a project
driver.get(f"{ZITADEL_HOST}/ui/console/projects/create")
keys("#cnsl-input-0", "Geoshop")
click("button.continue-button")
with open("/keys/project_ids.txt", "a+") as myfile:
    myfile.write(f"project_id\t{getText('.info-row-desc')}\n")

# Adding a frontend
driver.get(f"{ZITADEL_HOST}/ui/console/projects")
click(".card:nth-of-type(2)")
click(".cnsl-app-card.add")
keys("[formcontrolname='name']", "geoshop-front")
click("label[for='UA']")
click("button.mat-stepper-next")
click("label[for='PKCE']")
click("button.mat-stepper-next:nth-of-type(2)")
keys("#cnsl-input-1", "https://geoshop-front/de")
click(".redirect-section button")
keys("#cnsl-input-2", "https://geoshop-front/de")
click(".redirect-section:nth-of-type(2) button")
click("div.app-create-actions:nth-child(7) > button:nth-child(2)")
click("button.create-button")
click("button.ok-button")

with open("/keys/project_ids.txt", "a+") as myfile:
    myfile.write(f"frontend_app_id\t{getText('.copy-row button')}\n")

# Adding a backend
driver.get(f"{ZITADEL_HOST}/ui/console/projects")
click(".card:nth-of-type(2)")
click(".cnsl-app-card.add")
keys("[formcontrolname='name']", "geoshop-backend")
click("label[for='API']")
click("button.mat-stepper-next")
click("label[for='PK_JWT']")
click("button.mat-stepper-next:nth-of-type(2)")
click("button.create-button")
click("button.ok-button")
with open("/keys/project_ids.txt", "a+") as myfile:
    myfile.write(f"backend_app_id\t{getText('.copy-row button')}\n")

# Adding a key
click("cnsl-refresh-table .mdc-button")
click("button.ok-button")
click(".download-button")

keyfile = driver.get_downloadable_files()[0]
driver.download_file(keyfile, "/keys/")
shutil.move(f"/keys/{keyfile}", "/keys/private_key.json")
driver.close()
