
import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utils.logger import logger


@pytest.fixture(scope="function")
def driver():

    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--lang=es")

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    browser.implicitly_wait(10)

    try:
        yield browser
    finally:
        browser.quit()


# Hook para detectar cuando una prueba termina
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if report.passed:
            logger.info(f"PRUEBA APROBADA: {item.name}")

        elif report.failed:
            logger.error(f"PRUEBA FALLIDA: {item.name}")

            browser = item.funcargs.get("driver")

            if browser:

                screenshot_folder = "reports/screenshots"
                os.makedirs(screenshot_folder, exist_ok=True)

                screenshot_path = os.path.join(
                    screenshot_folder,
                    f"{item.name}.png"
                )

                browser.save_screenshot(screenshot_path)

                logger.info(
                    f"Captura guardada en: {screenshot_path}"
                )

        elif report.skipped:
            logger.warning(f"PRUEBA OMITIDA: {item.name}")
