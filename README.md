# Proyecto Final - QA Automation

Este proyecto corresponde a la entrega final del curso de QA Automation.

El objetivo es desarrollar un framework de pruebas automatizadas utilizando Python, Selenium, Pytest y Requests, realizando pruebas sobre una aplicación web y una API pública.

Las pruebas de interfaz se realizan sobre [SauceDemo](https://www.saucedemo.com/) y las pruebas de API sobre [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- WebDriver Manager
- pytest-html
- Git y GitHub
- JSON

## Estructura del proyecto

```text
pre_entrega_QA_automation/
├── data/
│   └── usuarios.json
├── logs/
│   └── automation.log
├── pages/
│   ├── LoginPage.py
│   ├── CatalogPage.py
│   └── CartPage.py
├── reports/
│   ├── reporte.html
│   └── screenshots/
├── tests/
│   ├── api/
│   │   └── test_api.py
│   ├── test_carrito.py
│   ├── test_catalogo.py
│   └── test_login.py
├── utils/
│   ├── helpers.py
│   └── logger.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

### Descripción de las carpetas y archivos

- **data:** contiene los datos externos utilizados en las pruebas, almacenados en formato JSON.
- **pages:** contiene las clases del Page Object Model (POM), con los elementos y acciones de cada página.
- **tests:** contiene las pruebas automatizadas de interfaz y API.
- **tests/api:** contiene los casos de prueba realizados sobre JSONPlaceholder.
- **utils:** contiene funciones auxiliares y la configuración del registro de actividad.
- **logs:** almacena el archivo de registro de las ejecuciones.
- **reports:** guarda el reporte HTML generado por Pytest y las capturas de pantalla de los fallos.
- **conftest.py:** configura el navegador y gestiona el registro de resultados y las capturas ante fallos.
- **pytest.ini:** contiene la configuración de Pytest para generar el reporte HTML.
- **requirements.txt:** contiene las dependencias necesarias para ejecutar el proyecto.

## Pruebas de interfaz (Selenium)

Las pruebas se realizan sobre SauceDemo.

### Login

Se verifican distintos escenarios utilizando datos externos desde `data/usuarios.json`:

- Inicio de sesión con credenciales válidas.
- Intento de inicio de sesión con credenciales incorrectas.
- Intento de inicio de sesión con campos vacíos.

Se utiliza parametrización de Pytest para ejecutar los distintos escenarios con el mismo caso de prueba.

### Catálogo

Se verifica:

- Que la página tenga el título correcto.
- Que aparezca la sección "Products".
- Que existan productos disponibles.
- Que el botón del menú sea visible.
- Que el selector de ordenamiento sea visible.

### Carrito

Se prueba:

- Agregar un producto al carrito.
- Verificar que el botón cambie a "Remove".
- Comprobar el contador del carrito.
- Ingresar al carrito.
- Verificar que el producto agregado aparezca correctamente.

## Pruebas de API (Requests)

Se utiliza JSONPlaceholder como API pública para realizar tres pruebas:

- **GET:** obtener una publicación y verificar el código HTTP 200 y el contenido de la respuesta JSON.
- **POST:** crear una publicación y verificar el código HTTP 201 y los datos enviados.
- **DELETE:** eliminar una publicación y verificar el código HTTP 200.

Se realizan aserciones para comprobar los códigos de respuesta y el contenido recibido.

## Page Object Model (POM)

Se utiliza el patrón Page Object Model para organizar las interacciones con las páginas de la aplicación.

Las clases implementadas son:

- **LoginPage:** contiene los localizadores y las acciones relacionadas con el inicio de sesión.
- **CatalogPage:** contiene las acciones y consultas relacionadas con el catálogo de productos.
- **CartPage:** contiene las consultas relacionadas con los productos dentro del carrito.

De esta manera, los tests quedan separados de las acciones de navegación e interacción con la página.

## Reportes y registros

### Reporte HTML

Pytest genera automáticamente un reporte HTML al ejecutar las pruebas.

El archivo se encuentra en:

`reports/reporte.html`

El reporte permite consultar los resultados de la ejecución, incluyendo las pruebas aprobadas y fallidas.

### Logging

Se utiliza el módulo `logging` de Python para registrar las acciones realizadas durante las pruebas y sus resultados.

Los registros se almacenan en:

`logs/automation.log`

### Capturas de pantalla

Cuando una prueba de interfaz falla durante su ejecución, se intenta guardar una captura de pantalla en:

`reports/screenshots/`

## Instalación y configuración

Se requiere tener Python instalado.

Clonar el repositorio:

```bash
git clone https://github.com/armendarizimanol/pre-entrega-automation-testing-imanol-armendariz.git
```

Ingresar a la carpeta del proyecto:

```bash
cd pre_entrega_QA_automation
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Desde la carpeta principal del proyecto, ejecutar:

```bash
python -m pytest
```

Pytest ejecutará las pruebas de interfaz y API y generará automáticamente el reporte HTML.

## Resultado de la ejecución

En la última ejecución de validación se obtuvieron los siguientes resultados:

- Pruebas ejecutadas: 10.
- Pruebas aprobadas: 10.
- Pruebas fallidas: 0.
- Tiempo de ejecución: 24,25 segundos.

**Resultado: 10 passed.**

## Autor

Imanol Armendáriz

Proyecto realizado como parte de la entrega final del curso de QA Automation.