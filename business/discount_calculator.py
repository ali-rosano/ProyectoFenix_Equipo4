from sqlalchemy import select
from config.db import engine
from model.inscriptions import inscriptions
from model.classes import classes
from model.descuentos import descuentos
from model.descuentos_alumnos import descuentos_alumnos
import logging
import pprint
from . import general_functions

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
def calculate_student_total_price(student_id: int) -> float:
    # Función para calcular el precio total con descuento para un estudiante específico

    # Consultar la base de datos para obtener las inscripciones del estudiante
    with engine.connect() as conn:
        query = inscriptions.select().where(inscriptions.c.id_user == student_id)
        result = conn.execute(query)
        rows=result.fetchall()
        logging.info(pprint.pformat(rows))

        packs = {}  # Diccionario para almacenar la cantidad de clases por id_class
        logging.info("test")
        # Aquí agruparemos las clases en sus respectivos paquetes.
        for row in rows:
            logging.info("entré a contar clases")
            class_id = row["id_class"]
            package = general_functions.get_class_by_id(class_id)["pack"]
            if package not in packs: 
                packs[package] = []
            
            packs[package].append({"id_class": class_id})
            #class_count[class_id] = class_count.get(class_id, 0) + 1
        logging.info(packs)
        # Calcular el precio total con los descuentos acumulados
        total_price = 0
        for pack, id_classes in packs.items():
            logging.info(pack)
            for index, class_id in enumerate (id_classes):
                # Obtener el precio base de cada clase y aplicar los descuentos
                logging.info(class_id["id_class"])
                base_price = get_class_base_price_by_id(class_id["id_class"])
                #discount_percentage = get_discount_percentage_by_type(student_id, class_id)
                
                logging.info(f"Iteracion actual: {index}")

    #Como se empieza a contar desde 0, entonces 1 es = 2 y 2= 3....
                if index == 1:
                    discount_percentage = get_discount_percentage_by_type(2) # id descuento segunda clase
                    total_price += base_price * (1 - discount_percentage / 100)
                elif index >=2:
                    discount_percentage = get_discount_percentage_by_type(3) # id descuento tercera clase o mas
                    total_price += base_price * (1 - discount_percentage / 100)


#Buscamos si tiene algun referido
            referido = general_functions.get_student_by_id_user(student_id)["Referido"]

            if referido:
                logging.info("hay referido")
                discount_percentage = get_discount_percentage_by_type(1) # descuento referido
                base_price = base_price * (1 - discount_percentage / 100)

            # Sumar el precio con descuento al precio total
            total_price += base_price
            logging.info(total_price)
        return total_price


def get_class_base_price_by_id(class_id: int) -> float:
    # Lógica para obtener el precio base de la clase a partir del id_class
    with engine.connect() as conn:        
        query = select([classes.c.price]).where(classes.c.id_class == class_id)
        logging.info(class_id)
        result = conn.execute(query).scalar()
        logging.info(pprint.pformat(result))
        return result


def get_discount_percentage_by_type(id_discount: int) -> float:
    # Obtener el porcentaje de descuento según el tipo de descuento
    # para el estudiante y la clase específica
    with engine.connect() as conn:
        query = select([descuentos.c.discount_percent]) \
            .where(descuentos.c.id_discount == id_discount)
        result = conn.execute(query).scalar()
        return result
