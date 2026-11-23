
import logging
from pathlib import Path


# Definimos la carpeta donde se guardaran los logs
project_folder = Path(__file__).resolve().parent.parent
logs_folder = project_folder / "logs"

# Creamos la carpeta si no existe
logs_folder.mkdir(exist_ok=True)

# Configuramos el archivo de registro
log_file = logs_folder / "automation.log"

logger = logging.getLogger("automation")
logger.setLevel(logging.INFO)

# Evitamos agregar handlers repetidos
if not logger.handlers:

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
