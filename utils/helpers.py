
from pages.LoginPage import LoginPage
from utils.logger import logger


def iniciar_sesion(driver):

    logger.info("Ingresando a SauceDemo")

    driver.get("https://www.saucedemo.com/")

    logger.info("Completando credenciales de usuario")

    login = LoginPage(driver)

    login.hacer_login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("Proceso de login ejecutado")
