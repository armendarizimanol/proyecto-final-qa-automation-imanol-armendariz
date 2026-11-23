
import json
from pathlib import Path

import pytest

from pages.LoginPage import LoginPage


# Cargamos los datos externos desde el archivo JSON
project_folder = Path(__file__).resolve().parents[1]
data_file = project_folder / "data" / "usuarios.json"

with open(data_file, "r", encoding="utf-8") as file:
    usuarios = json.load(file)


@pytest.mark.parametrize("datos_usuario", usuarios)
def test_login(driver, datos_usuario):

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    login.hacer_login(
        datos_usuario["usuario"],
        datos_usuario["password"]
    )

    if datos_usuario["resultado_esperado"] == "exito":

        assert "/inventory.html" in driver.current_url

    else:

        error_message = driver.find_element(
            "css selector",
            "[data-test='error']"
        )

        assert error_message.is_displayed()
        assert "Epic sadface" in error_message.text
