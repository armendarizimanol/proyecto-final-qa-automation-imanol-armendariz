
from utils.helpers import iniciar_sesion
from pages.CatalogPage import CatalogPage


def test_catalogo(driver):

    iniciar_sesion(driver)

    catalogo = CatalogPage(driver)

    # Verificamos el titulo de la pagina
    assert driver.title == "Swag Labs"

    # Verificamos el encabezado del catalogo
    assert catalogo.obtener_titulo() == "Products"

    # Verificamos que existan productos
    cantidad_productos = catalogo.obtener_cantidad_productos()

    assert cantidad_productos > 0

    # Verificamos que el menu este visible
    assert catalogo.menu_visible()

    # Verificamos que el selector de ordenamiento este visible
    assert catalogo.ordenamiento_visible()
