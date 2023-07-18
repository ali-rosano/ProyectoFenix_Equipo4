import logging
import os


def log_info() -> None:

    archivo = r"C:\Users\ferna\Desktop\Git(Hub)\ProyectoFenix_Equipo4\basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info("This is running right")

    os.chmod(archivo, 0o444)


def log_debug() -> None:

    archivo = r"C:\Users\ferna\Desktop\Git(Hub)\ProyectoFenix_Equipo4\basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.debug("Have a BUG")

    os.chmod(archivo, 0o444)

def log_error() -> None:

    archivo = r"C:\Users\ferna\Desktop\Git(Hub)\ProyectoFenix_Equipo4\basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.error("Hava a ERROR")

    os.chmod(archivo, 0o444)

def log_warning() -> None:

    archivo = r"C:\Users\ferna\Desktop\Git(Hub)\ProyectoFenix_Equipo4\basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.warning("Something is not right. WARNING!!!")

    os.chmod(archivo, 0o444)

def log_critical() -> None:

    archivo = r"C:\Users\ferna\Desktop\Git(Hub)\ProyectoFenix_Equipo4\basic.log"

    os.chmod(archivo, 0o666)

    logger = logging.getLogger("logger")

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("basic.log", mode="a", encoding=None, delay=False, errors=None)

    file_handler.setLevel(logging.DEBUG)

    formatter =  logging.Formatter("%(asctime)s - %(processName)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.critical("All is BAD. CRITICAL!!!")
    
    os.chmod(archivo, 0o444)

