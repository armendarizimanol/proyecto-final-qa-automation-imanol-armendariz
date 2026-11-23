
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver

        self.cart_products = (
            By.CLASS_NAME,
            "inventory_item_name"
        )

        self.cart_title = (
            By.CLASS_NAME,
            "title"
        )

    def obtener_productos_carrito(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.cart_products
            )
        )

        return self.driver.find_elements(
            *self.cart_products
        )

    def obtener_nombre_primer_producto(self):

        productos = self.obtener_productos_carrito()

        return productos[0].text

    def obtener_titulo(self):

        titulo = self.driver.find_element(
            *self.cart_title
        )

        return titulo.text
