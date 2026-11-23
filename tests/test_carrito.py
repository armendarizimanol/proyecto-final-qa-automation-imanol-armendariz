
from utils.helpers import iniciar_sesion

from pages.CatalogPage import CatalogPage
from pages.CartPage import CartPage


def test_agregar_producto(driver):

    iniciar_sesion(driver)

    catalogo = CatalogPage(driver)

    catalogo.agregar_primer_producto()

    boton_texto = catalogo.obtener_texto_boton_primer_producto()

    assert boton_texto == "Remove"


def test_contador_carrito(driver):

    iniciar_sesion(driver)

    catalogo = CatalogPage(driver)

    catalogo.agregar_primer_producto()

    contador = catalogo.obtener_contador_carrito()

    assert contador == "1"


def test_navegar_carrito_y_verificar_producto(driver):

    iniciar_sesion(driver)

    catalogo = CatalogPage(driver)

    nombre_producto = catalogo.obtener_nombre_primer_producto()

    catalogo.agregar_primer_producto()

    catalogo.abrir_carrito()

    carrito = CartPage(driver)

    nombre_en_carrito = carrito.obtener_nombre_primer_producto()

    titulo = carrito.obtener_titulo()

    assert nombre_en_carrito == nombre_producto
    assert titulo == "Your Cart"
