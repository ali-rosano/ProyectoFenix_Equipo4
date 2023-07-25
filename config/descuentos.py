import pymysql as MySQLdb
import sqlalchemy

class calculadoraDescuentosPorClases:
    
    #contructor
    def __init__(self) -> None:

        self.clases = ['Bachata', 'Salsa', 'Kizomba', 'Role Rotation']
        self.clase_inscritas = 0
        self.alumnoId = 0
        self.precio = 0
        self.num_clases = 0
        self.tipo_inscripcion = {"FAMILIAR" : -0.1, "REGULAR": precio_total}
        self.familiar = str(0)

        def traerIdInscripcion(query=""):
            db = MySQLdb.connect(host='localhost',user="root",password="admin",db="proyectofenix")
            cursor =  db.cursor()
            cursor.execute(query)

            if query.upper().startswith('SELECT'):
                
                return
        
        def traerIdDescuento():

            return
        
        def descuentosPorPaquetes():
             
            return

        pass
#Precios para los diferentes paquetes y clases sueltas
PRECIO_PAQUETE_35 = 35.0
PRECIO_PAQUETE_40 = 40.0
PRECIO_CLASE_SUelta = 40.0

#Descuentos para los paquetes
DESCUENTO_PAQUETE_SEGUNDA_CLASE = 0.5
DESCUENTO_PAQUETE_TERCERA_CLASE_Y_SIGUIENTES = 0.75

#Descuento para familiares de primer grado
DESCUENTO_FAMILIAR_PRIMER_GRADO = 0.1

def calcular_descuento_clase_paquete(num_clases, precio_paquete):
        if num_clases == 1:
             return precio_paquete
        elif num_clases == 2:
            return precio_paquete + (precio_paquete * DESCUENTO_PAQUETE_SEGUNDA_CLASE)
        else:
            return precio_paquete + (precio_paquete * DESCUENTO_PAQUETE_SEGUNDA_CLASE) + (precio_paquete * DESCUENTO_PAQUETE_TERCERA_CLASE_Y_SIGUIENTES)

def calcular_descuento_clase_suelta():
    return PRECIO_CLASE_SUelta

def calcular_precio_clases_inscritas(alumno):
    total_price = 0.0

    for inscription in alumno.inscriptions:
        if inscription.pack == 'pack_35':
            num_clases = alumno.inscriptions.count(inscription)
            total_price += calcular_descuento_clase_paquete(num_clases, PRECIO_PAQUETE_35)
        elif inscription.pack == 'pack_40':
            num_clases = alumno.inscriptions.count(inscription)
            total_price += calcular_descuento_clase_paquete(num_clases, PRECIO_PAQUETE_40)
        else:
            total_price += calcular_descuento_clase_suelta()

    return total_price

def calcular_precio_total(alumno):
    total_clases = calcular_precio_clases_inscritas(alumno)
    total_descuentos_familiares = 0.0

    for familiar in alumno.familiares:
        total_descuentos_familiares += total_clases * DESCUENTO_FAMILIAR_PRIMER_GRADO

    return total_clases - total_descuentos_familiares