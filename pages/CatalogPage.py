
from selenium.webdriver.common.by import By


class CatalogPage:

    def __init__(self, driver):
        self.driver = driver

        self.inventory_items = (
            By.CLASS_NAME,
            "inventory_item"
        )

        self.product_name = (
            By.CLASS_NAME,
            "inventory_item_name"
        )

        self.shopping_cart = (
            By.CLASS_NAME,
            "shopping_cart_link"
        )

        self.cart_badge = (
            By.CLASS_NAME,
            "shopping_cart_badge"
        )

        self.page_title = (
            By.CLASS_NAME,
            "title"
        )

        self.menu_button = (
            By.ID,
            "react-burger-menu-btn"
        )

        self.product_sort = (
            By.CLASS_NAME,
            "product_sort_container"
        )

    def obtener_titulo(self):

        return self.driver.find_element(
            *self.page_title
        ).text

    def obtener_productos(self):

        return self.driver.find_elements(
            *self.inventory_items
        )

    def obtener_cantidad_productos(self):

        return len(self.obtener_productos())

    def obtener_nombre_primer_producto(self):

        productos = self.obtener_productos()

        return productos[0].find_element(
            *self.product_name
        ).text

    def agregar_primer_producto(self):

        productos = self.obtener_productos()

        boton = productos[0].find_element(
            By.TAG_NAME,
            "button"
        )

        boton.click()

    def obtener_texto_boton_primer_producto(self):

        productos = self.obtener_productos()

        boton = productos[0].find_element(
            By.TAG_NAME,
            "button"
        )

        return boton.text

    def obtener_contador_carrito(self):

        return self.driver.find_element(
            *self.cart_badge
        ).text

    def abrir_carrito(self):

        self.driver.find_element(
            *self.shopping_cart
        ).click()

    def menu_visible(self):

        return self.driver.find_element(
            *self.menu_button
        ).is_displayed()

    def ordenamiento_visible(self):

        return self.driver.find_element(
            *self.product_sort
        ).is_displayed()
